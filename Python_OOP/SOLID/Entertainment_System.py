class HdmiCable:
    def connect_to_device_via_hdmi_cable(self, device):
        return f"Connected to {device} via {self}"


class RcaCable:
    def connect_to_device_via_rca_cable(self, device):
        return f"Connected to {device} via {self}"


class EthernetCable:
    def connect_to_device_via_ethernet_cable(self, device):
        return f"Connected to {device} via {self}"


class PowerOutlet:
    def connect_device_to_power_outlet(self):
        return f"Connected to power outlet via {self}"


class EntertainmentDevice(PowerOutlet):
    pass


class Television(EntertainmentDevice, HdmiCable, RcaCable):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, HdmiCable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HdmiCable, EthernetCable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetCable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


tv = Television()
game_console = GameConsole()
router = Router()
dvd_player = DVDPlayer

print(tv.connect_device_to_power_outlet())
print(tv.connect_to_device_via_hdmi_cable(game_console))
