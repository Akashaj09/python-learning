class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullName(self):
        return self.first_name+" "+self.last_name

    def email(self):
        return self.first_name.lower()+self.last_name.lower()+"@gmail.com"

user = User("Akash", "Aj")

print(user.email())