import telnetlib
from time import sleep


class MyTelnet:
    def __init__(self, host, user, pwd):
        self.__host = host
        self.__user = user
        self.__pwd = pwd
        self.__session = None

    def __del__(self):
        self.__session.close()

    def connect(self):
        self.__session = telnetlib.Telnet(
            host=self.__host,
            port=23)
        self.__session.read_until(b"Username: ")
        self.__session.write(self.__user.encode() + b"\n")
        self.__session.read_until(b"Password: ")
        self.__session.write(self.__pwd.encode() + b"\n")

    def send_command(self, command, t=2):
        self.__session.write(b"terminal length 0\n")
        self.__session.write(command.encode() + b"\n")
        sleep(t)
        self.__session.write(b"exit\n")
        return self.__session.read_all().decode()
