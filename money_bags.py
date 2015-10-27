__author__ = 'frankie'
import os


class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = {}

    @property
    def largest(self):
        inverse = [(value, key) for key, value in self._accounts.items()]
        return max(inverse)[1]

    @property
    def grand_total(self):
        gt = 0
        for key in self._accounts:
            gt += self._accounts[key].balance
        return gt


class Account:
    current_acct_nu = 100

    def __init__(self, name, pennies, nickles, dimes, quarters, half_dollars, dollars, bug_out):
        self._acct_nu = Account.current_acct_nu + 1
        self._name = name
        self._bug_out = bug_out
        self._pennies = pennies
        self._nickles = nickles
        self._dimes = dimes
        self._quarters = quarters
        self._half_dollars = half_dollars
        self._dollars = dollars
        self._balance = 0

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
        self._add = pennies*.01 + nickles*.05 + dimes*.10 + quarters*.25 + half_dollars*.50 + dollars*1.00
        print("Ammount to deposit: ${0:.2f}".format(self._add))
        return self._add


    def withdraw(self, pennies, nickles, dimes, quarters, half_dollars, dollars):
        pennies = int(input("Number of pennies to withdraw -> "))
        self._pennies = self._pennies - pennies
        nickles = int(input("Number of nickles to withdraw -> "))
        self._nickles = self._nickles - nickles
        dimes = int(input("Number of dimes to withdraw -> "))
        self._dimes = self._dimes - dimes
        quarters = int(input("Number of quarters to withdraw -> "))
        self._quarters = self._quarters - quarters
        half_dollars = int(input("Number of half-dollars to withdraw -> "))
        self._half_dollars = self._half_dollars - half_dollars
        dollars = int(input("Number of dollars to withdraw -> "))
        self._dollars = self._dollars - dollars
        self._remove =  pennies*.01 + nickles*.05 + dimes*.10 + quarters*.25 + half_dollars*.50 + dollars*1.00
        print("Ammount to withdraw: ${0:.2f}".format(self._remove))
        return self._remove

    @property
    def balance(self):
        return self._pennies*.01 + self._nickles*.05 + self._dimes*.10 + self._quarters*.25 + self._half_dollars*.50 + self._dollars*1.00

    def transfer(self, acct_to, acct_from, amount):
        pass


class User:
    current_bank_id = 0
    name = "test user"
    num_of_accounts = 0

    def __init__(self, name):
        self._name = User.name
        User.name = name
        self._bank_id = User.current_bank_id
        User.current_bank_id = User.current_bank_id + 1
        self._num_of_accounts = User.num_of_accounts
        User._num_of_accounts = User.num_of_accounts


def interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    my_bank = Bank("First Bank of Matratze") # make the bank bank
    x = 0
    while x == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----------------------------\nWelcome to the {}!\nPlease select an option: \n1) QUIT\n2) Grand Total in Bank\n"
              "3) Largest Account\n4) Make New Account(s)\n5) Edit Account(s)\n----------------------------".format(my_bank._name))
        option = int(input("-> "))
        if option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            #SAVE FUNCTION GOES HERE save_to_disk()
            os._exit(0)
        elif option == 2:
            print("Total: ${0:.2f}".format(my_bank.grand_total)) #all_accounts.balance)
            raw_input("\n**Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        elif option == 3:
            if len(my_bank._accounts.items()) == 0:
                print("Create an account first.")
                raw_input("\n**Press Enter to continue...")
            else:
                print("The largest account at this bank is {}.".format(my_bank.largest)) #all_accounts.balance)
                raw_input("\n**Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        elif option == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            next = 'y'
            while next == 'y':
                print("----------------------------\nLets create new accounts!\n")
                name = raw_input("Account name -> ")
                pennies = int(input("Number of pennies to deposit -> "))
                nickles = int(input("Number of nickles to deposit -> "))
                dimes = int(input("Number of dimes to deposit -> "))
                quarters = int(input("Number of quarters to deposit -> "))
                half_dollars = int(input("Number of half-dollars to deposit -> "))
                dollars = int(input("Number of dollars to deposit -> "))
                bug_out = raw_input("Would you like this account to be a bug-out bag?(y,n): ")
                new_account = Account(name,pennies,nickles,dimes,quarters,half_dollars,dollars,bug_out)
                my_bank._accounts.update({name: new_account})
                next = raw_input("Create another account?(y,n): ")
                os.system('cls' if os.name == 'nt' else 'clear')
            print("Your account(s): ")
            for key in my_bank._accounts:
                print key
            raw_input("\n**Press Enter to continue...")
        else:
            x = 1
            while x == 1:
                if len(my_bank._accounts.items()) == 0:
                    print("Create an account first.")
                    raw_input("\n**Press Enter to continue...")
                    x = 0
                else:
                    print("All account(s): ")
                    for keys, values in my_bank._accounts.items():
                        print(keys,':',values)
                    edit = raw_input("Enter name of account to edit: ")
                    x = 2
                while x == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Account name: {}\nWhat do you want to do?\n----------------------------\n1) Back...\n2) Withdraw"
                          "\n3) Deposit\n4) Transfer\n5) Get Balance\n-----------------------------".format(my_bank._accounts[edit]))
                    option = int(input("(1-5) -> "))
                    if option == 5:
                        print("${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == 4:
                        print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == 3:
                        my_bank._accounts[edit].deposit(0,0,0,0,0,0)
                        print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == 2:
                        my_bank._accounts[edit].withdraw(0,0,0,0,0,0)
                        if my_bank._accounts[edit].balance < 0:
                            print("OVERDRAWN! Action declared invalid! You will now be fined a huge ridiculous fee!")
                        else:
                            print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == 1:
                        x = 0
                    else:
                        print("Error: Enter (1-5): ")
                        raw_input("\n**Press Enter to continue...")


if __name__ == '__main__':
    interface()