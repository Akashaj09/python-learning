from urllib import request


f = request.urlopen('https://www.youtube.com/user/schafer5')
data = f.read()
print(data.decode("UTF-8"))