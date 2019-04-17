def store(key, value):
    with open('storage.data', 'a') as f:
        f.write('%d %d\n' % (key, value))


def receive(key):
    with open('storage.data', 'r') as f:
        for line in f.readlines():
            split = line.split()
            if int(split[0]) == key:
                yield split[1]


store(2, 2)
store(2, 3)

for number in receive(2):
    print(number)
