first = b"Hello"
second = "World".encode()


print(first, second)
print(first.decode(), second.decode())

print(first[0])
print(chr(first[0]))
print(first.decode()[0])

name = b"Mikael"
print(name)

for i in range(len(name)):
    print(name.decode()[i], "is", name[i])