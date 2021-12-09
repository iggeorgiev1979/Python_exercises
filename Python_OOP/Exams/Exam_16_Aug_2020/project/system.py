import sys
sys.path.append(".")

from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware

class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))
    
    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))
    
    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [el for el in System._hardware if el.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        # except Exception as ex:
        #     return str(ex)
    
    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [el for el in System._hardware if el.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        # except Exception as ex:
        #     return str(ex)
    
    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [el for el in System._hardware if el.name == hardware_name][0]
            software = [el for el in System._software if el.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"
    
    @staticmethod
    def analyze():
        number_of_hardware_components = len(System._hardware)
        number_of_software_components = len(System._software)
        total_memory_consumption = sum(el.memory_consumption for el in System._software)
        total_memory = sum(el.memory for el in System._hardware)
        total_capacity_consumption = sum(el.capacity_consumption for el in System._software)
        total_capacity = sum(el.capacity for el in System._hardware)

        return f"""System Analysis
Hardware Components: {number_of_hardware_components}
Software Components: {number_of_software_components}
Total Operational Memory: {total_memory_consumption} / {total_memory}
Total Capacity Taken: {total_capacity_consumption} / {total_capacity}"""
        
    @staticmethod
    def system_split():
        return "\n".join([str(el) for el in System._hardware])
      