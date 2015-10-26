__author__ = 'frankie'
import os

coin_vals = {'pennies':.01,'nickles':.05,'dimes':.10,'quarters':.25,'half_dollars':.50,'dollars':1.00}

class User:
    current_bank_id = 0
    name = "test"
    num_of_accounts = 0

    def __init__(self, bank_id, name, num_of_accounts):
        self._bank_id = User.current_bank_id
        User.current_bank_id = User.current_bank_id + 1
        self._name = User.name
        User._num_of_accounts = User.num_of_accounts
        self._num_of_accounts = User.num_of_accounts

    def new_user(self,name):
        self._name = name
        return self._bank_id


class Account:
    current_acct_nu = 100

    def __init__(self, acct_nu):
        self._acct_nu = Account.current_acct_nu + 1
        self._balance = 0
        self._pennies = 0
        self._nickles = 0
        self._dimes = 0
        self._quarters = 0
        self._half_dollars = 0
        self._dollars = 0

    def __str__(self):
        #return str(self, name)
        pass

    def deposit(self, acct_nu):
        pennies = int(input("Number of pennies to deposit -> "))
        Account._pennies = Account._pennies + pennies
        nickles = int(input("Number of nickles to deposit -> "))
        Account._nickles = Account._nickles + nickles
        dimes = int(input("Number of dimes to deposit -> "))
        Account._dimes = Account._dimes + dimes
        quarters = int(input("Number of quarters to deposit -> "))
        Account._quarters = Account._quarters + quarters
        half_dollars = int(input("Number of half-dollars to deposit -> "))
        Account._half_dollars = Account._half_dollars + half_dollars
        dollars = int(input("Number of dollars to deposit -> "))
        Account._dollars = Account._dollars + dollars
        print("Your current total: (in all accounts)")
        return pennies, nickles, dimes, quarters, half_dollars, dollars

    def withdraw(self, acct_nu, amount):
        pass

    @property
    def balance(self):
        return self._pennies + self._nickles + self._dimes + self._quarters + self._half_dollars + self._dollars

    def transfer(self, acct_to, acct_from, amount):
        pass


def interface():
    # Who is using the bank?
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome = int(input("Welcome to the First Bank of Matratze!\nEnter your user ID# or enter '0' to open a new account: "))
    x = 0
    while x == 0:
        if welcome == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("----------------------------\nWelcome new user!\nPlease enter some basic info: \n----------------------------")
            name = raw_input("Your Name -> ")
            num_accounts = int(input("How many accounts do you wish to open? "))
            bug_out = raw_input("Would you like one to be a bug-out bag? (y,n): ")
            user_add = User(User.current_bank_id,name,num_accounts)
            print(type(user_add.new_user(name)))
            print("Your ID# is {}\nYour account number(s) are: {}".format(user_add.new_user(name),"derp"))
            raw_input("Press Enter to continue...")
            welcome = 1
            #Account.deposit()
        else:
            # For selected user, show "accounts (bags)"
            x = 1
        while x == 1:
            x = 2
            if x == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Welcome, {} -- ID#: {}\n----------------------------\nSelect account: \n1) QUIT\n2) Create new savings account\n3) {}\n----------------------------".format(User.name,welcome,User.num_of_accounts))
                option = int(input("-> "))
                if option == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    #SAVE FUNCTION GOES HERE save_to_disk()
                    os._exit(0)
                elif option == 2:
                    #NEW BANK ACCOUNT FUNCTION HERE
                    User.num_of_accounts = User.num_of_accounts + 1
                    next_acct = Account.current_acct_nu + 1
                    Account.__init__()
                    x = 1
                else:
                    x = 3
                while x == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Account number: {}\nWhat do you want to do?\n----------------------------\n1) Back...\n2) Withdraw\n3) Deposit\n4) Transfer\n5) Get Balance\n-----------------------------")
                    option = int(input("(1-5) -> "))
                    if option == 5:
                        Account.
                        raw_input("Press Enter to continue...")
                        pass
                    elif option == 4:
                        raw_input("Press Enter to continue...")
                        pass
                    elif option == 3:
                        raw_input("Press Enter to continue...")
                        pass
                    elif option == 2:
                        raw_input("Press Enter to continue...")
                        pass
                    elif option == 1:
                        x = 1
                    else:
                        print("Error: Enter (1-5): ")
                        raw_input("Press Enter to continue...")


# Save to disk
def save_to_disk():
    pass

# Convert currency types


if __name__ == '__main__':
    interface()