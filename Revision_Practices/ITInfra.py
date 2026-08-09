

class Device:

    device_connected = 0

    def __init__(self, name, ip, status):
        self.name = name
        self.ip = ip
        self.status = status
        Device.device_connected += 1

    def show_info(self):
        print(f"{self.name} has ip:{self.ip} status:{self.status}")

class NetworkDevices(Device):

    def port20(self):
        print("Connected to port:20")

    def port141(self):
        print("Connected to port:141")
    

class Router(NetworkDevices):
    def OSPF(self):
        print("Follows OSPF protocol")

    def TPC(self):
        print("Uses TCP protocal")


class Computer(Device):

    def linux(self):
        print("Running: Linux")

    def windows(self):
        print("Running: Windows")


class ComputerNetwork(NetworkDevices, Computer):

    def server01(self):
        print("Host: Server 01")

    def server02(self):
        print("Host: Server 04")

router = Router("Router1", "192.168.1.1", "Up")
computer = Computer("Laptop1", "192.168.1.10", "Up")
network_computer = ComputerNetwork("Server1", "192.168.1.100", "Up")


router.show_info()
computer.show_info()
router.OSPF()
computer.linux()
network_computer.show_info()
network_computer.port20()
network_computer.linux()
network_computer.server01()
print(f"Total devices: {Device.device_connected}")
