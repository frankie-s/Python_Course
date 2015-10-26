__author__ = 'frankie'
import os


class User:
    current_bank_id = 0
    name = "test"
    num_of_accounts = 0

    def __init__(self, name):
        self._name = User.name
        User.name = name
        self._bank_id = User.current_bank_id
        User.current_bank_id = User.current_bank_id + 1
        self._num_of_accounts = User.num_of_accounts
        User._num_of_accounts = User.num_of_accounts

    def new_user(self,name):
        self._name = name
        return self._bank_id


class Bank:
    def __init__(self):
        self._listofusers = []
        self._listofaccounts = []


class Account:
    current_acct_nu = 100
    initial_balance = 0

    def __init__(self):
        self._balance = Account.initial_balance
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

    def deposit(self, pennies, nickles, dimes, quarters, half_dollars, dollars):
        pennies = int(input("Number of pennies to deposit -> "))
        self._pennies = self._pennies + pennies
        nickles = int(input("Number of nickles to deposit -> "))
        self._nickles = self._nickles + nickles
        dimes = int(input("Number of dimes to deposit -> "))
        self._dimes = self._dimes + dimes
        quarters = int(input("Number of quarters to deposit -> "))
        self._quarters = self._quarters + quarters
        half_dollars = int(input("Number of half-dollars to deposit -> "))
        self._half_dollars = self._half_dollars + half_dollars
        dollars = int(input("Number of dollars to deposit -> "))
        self._dollars = self._dollars + dollars
        print("Your current total: (in this account)")
        return pennies*.01 + nickles*.05 + dimes*.10 + quarters*.25 + half_dollars*.50 + dollars*1.00

    def withdraw(self, pennies, nickles, dimes, quarters, half_dollars, dollars):
        pennies = int(input("Number of pennies to withdraw -> "))
        self._pennies = self._pennies + pennies
        nickles = int(input("Number of nickles to withdraw -> "))
        self._nickles = self._nickles + nickles
        dimes = int(input("Number of dimes to withdraw -> "))
        self._dimes = self._dimes + dimes
        quarters = int(input("Number of quarters to withdraw -> "))
        self._quarters = self._quarters + quarters
        half_dollars = int(input("Number of half-dollars to withdraw -> "))
        self._half_dollars = self._half_dollars + half_dollars
        dollars = int(input("Number of dollars to withdraw -> "))
        self._dollars = self._dollars + dollars
        print("Your current total: (in all withdraw)")
        return pennies*.01 + nickles*.05 + dimes*.10 + quarters*.25 + half_dollars*.50 + dollars*1.00

    def overdrawn(self):
        return self.balance < 0

    @property
    def balance(self):
        return self._pennies*.01 + self._nickles*.05 + self._dimes*.10 + self._quarters*.25 + self._half_dollars*.50 + self._dollars*1.00

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
            user_add = User(name)
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
                print("Welcome, {} -- ID#: {}\n----------------------------\nSelect account: \n1) QUIT\n2) Get Total\n3) {}\n----------------------------".format(User.name,welcome,User.num_of_accounts))
                my_account = Account()
                my_account_nu = Bank._listofaccounts[0]
                print(type(my_account_nu))
                option = int(input("-> "))
                if option == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    #SAVE FUNCTION GOES HERE save_to_disk()
                    os._exit(0)
                elif option == 2:
                    print("Get total: $", ) #all_accounts.balance)
                    raw_input("Press Enter to continue...")
                    x = 1
                else:
                    x = 3
                while x == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Account number: {}\nWhat do you want to do?\n----------------------------\n1) Back...\n2) Withdraw\n3) Deposit\n4) Transfer\n5) Get Balance\n-----------------------------")
                    option = int(input("(1-5) -> "))
                    if option == 5:
                        print("$",my_account.balance)
                        raw_input("Press Enter to continue...")
                    elif option == 4:
                        raw_input("Press Enter to continue...")
                        pass
                    elif option == 3:
                        my_account.deposit(0,0,0,0,0,0)
                        print("$",my_account.balance)
                        raw_input("Press Enter to continue...")
                    elif option == 2:
                        my_account.withdraw(0,0,0,0,0,0)
                        print my_account.balance
                        raw_input("Press Enter to continue...")
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