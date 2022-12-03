"""
Task 1
Create a python script that connects to all 3 routers using Telnet protocol
No need to output any data
"""
import telnetlib
import time


class Telnet:
    def __init__(self, host):
        self.__host = host
        self.__session = None

    def __del__(self):
        self.__session.close()

    def connect(self):
        self.__session = telnetlib.Telnet(host=self.__host, port=23)
        self.__session.read_until(b"Username: ")
        self.__session.write(b"u1\n")
        self.__session.read_until(b"Password: ")
        self.__session.write(b"cisco\n")

    def send_command(self, command, st=2):
        self.__session.write(b"terminal length 0\n")
        self.__session.write(command.encode() + b"\n")
        time.sleep(st)
        self.__session.write(b"exit\n")
        return self.__session.read_all().decode()


t1 = Telnet("192.168.122.10")
t1.connect()

t2 = Telnet("192.168.122.20")
t2.connect()

t3 = Telnet("192.168.122.30")
t3.connect()

print(t1.send_command("show clock", 3))
print(t2.send_command("show version", 3))
print(t3.send_command("show interfaces", 3))