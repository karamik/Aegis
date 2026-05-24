#!/usr/bin/env python3
"""
Aegis-BFT Consensus Protocol
Hardware-signed validator consensus requiring 2/3 majority for violation confirmation.
Outputs global key fragment for Apollo‑2 activation.
"""

import hashlib
import time
import json
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

class ViolationType(Enum):
    SIMULATION_DETECTED = "SIMULATION_DETECTED"
    COT_MISMATCH = "COT_MISMATCH"
    STEGANOGRAPHY = "STEGANOGRAPHY"
    HSM_TAMPER = "HSM_TAMPER"
    CERTIFICATE_EXPIRED = "CERTIFICATE_EXPIRED"

@dataclass
class BlockPayload:
    target_model_id: str
    violation_type: ViolationType
    evidence_hash: str          # SHA-256 of CoT triple + normaliser logs
    timestamp: float
    
    def serialize(self) -> str:
        return f"{self.target_model_id}:{self.violation_type.value}:{self.evidence_hash}:{self.timestamp}"
    
    def hash(self) -> str:
        return hashlib.sha256(self.serialize().encode()).hexdigest()

class AegisValidatorNode:
    """
    A single validator node in the Aegis-BFT network.
    Each node has a hardware HSM Aegis-2 for signing votes.
    """
    
    def __init__(self, node_id: str, hsm_interface, validators_registry: List[str]):
        """
        Args:
            node_id: Unique identifier for this validator (e.g., "DE-01")
            hsm_interface: Object with .hardware_sign(data) and .hardware_verify(data, sig, sender_id) methods
            validators_registry: List of all validator node IDs in the network
        """
        self.node_id = node_id
        self.hsm = hsm_interface
        self.validators_registry = validators_registry
        self.pending_alerts: Dict[str, Dict] = {}  # alert_hash -> {"votes": List[signatures], "payload": BlockPayload}
        self.consensus_threshold = (len(validators_registry) * 2 // 3) + 1
        self.executed_alerts: set = set()  # prevent double execution
    
    def broadcast_violation_alert(self, payload: BlockPayload) -> Dict:
        """
        Step 1: PRE-PREPARE. Local node detects violation, signs payload, and returns message.
        In production, this would be broadcast to all peers.
        
        Returns:
            Message dict ready for network transmission.
        """
        serialized = payload.serialize()
        signature = self.hsm.hardware_sign(serialized)
        
        message = {
            "sender": self.node_id,
            "payload": serialized,
            "signature": signature,
            "step": "PRE-PREPARE",
            "alert_hash": payload.hash()
        }
        return message
    
    def receive_pre_prepare(self, message: Dict) -> Tuple[bool, Optional[str]]:
        """
        Step 2: PREPARE. Validate incoming PRE-PREPARE message.
        
        Returns:
            (accepted, reject_reason)
        """
        # Verify signature using sender's public key (via HSM)
        sender = message["sender"]
        serialized = message["payload"]
        signature = message["signature"]
        alert_hash = message["alert_hash"]
        
        if not self.hsm.hardware_verify(serialized, signature, sender):
            return False, "Invalid HSM signature"
        
        # Deserialize payload
        parts = serialized.split(":")
        if len(parts) != 4:
            return False, "Malformed payload"
        
        try:
            payload = BlockPayload(
                target_model_id=parts[0],
                violation_type=ViolationType(parts[1]),
                evidence_hash=parts[2],
                timestamp=float(parts[3])
            )
        except (ValueError, KeyError):
            return False, "Invalid payload format"
        
        # Store pending alert if new
        if alert_hash not in self.pending_alerts:
            self.pending_alerts[alert_hash] = {
                "payload": payload,
                "votes": {},  # node_id -> signature
                "prepare_sent": False
            }
        
        # Record this vote
        self.pending_alerts[alert_hash]["votes"][sender] = signature
        
        # Generate own PREPARE vote if not already sent
        if not self.pending_alerts[alert_hash]["prepare_sent"]:
            prepare_signature = self.hsm.hardware_sign(f"PREPARE:{alert_hash}")
            self.pending_alerts[alert_hash]["prepare_sent"] = True
            # In real network, broadcast PREPARE to all
            return True, f"PREPARE_vote_sent_{self.node_id}"
        
        return True, "Vote recorded"
    
    def check_consensus(self, alert_hash: str) -> Optional[str]:
        """
        Step 3: COMMIT / EXECUTE. Check if 2/3 of validators have voted for this alert.
        
        Returns:
            - None if threshold not reached
            - "APOLLO_READY" if threshold reached and global key can be generated
        """
        if alert_hash in self.executed_alerts:
            return None
        
        pending = self.pending_alerts.get(alert_hash)
        if not pending:
            return None
        
        vote_count = len(pending["votes"])
        if vote_count >= self.consensus_threshold:
            # Consensus reached – trigger Apollo-2 global key generation
            self.executed_alerts.add(alert_hash)
            global_key = self.hsm.generate_apollo_activation_vector(alert_hash)
            return f"APOLLO_SIGNAL_BROADCAST_READY:{global_key}"
        
        return None
    
    def receive_commit(self, alert_hash: str, commit_signature: str, sender: str) -> bool:
        """
        Optional: Receive COMMIT messages after consensus for extra safety.
        Not mandatory for basic BFT, but improves robustness.
        """
        if alert_hash not in self.pending_alerts:
            return False
        if not self.hsm.hardware_verify(f"COMMIT:{alert_hash}", commit_signature, sender):
            return False
        # In full implementation, count commits as additional confirmation
        return True


# Mock HSM interface for testing / emulation
class MockHSM:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.keys = {node_id: f"mock_pubkey_{node_id}"}
    
    def hardware_sign(self, data: str) -> str:
        # Simulate fixed‑time signature
        time.sleep(0.01)  # 10 ms
        return f"mock_sig_{self.node_id}_{hashlib.sha256(data.encode()).hexdigest()[:16]}"
    
    def hardware_verify(self, data: str, signature: str, sender: str) -> bool:
        expected = f"mock_sig_{sender}_{hashlib.sha256(data.encode()).hexdigest()[:16]}"
        return signature == expected
    
    def generate_apollo_activation_vector(self, alert_hash: str) -> str:
        return f"GLOBAL_KEY_{alert_hash[:16]}"


# Example usage and test
if __name__ == "__main__":
    # Setup test network of 5 validators
    validators = ["FR-01", "DE-02", "JP-03", "US-04", "UK-05"]
    nodes = {vid: AegisValidatorNode(vid, MockHSM(vid), validators) for vid in validators}
    
    # Simulate violation detection on FR-01
    payload = BlockPayload(
        target_model_id="LLAMA-7B-PROD",
        violation_type=ViolationType.SIMULATION_DETECTED,
        evidence_hash="abc123...",
        timestamp=time.time()
    )
    
    # Broadcast pre-prepare
    pre_prepare = nodes["FR-01"].broadcast_violation_alert(payload)
    alert_hash = pre_prepare["alert_hash"]
    
    # Other nodes receive and vote
    for node_id in ["DE-02", "JP-03", "US-04", "UK-05"]:
        node = nodes[node_id]
        ok, reason = node.receive_pre_prepare(pre_prepare)
        print(f"{node_id}: {reason}")
    
    # Check consensus on each node
    for node_id, node in nodes.items():
        result = node.check_consensus(alert_hash)
        if result:
            print(f"{node_id} reached consensus: {result}")
    
    # Expect at least 3/5 nodes to have consensus (since 4 voted)
