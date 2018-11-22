class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def setRaisAmount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, empl_str):
        first, last, email, pay = empl_str.split("-")
        return cls(first, last, email, int(pay))

    @staticmethod
    def is_workDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    pass
employe_str = 'John-Doe-jsss-70000000'
newEmploye = Developer.from_string(employe_str)
Employee.setRaisAmount(1.5)
newEmploye.apply_raise()
print(newEmploye.pay)

