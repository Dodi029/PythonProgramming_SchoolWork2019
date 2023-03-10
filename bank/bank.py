class BankAccount:
    def __init__(self, name, number, balance):
        self.__balance= balance
        self.name = name
        self.number= number

    def withdraw(self, amount):
        self.__balance-= amount
        return self.__balance

    def deposit(self, amount):
        self.__balance+= amount
        return self.__balance
    def __repr__(self):
        return repr((self.__balance))
class SavingsAccount(BankAccount):
    def __init__(self,  name, number, balance,  interest_rate):
            super().__init__( name, number, balance)
            self.interest_rate=interest_rate

    def set_interest_rate(self, interest_rate):
            self.interest_rate= interest_rate

    def get_interest_rate(self):
       return self.interest_rate

    def add_interest(self):
        self.__balance+= self.__balance*self.interest_rate

    def __repr__(self):
        return super().__repr__()

class CheckingAccount(BankAccount):
    def __init__(self,  name, number, balance):
       super().__init__( name, number, balance)
       self.withdraw_charge= 10000# 수표발행수수료
    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)

    def __repr__(self):
        return super().__repr__()