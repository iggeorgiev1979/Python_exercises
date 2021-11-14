from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.memory = memory
        self.capacity = capacity
        self.hardware_type = hardware_type
        self.name = name
        self.software_components = []
        self.available_memory = self.memory
        self.available_capacity = self.capacity

    def install(self, software):
        if self.available_capacity >= software.capacity_consumption and self.available_memory >= software.memory_consumption:
            self.software_components.append(software)
            self.available_capacity -= software.capacity_consumption
            self.available_memory -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.available_memory += software.memory_consumption
            self.available_capacity += software.capacity_consumption

    def __repr__(self):
        number_of_installed_light_software = len([software for software in self.software_components if isinstance(software, LightSoftware)])
        number_of_installed_express_software = len([software for software in self.software_components if isinstance(software, ExpressSoftware)])
        if self.software_components:
            list_of_names = ", ".join([software.name for software in self.software_components])
        else:
            list_of_names = "None"
        return f"Hardware Component - {self.name}\n" \
               f"Express Software Components: {number_of_installed_express_software}\n" \
               f"Light Software Components: {number_of_installed_light_software}\n" \
               f"Memory Usage: {self.memory - self.available_memory} / {self.memory}\n" \
               f"Capacity Usage: {self.capacity - self.available_capacity} / {self.capacity}\n" \
               f"Type: {self.hardware_type}\n" \
               f"Software Components: {list_of_names}"


