# ENCAPSULATION
class Library:
    def __init__(self,name):
        self.name = name
        # Declaring private variable with double underscore
        self.__expenses = {'salary':1234, 'ke_bill':134}

# Getter Function
    def get_expenses(self):
        return self.__expenses


# Setter Function
    def update_expenses(self,update_exp):
        #  self.__expenses = {'salary':1234, 
        #                     'ke_bill':134,
        #                     'furniture':345678}
         self.__expenses= update_exp

         return self.__expenses
        





lib = Library('Kiswa')
print(lib.get_expenses())
print(lib.update_expenses({'furniture':3456}))