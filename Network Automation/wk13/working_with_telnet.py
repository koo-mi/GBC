import telnetlib
import time

t = telnetlib.Telnet(host="192.168.122.10", port=23)
t.read_until(b"Username: ")
t.write(b"u1\n")

t.read_until(b"Password: ")
t.write(b"cisco" + "\n".encode())

t.write(b"terminal length 0\n")
t.write(b"show version\n")
time.sleep(1)

t.write(b"exit\n")

output = t.read_all().decode()
print(output)
