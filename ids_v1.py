import time
import random

# Simulated network IPs
sample_ips = [
    "192.168.1.2",
    "192.168.1.5",
    "10.0.0.8",
    "172.16.0.3"
]

# Track activity
ip_count = {}

print("Mini IDS Started... 🔥")
print("Monitoring simulated network traffic...\n")

while True:

    # Simulate incoming packet
    source_ip = random.choice(sample_ips)

    if source_ip not in ip_count:
        ip_count[source_ip] = 1
    else:
        ip_count[source_ip] += 1

    print(f"[+] Traffic from {source_ip} | Count: {ip_count[source_ip]}")

    # Detection threshold
    if ip_count[source_ip] >= 5:

        alert = f"[ALERT] Suspicious activity detected from {source_ip} at {time.ctime()}"

        print(alert)

        with open("logs/alerts.log", "a") as log:
            log.write(alert + "\n")

        # Reset count after alert
        ip_count[source_ip] = 0

    time.sleep(1)
