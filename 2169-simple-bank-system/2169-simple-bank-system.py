class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.valid_length = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.valid_length or account2 > self.valid_length:
            return False

        if money > self.balance[account1 - 1]:
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        if account > self.valid_length:
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.valid_length:
            return False

        if(money > self.balance[account - 1]):
            return False
        
        self.balance[account - 1] -= money
        return True