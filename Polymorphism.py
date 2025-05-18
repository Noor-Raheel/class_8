# POLYMORPHISM
# same method with different behaviour
# polymorphism happens after inheritance
# same function should be defined
# implemmentation could be different
# Method Overriding
class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    def get_info(self):
        return f"{self.name}"
        

class Liabrian(Person):
    def __init__(self, name, email,salary):
        super().__init__(name, email)
        self.salary=salary

    def get_info(self):
        pass



class Member(Person):
    def __init__(self, name, email,mem_id):
        super().__init__(name, email)
        self.mem_id= mem_id
        # def get_info(self):
        #   return {
        #       'name':self.name,
        #       'mem_id':self.mem_id
        #   }





liabrian = Liabrian("mahnoor", "mahnoor@gmail.com",24567)
# print(liabrian.name)

member= Member('Zoraiz','zoraiz@gmail.com', 'mem_986')
# print(member.mem_id)
print(member.get_info())