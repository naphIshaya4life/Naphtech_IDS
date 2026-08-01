
"""
Detection Engine for Naphtech IDS
Developer: Naphtali Ishaya
Company: Naphtech Hub
"""

import random
import time

from config import load_config
from logger import log_info, log_alert


class DetectionEngine:
    """Core detection engine."""

    def __init__(self):
        config = load_config()

        self.threshold = config["packet_threshold"]

        self.sample_ips = [
            "192.168.1.2",
            "192.168.1.5",
            "10.0.0.8",
            "172.16.0.3"
        ]

        self.ip_count = {}

        log_info("Detection Engine initialized.")

    def simulate_packet(self):
        """Return a simulated source IP."""

        return random.choice(self.sample_ips)

    def process_packet(self, source_ip):
        """Process incoming traffic."""

        self.ip_count[source_ip] = self.ip_count.get(source_ip, 0) + 1

        print(f"[+] {source_ip} | Count: {self.ip_count[source_ip]}")

        if self.ip_count[source_ip] >= self.threshold:

            message = (
                f"Suspicious activity detected from "
                f"{source_ip}"
            )

            print(f"[ALERT] {message}")

            log_alert(message)

            self.ip_count[source_ip] = 0

    def monitor_network(self):
        """Start monitoring."""

        log_info("Monitoring started.")

        try:

            while True:

                ip = self.simulate_packet()

                self.process_packet(ip)

                time.sleep(1)

        except KeyboardInterrupt:

            print("\nMonitoring stopped.")

            log_info("Monitoring stopped by user.")

