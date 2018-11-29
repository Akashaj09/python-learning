import datetime as d
import calendar as c

print(d.date.today())
daa = "2018-12-12"
mmmm = d.datetime.strptime(daa, "%Y-%m-%d")
print(mmmm)

balance = 5000
interest_rate = 13*0.1
monthly_payment = 200

today = d.date.today()
days_in_current_month = c.monthrange(today.year, today.month)[1]
day_till_month = days_in_current_month-today.day

start_date = today + d.timedelta(days=day_till_month+1)

end_date = start_date
while balance > 0:
    interest_charge = (interest_rate/12) * balance
    balance += interest_charge
    balance -= monthly_payment
    balance = 0 if balance < 0 else round(balance, 2)
    print(end_date, balance)
    days_in_current_month = c.monthrange(end_date.year, end_date.month)[1]
    end_date = today + d.timedelta(days=days_in_current_month)