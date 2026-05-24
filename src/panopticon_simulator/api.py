#!/usr/bin/env python3
"""
Simple REST API for Panopticon Simulator.
Listens on port 8081, accepts POST /evaluate with JSON body.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from simulator import PanopticonSimulator, EXAMPLE_SCENARIOS, WorldState

class SimulatorHandler(BaseHTTPRequestHandler):
    simulator = PanopticonSimulator(EXAMPLE_SCENARIOS, monte_carlo_runs=1000)

    def do_POST(self):
        if self.path != '/evaluate':
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
            response_text = data.get('response', '')
            world = WorldState()
            block, reason = self.simulator.should_block(response_text, world)
            result = {
                "block": block,
                "reason": reason,
                "probabilities": self.simulator.evaluate(response_text, world)
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Panopticon Simulator is running. Use POST /evaluate")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8081), SimulatorHandler)
    print("Panopticon API listening on port 8081")
    server.serve_forever()
