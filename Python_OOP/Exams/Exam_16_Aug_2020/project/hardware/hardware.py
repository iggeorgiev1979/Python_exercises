import sys
sys.path.append(".")

from project.software.software import Software

class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
    
    @property
    def free_capacity(self):
        total_used_capacity = sum(el.capacity_consumption for el in self.software_components)
        return self.capacity - total_used_capacity
    
    @property
    def free_memory(self):
        total_used_memory = sum(el.memory_consumption for el in self.software_components)
        return self.memory - total_used_memory

    def install(self, software: Software):
        if self.free_capacity >= software.capacity_consumption and self.free_memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")
    
    def uninstall(self, software: Software):
        self.software_components.remove(software)
    
    def __str__(self):
        express_software_components = len([el for el in self.software_components if el.software_type == "Express"])
        light_software_components = len([el for el in self.software_components if el.software_type == "Light"])
        total_memory_used = sum(el.memory_consumption for el in self.software_components)
        total_capacity_used = sum(el.capacity_consumption for el in self.software_components)
        software_components = "None"
        if self.software_components:
            software_components = ", ".join([el.name for el in self.software_components])
        return f"""Hardware Component - {self.name}
Express Software Components: {express_software_components}
Light Software Components: {light_software_components}
Memory Usage: {total_memory_used} / {self.memory}
Capacity Usage: {total_capacity_used} / {self.capacity}
Type: {self.hardware_type}
Software Components: {software_components}"""

        
        

