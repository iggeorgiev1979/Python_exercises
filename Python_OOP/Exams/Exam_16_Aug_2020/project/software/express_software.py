import sys
sys.path.append("..")
from project.software.software import Software

class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", capacity_consumption, memory_consumption * 2)
    