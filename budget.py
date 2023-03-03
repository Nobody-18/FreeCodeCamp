class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.depo = {}
        self.depo["amount"] = amount
        self.depo["description"] = description
        self.ledger.append(self.depo)
        self.balance += amount

    def withdraw(self, amount, description=""):
        if amount > self.balance:
            return False
        self.withd = {}
        self.withd["amount"] = -amount
        self.withd["description"] = description
        self.ledger.append(self.withd)
        self.balance -= amount
        return True

    def get_balance(self):
        print(f"The remaining balance is {self.balance}")

    def transfer(self, amount, Category):
        if amount > self.balance:
            return False
        self.withdraw(amount, f"Transfer to {Category.name}")
        Category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        st = self.name.center(30, "*")
        for entry in self.ledger:
            data = "\n%-23s %-9s" % (entry["description"], entry["amount"])
            st += data
        st = st + (f"\nTotal: {self.balance}")

        return st


food = Category("food")
Clothing = Category("Clothing")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restraunt and more food")
food.transfer(50, Clothing)
print(food)
print(Clothing)
