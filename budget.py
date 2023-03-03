class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spend = 0

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
        if not self.withd["description"].startswith("Transfer"):
            self.spend += amount

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
            data = "\n%-20s %-9s" % (entry["description"], entry["amount"])
            st += data
        st = st + (f"\nTotal: {self.balance}")

        return st


def create_spend_chart(categories):
    total = 0
    percent = {}
    for category in categories:
        total += category.spend
    for category in categories:
        percent[category.name] = round(category.spend / total * 10, 0)
        print(percent)
    for i in range(10):
        print(str(100 - 10 * i).rjust(3), "|", end="")
        for category in categories:
            if i < (10 - percent[category.name]):
                continue
            print("o", end="  ")
        print("\n")
    print("   ", "---" * len(categories))
    for i in range(20):
        print("     ", end="")
        for category in categories:
            if i < len(category.name):
                print(category.name[i], end="  ")
            else:
                print(" ", end="  ")
        print("\n")