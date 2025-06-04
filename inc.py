class AccountBank:
    name_bank = "Mono"
    __balance = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value: int):
        if isinstance(value, (int, float)):
            self.__balance = value
        else:
            raise ValueError("Balance is INT")
        
    @balance.deleter
    def balance(self):
        del self.balance

account = AccountBank("Катя", 18)
print(account.balance)
account.balance = "100"
print(account.balance)
