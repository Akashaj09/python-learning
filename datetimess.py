import datetime as d

print(d.date.today())
daa = "2018-12-12"
mmmm = d.datetime.strptime(daa, "%Y-%m-%d")

print(mmmm)
