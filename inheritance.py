class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        


class Liabrian(Person):
    def __init__(self, name, email,salary):
        super().__init__(name, email)
        self.salary=salary



class Member(Person):
    def __init__(self, name, email,mem_id):
        super().__init__(name, email)
        self.mem_id= mem_id




liabrian = Liabrian("mahnoor", "mahnoor@gmail.com",24567)
print(liabrian.name)

member= Member('Zoraiz','zoraiz@gmail.com', 'mem_986')
print(member.mem_id)