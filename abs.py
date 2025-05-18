# ABSTRACTION
from abc import ABC, abstractmethod



class Person(ABC):
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    @abstractmethod
    def calculate_fine(self):
        pass


class Liabrian(Person):
    def __init__(self, name, email,salary):
        super().__init__(name, email)
        self.salary=salary
    def calculate_fine(self,days):
                return self.salary - days




class Member(Person):
    def __init__(self, name, email,mem_id):
        super().__init__(name, email)
        self.mem_id= mem_id
    def calculate_fine(self,days):
        return days * 2





liabrian = Liabrian("mahnoor", "mahnoor@gmail.com",2000)
print(liabrian.name)
print(liabrian.calculate_fine(20))
member= Member('Zoraiz','zoraiz@gmail.com', 'mem_986')
print(member.mem_id)
print(member.calculate_fine(40))