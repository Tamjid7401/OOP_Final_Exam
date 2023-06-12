class Bank: 
    account_number_counter = 1000
    def __init__(self, name, NID): 
        self.name = name
        self.NID = NID
        self.account_number = Bank.account_number_counter
        self.balance = 0
        self.loan_amount = 0
        self.money_transaction = []
        Bank.account_number_counter += 1

    def deposit(self, amount): 
        self.balance += amount 
        self.money_transaction.append(f'Cash Deposit: BDT {amount}')
        print("Congratulations! You've deposited BDT", amount)
    
    def withdraw(self, amount): 
        if self.balance >= amount: 
            self.balance -= amount 
            self.money_transaction.append(f'Cash Withdrawl: BDT {amount}')
            print("Congratulations! You've Successfully withdrawl BDT", amount)
        elif self.balance == 0:
            print("The Bank is Bankrupt")
        else:
            print("Not Available Balance")
    
    def transfer(self, amount, receiver): 
        if self.balance >= amount: 
            self.balance -= amount 
            receiver.balance += amount 
            self.money_transaction.append(f"Balance Transfer: BDT {amount}")
            receiver.money_transaction.append(f"Cash Received: BDT {amount}")
            print(f"Successful Money Transfer from {self.name} to {receiver.name}")
        else: 
            print("Not enough money. Please deposit first")
    

    def get_loan(self, amount): 
        if amount <= 2*self.balance: 
            self.loan_amount += amount 
            self.money_transaction.append(f"Loan: BDT {amount}")
            print(f"Success! Loan Approved: BDT {amount}")
        else:
            print("Loan Application Declined")  
    def loan_control(self):
        quit(Bank.get_loan(user1,10000))
    
    
    def transaction_history(self):
        print("Transaction History:") 
        for string in self.money_transaction:
            print(f"...{string}...")


class Customer(Bank):
    def __init__(self, name, NID):
        super().__init__(name, NID)
        
    def create_account(self): 
        print(self.name,"Account created succesfully. Your account number is:", self.account_number) 
    
    def balance_inquiry(self):
        if self.balance > 0:
            print("Available Balance is BDT", self.balance)
        else:
            print("Your current balance is BDT 0, Please deposit.")

class Admin(Bank): 
    account_number_counter = 10
    def __init__(self, name, NID):
        super().__init__(name, NID)
        self.name = name
        self.customers = []
        self.account_number = Admin.account_number_counter
        Admin.account_number_counter += 1

    def create_account(self,): 
        print(self.name,"Account created succesfully. Your account number is:", self.account_number)

    def add_customer(self, customer): 
        self.customers.append(customer) 
        print(f"Customer added successfully.")
    
    def available_balance(self): 
        bank_balance = sum(customer.balance for customer in self.customers) 
        print(f"Total available balance of the Bank is: BDT {bank_balance}")
   
    def total_loan_amount(self): 
        total_loan_amount = sum(customer.loan_amount for customer in self.customers ) 
        print(f"Total loan amount of the Bank is: BDT {total_loan_amount}")

user1 = Customer("Mohammad", 123456789)
user2 = Customer("Tamjid", 987654321)

user1.create_account() # Mohammad Account created succesfully. Your account number is: 1000
user2.create_account() # Tamjid Account created succesfully. Your account number is: 1001

user1.deposit(5000) # Congratulations! You've deposited BDT 5000
user1.balance_inquiry() # Available Balance is BDT 5000
user1.withdraw(1000) # Congratulations! You've Successfully withdrawl BDT 1000
user1.balance_inquiry() # Available Balance is BDT 4000

user2.balance_inquiry() # Your current balance is BDT 0, Please deposit.
user2.withdraw(1000) # The Bank is Bankrupt
user1.transfer(1000, user2) # Successful Money Transfer from Mohammad to Tamjid
user2.deposit(5000) # Congratulations! You've deposited BDT 5000
user2.balance_inquiry() # Available Balance is BDT 6000

user1.get_loan(4000) # Success! Loan Approved: BDT 4000
user2.get_loan(2000) # Success! Loan Approved: BDT 2000

user1.transaction_history() # Transaction History:
                            #...Cash Deposit: BDT 5000...
                            #...Cash Withdrawl: BDT 1000...
                            #...Balance Transfer: BDT 1000...
                            #...Loan: BDT 4000...
user2.transaction_history() # Transaction History:
                            #...Cash Received: BDT 1000...
                            #...Cash Deposit: BDT 5000...
                            #...Loan: BDT 2000...

admin1 = Admin("Adnan", 998877665)

admin1.create_account() # Adnan Account created succesfully. Your account number is: 10
admin1.add_customer(user1) # Customer added successfully.
admin1.add_customer(user2) # Customer added successfully.

admin1.available_balance() # Total available balance of the Bank is: BDT 9000
admin1.total_loan_amount() # Total loan amount of the Bank is: BDT 6000

# admin1.loan_control() # If called below two will get declined
# user1.get_loan(1000) # Loan Application Declined
# user2.get_loan(1000) # Loan Application Declined