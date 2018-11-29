from contextlib import contextmanager


class OpenFile ():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open ( self.filename, self.mode )
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close ()


with OpenFile('simple.text', 'w') as f:
    f.write("Hello fucking world.\nI am coming")

print(f.closed)


# using generator
@contextmanager
def open_file(file, mode):
    try:
        f = open ( file, mode )
        yield f
    finally:
        f.close()


with open_file('contexxx.text', 'w') as f:
    f.write("Hey there,\n Its my start to new journey")


