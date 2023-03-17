class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        print(self.email)
        self.account.display_account_info()
        print(self.account.balance)
        return self


class BankAccount:
    # don't forget to add some default values for these parameters!
  def __init__(self, int_rate=0.1, balance=0): 
    self.int_rate = int_rate
    self.balance = balance


  def deposit(self, amount):
    self.balance += amount
    print(self.balance)
    return self

  def withdraw(self, amount):
    if amount < self.balance:
      self.balance = self.balance - amount
      return self
    else:
      print("Insufficient funds Charging a $5 fee")
      self.balance -= 5
      print(f"your new balance is: ${self.balance}")
      return self


  def display_account_info(self):
    print(self.balance)
    return self

  def yield_interest(self):
      self.balance *= (1 + self.int_rate)
      print(self.balance)
      return self

gokhan_acc = User("Gokhan", "gokhan@hotmail.com")
gokhan_acc.make_deposit(100).make_withdrawal(80).display_user_balance()

# bank_acc1 = BankAccount(0.1, 100)
# bank_acc2 = BankAccount(0.01, 200)

# bank_acc1.deposit(10).deposit(20).withdraw(50).yield_interest().display_account_info()
# bank_acc2.deposit(20).deposit(30).withdraw(5).withdraw(10).withdraw(15).withdraw(30).yield_interest().display_account_info()

