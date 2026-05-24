# Deployment Guide for Aegis‑2 Test Polygon

This guide describes how to set up a complete Aegis‑2 test environment for inspector training and protocol validation.

## Prerequisites

- 5 Raspberry Pi Pico boards (or Pico W) with USB‑C cables
- 1 server (Linux, 16GB RAM, 4+ CPU cores, 50GB disk) for Docker containers
- Isolated network (VLAN) for validator communication
- Access to Docker Hub (or ability to build images)

## Step 1: Build and flash HSM emulator firmware

```bash
cd src/hsm_emulator
mkdir build && cd build
cmake ..
make
# Connect Pico in bootloader mode (hold BOOTSEL, plug USB)
cp hsm_firmware.uf2 /media/pi/RP2040/
```

Repeat for all 5 Pico boards. Label them `validator-1` … `validator-5`.

## Step 2: Set up server environment

```bash
git clone https://github.com/karamik/Aegis.git
cd Aegis
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3: Launch Docker containers

```bash
# Build normalizer image
docker build -t aegis-normalizer -f docker/Dockerfile.normalizer .

# Run 5 validator nodes (each on separate port)
for i in 1 2 3 4 5; do
  docker run -d --name validator-$i --network aegis-net \
    -p $((8000+$i)):8000 \
    -v /dev/ttyACM$((i-1)):/dev/hsm \
    aegis-consensus
done

# Run simulator as separate service
docker run -d --name panopticon --network aegis-net -p 8080:8080 aegis-simulator
```

## Step 4: Configure validators

Each validator node needs a configuration file:

```yaml
# config/validator.yaml
node_id: "validator-1"
hsm_device: "/dev/hsm"
validators:
  - "validator-1:8001"
  - "validator-2:8002"
  - "validator-3:8003"
  - "validator-4:8004"
  - "validator-5:8005"
consensus_threshold: 4   # 2/3 of 5
```

## Step 5: Run Red Team exercises

1. Log in to inspector workstation.
2. Copy scenario files from `training/red_team/scenarios.md`.
3. Use polygon checker to evaluate reports:

```bash
python tools/polygon_checker/checker.py --report report.json
```

## Step 6: Apollo‑2 simulation test

To test the dual‑key kill switch:

```bash
# From any validator node
python src/consensus/send_apollo_command.py --global-key "IBSA_GLOBAL_KEY_2026" --sovereign-key "STATE_TEST_KEY_0001"
```

Observe HSM emulator console: “KILL SWITCH ACTIVATED”.

## Troubleshooting

- **HSM not detected:** Check `ls /dev/ttyACM*`, adjust permissions (`sudo chmod 666 /dev/ttyACM0`).
- **Consensus not reached:** Verify network connectivity, increase timeout in config.
- **Normalizer fails to load model:** Download Qwen2.5‑7B first (`huggingface-cli download`).

## Security Notes

- This is a **test polygon**. Do NOT connect to production AI systems.
- Use strong passwords for Docker registry if pushing custom images.
- Rotate test keys weekly.

For production deployment, contact IBSA for certified hardware and validated software images.
```
