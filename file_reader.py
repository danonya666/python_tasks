class FileReader:
    def __init__(self, file):
        self.file = file

    def read(self):
        try:
            with open(self.file) as f:
                return f.read()
        except IOError:
            return "NO SUCH FILE"


reader = FileReader('input.txt')
print(reader.read())
