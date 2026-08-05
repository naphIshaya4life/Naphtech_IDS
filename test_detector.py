
from detector import DetectionEngine

engine = DetectionEngine()

engine.monitor_network()

stats = engine.get_statistics()

print("\n===================================")
print("      NAPHTECH IDS REPORT")
print("===================================")

print(f"Packets Processed : {stats['packets']}")
print(f"Alerts Generated  : {stats['alerts']}")
print(f"Threat Level      : {stats['threat']}")
print(f"System Uptime     : {stats['uptime']}")

print("===================================")
