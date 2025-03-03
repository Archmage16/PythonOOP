import random as rd

class Member:
    total_family_money = 0
    
    def __init__(self, name, Total_expense, Income):
        self.__name = name
        self.__Cur_expense = rd.randint(0, Total_expense)
        self.__Income = Income
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def Income(self):
        return self.__Income
    @Income.setter
    def Income(self, Income):
        self.__Income = Income
    @property

    def Cur_expense(self):
        return self.__Cur_expense
    @Cur_expense.setter
    def Cur_expense(self, new_expense):
        self.__Cur_expense = new_expense


    def Input(self):
        self.name = input("Enter name: ")
        self.Total_expense = int(input("Enter total expense: "))
        self.Income = int(input("Enter income: "))
        
    @staticmethod
    def set_money(money):
        Member.total_family_money += money
    
    def spend_money(self):
        Member.total_family_money -= self.Cur_expense
        return Member.total_family_money
    
    def __str__(self):
        print("-"*20)
        return f"Name: {self.name}\nTotal expense: {str(self.Total_expense)}\nIncome: {str(self.Income)}"
        
    



Mom = Member("Mom", 100, 5000)
Dad = Member("Dad", 200, 6000)
Son = Member("Son", 30, 0)
Daughter = Member("Daughter", 80, 0)


l = Mom.Income + Dad.Income + Son.Income + Daughter.Income
Member.set_money(l) 
print(f"Total family money: {Member.total_family_money}$")

for i in range(0, 7):
    Mom.spend_money()
    Dad.spend_money()
    Son.spend_money()
    Daughter.spend_money()
    print(f"Left money: {Member.total_family_money}$")


