class Bank:

    def __init__(self, initial_amount=0.00):
     self.balance = initial_amount
    
    def log_transaction(self,transaction_string):
       with open("transaction.txt","a") as file:
          file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")

    def withdrawal(self,amount):
       try:
          amount = float(amount)
       except ValueError:
          amount = 0
       if amount:    
        self.balance = self.balance - amount
        self.log_transaction(f"Withdrew {amount}")

    def deposit(self,amount):
       try:
           amount = float(amount)
       except ValueError:
          amount = 0 
       if amount:    
        self.balance = self.balance + amount
        self.log_transaction(f"Deposited {amount}")


account = Bank(100)   
while True:
   try:
    action = input("what kind of transactions you wanna do today ?\n")
   except KeyboardInterrupt:
      print("\nThanks for visiting ABC Bannk , Adios sayonara !!") 
      break
   if action in ["withdrawal","deposit"]:
      if action == "withdrawal":
         amount = input("How much Money you want to take out ?")
         account.withdrawal(amount)
      else:
         amount = input("How much money do you want to deposit ?")
         account.deposit(amount)

      print("Your new balance is", account.balance)   
   else:
      print("error !! Sorry that is not valid option .... Try again ")     





