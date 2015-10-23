__author__ = 'frankie'
import os


class User:
    current_bank_id = 0
    accounts = []

    def __init__(self,bank_id, name, accounts):
        self._name = name
        self._accounts = []
        User._accounts = User.accounts
        User.current_bank_id = User.current_bank_id + 1
        self._bank_id = User.current_bank_id


class Account:
    current_acct_nu = 100

    def __init__(self, acct_nu, name, balance, pennies, nickles, dimes, quarters):
        self._acct_nu = Account.current_acct_nu + 1
        self._name = name
        self._balance = balance
        self.pennies = pennies
        self.nickles = nickles
        self.dimes = dimes
        self.quarters = quarters

    def __str__(self):
        #return str(self, name)
        pass

    def deposit(self, acct_nu):
        pennies = int(input("Number of pennies to deposit -> "))
        nickles = int(input("Number of nickles to deposit -> "))
        dimes = int(input("Number of dimes to deposit -> "))
        quarters = int(input("Number of quarters to deposit -> "))
        print("Your current total: (in all accounts)")
        return pennies, nickles, dimes, quarters

    def withdraw(self, acct_nu, amount):
        pass

    def get_balance(self, acct_nu):
        pass

    def transfer(self, acct_to, acct_from, amount):
        pass


def interface():
    # Who is using the bank?
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome = int(input("Welcome to the First Bank of Matratze!\nEnter your user ID or enter '0' to open a new account: "))
    x = 0
    while x == 0:
        if welcome == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--------------------\nWelcome new user. Your ID is XXX\nPlease enter some basic info: \n--------------------")
            name = raw_input("Your Name -> ")
            num_accounts = int(input("How many accounts do you wish to open? "))
            print("Your account number(s) are: ")
            bug_out = raw_input("Would you like one to be a bug-out bag? (y,n): ")
            welcome = 1
            #Account.deposit()
        else:
            # For selected user, show "accounts (bags)"
            x = 1
        while x == 1:
            x = 2
            if x == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Welcome, {}.\n--------------------\nSelect account: \n1) QUIT\n2) Create new account\n3) {}\n--------------------\n".format(User.current_bank_id,User.accounts))
                account = int(input("(1-X) -> "))
                if account == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    #SAVE FUNCTION GOES HERE save_to_disk()
                    os._exit(0)
                elif account == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    #CREATE NEW ACCOUNT
                else:
                    x = 3
                while x == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("What do you want to do?\n--------------------\n1) Back...\n2) Withdraw\n3) Deposit\n4) Transfer\n5) Get Balance\n---------------------")
                    option = int(input("(1-5) -> "))
                    if option == 5:
                        pass
                    elif option == 4:
                        pass
                    elif option == 3:
                        pass
                    elif option == 2:
                        pass
                    else:
                        x = 1


# Save to disk
def save_to_disk():
    pass

# Convert currency types


if __name__ == '__main__':
    interface()