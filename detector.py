

"""
Naphtech IDS - Detection Engine
Developer: Naphtali Ishaya
Company: Naphtech Hub
"""

import random
import time

from config import load_config
from logger import log_info, log_alert


class DetectionEngine:
    """Core Intrusion Detection Engine."""

    def __init__(self):
        """Initialize the detection engine."""

        config = load_config()

        self.threshold = config["packet_threshold"]

        self.sample_ips = [
            "192.168.1.2",
            "192.168.1.5",
            "10.0.0.8",
            "172.16.0.3"
        ]

        self.ip_count = {}

        # Statistics
        self.total_packets = 0
        self.total_alerts = 0
        self.start_time = time.time()

        log_info("Detection Engine initialized.")

    def simulate_packet(self):
        """Simulate an incoming packet."""

        return random.choice(self.sample_ips)

    def process_packet(self, source_ip):
        """Process a network packet."""

        # Count every packet
        self.total_packets += 1

        # Count packets per IP
        self.ip_count[source_ip] = self.ip_count.get(source_ip, 0) + 1

        print(f"[+] {source_ip} | Count: {self.ip_count[source_ip]}")

        # Detect suspicious activity
        if self.ip_count[source_ip] >= self.threshold:

            message = f"Suspicious activity detected from {source_ip}"

            print(f"[ALERT] {message}")

            log_alert(message)


            # Reset counter after alert
            self.ip_count[source_ip] = 0

    def monitor_network(self):
        """Start monitoring."""

        log_info("Monitoring started.")

        try:
            while True:

                packet = self.simulate_packet()

                self.process_packet(packet)

                time.sleep(1)

        except KeyboardInterrupt:

            print("\nMonitoring stopped.")

            log_info("Monitoring stopped by user.")

    def get_threat_level(self):
        """Return the current threat level."""

        if self.total_alerts == 0:
            return "LOW"

        elif self.total_alerts <= 3:
            return "MEDIUM"

        elif self.total_alerts <= 6:
            return "HIGH"

        return "CRITICAL"

    def get_threat_meter(self):
        """
        Return a visual threat meter based on the
        current number of detected security alerts.
        """

        if self.total_alerts == 0:
            return "🟢 ▓░░░░░░░░ 10%"

        elif self.total_alerts <= 3:
            return "🟡 ▓▓▓░░░░░░ 40%"

        elif self.total_alerts <= 6:
            return "🟠 ▓▓▓▓▓▓░░░ 70%"

        else:
            return "🔴 ▓▓▓▓▓▓▓▓▓ 100%"





    def get_uptime(self):
        """Return formatted uptime."""

        uptime = int(time.time() - self.start_time)

        hours = uptime // 3600
        minutes = (uptime % 3600) // 60
        seconds = uptime % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"



    def get_statistics(self) -> dict:
        """
        Return current IDS statistics.
        """

        return {
            "packets": self.total_packets,
            "alerts": self.total_alerts,
            "unique_ips": len(self.ip_count),
            "threat": self.get_threat_level(),
            "meter": self.get_threat_meter(),
            "uptime": self.get_uptime()
        }






