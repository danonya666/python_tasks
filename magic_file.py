import tempfile
import os


class File(object):
    def __init__(self, path):
        self.path = path
        self.file = open(os.curdir + path, 'a+')
        self.file.write('file opened!')

    def write(self, text):
        self.file.write(text)

    def __add__(self, other):
        data = self.get_data() + other.get_data()
        temp_path = tempfile.gettempdir()
        temp_path = temp_path + self.path
        try:
            file = open(temp_path, 'a+')
        except FileNotFoundError:
            os.makedirs(temp_path)
            file = open(temp_path, 'a+')
        file.write(data)
        print(f'wrote {data} to {file}')

        return file

    def get_data(self):
        self.file.write('smth')
        data = self.file.read()
        print(f'file = {self.file}')
        return data


obj = File('\\tmp\\file.txt')

obj.write('line\n')

first = File('\\tmp\\first.txt')
second = File('\\tmp\\second.txt')
new_obj = first + second

obj = File('\\tmp\\file.txt')

print(obj.get_data())
