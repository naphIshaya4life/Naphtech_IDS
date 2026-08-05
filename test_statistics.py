
from detector import DetectionEngine

engine = DetectionEngine()

try:
    engine.monitor_network()
except KeyboardInterrupt:
    pass

print("\n===== IDS Statistics =====")
print(engine.get_statistics())
