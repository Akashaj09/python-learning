# text file

f = open("filess/guido_bio.txt")

text = f.read()

print(text)

f.close()

with open("filess/guido_bio.txt") as a:
    bio = a.read()

print(bio)