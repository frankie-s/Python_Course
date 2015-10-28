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

    def __init__(self, owner, acct_name, pennies, nickles, dimes, quarters, half_dollars, dollars, bug_out):
        self._owner = owner
        self._acct_name = acct_name
        self._bug_out = bug_out
        self._pennies = pennies
        self._nickles = nickles
        self._dimes = dimes
        self._quarters = quarters
        self._half_dollars = half_dollars
        self._dollars = dollars
        self._balance = 0

    def deposit(self, pennies, nickles, dimes, quarters, half_dollars, dollars):
        self._pennies = self._pennies + pennies
        self._nickles = self._nickles + nickles
        self._dimes = self._dimes + dimes
        self._quarters = self._quarters + quarters
        self._half_dollars = self._half_dollars + half_dollars
        self._dollars = self._dollars + dollars
        self._add = pennies*.01 + nickles*.05 + dimes*.10 + quarters*.25 + half_dollars*.50 + dollars*1.00
        return self._add

    def withdraw(self, pennies, nickles, dimes, quarters, half_dollars, dollars):
        self._pennies = self._pennies - pennies
        self._nickles = self._nickles - nickles
        self._dimes = self._dimes - dimes
        self._quarters = self._quarters - quarters
        self._half_dollars = self._half_dollars - half_dollars
        self._dollars = self._dollars - dollars
        self._remove =  pennies*.01 + nickles*.05 + dimes*.10 + quarters*.25 + half_dollars*.50 + dollars*1.00
        return self._remove

    @property
    def balance(self):
        return self._pennies*.01 + self._nickles*.05 + self._dimes*.10 + self._quarters*.25 + self._half_dollars*.50 + self._dollars*1.00

    @property
    def owner(self):
        return self._owner


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    my_bank = Bank("First Bank of Matratze") # make the bank bank
    x = 0
    while x == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----------------------------\nWelcome to the {}!\nPlease select an option: \n1) QUIT\n2) Grand Total in Bank\n"
              "3) Largest Account\n4) Make New Account(s)\n5) Edit Account(s)\n----------------------------".format(my_bank._name))
        option = raw_input("-> ")
        if option == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            #SAVE FUNCTION GOES HERE save_to_disk()
            os._exit(0)
        elif option == '2':
            print("Total: ${0:.2f}".format(my_bank.grand_total)) #all_accounts.balance)
            raw_input("\n**Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        elif option == '3':
            if len(my_bank._accounts.items()) == 0:
                print("Create an account first.")
                raw_input("\n**Press Enter to continue...")
            else:
                print("The largest account at this bank is {}.".format(my_bank.largest)) #all_accounts.balance)
                raw_input("\n**Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        elif option == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            next = 'y'
            while next == 'y':
                print("----------------------------\nLets create new accounts!\n")
                owner = raw_input("Account owner -> ")
                name = raw_input("Account nick-name -> ")
                p = int(input("Number of pennies to deposit -> "))
                n = int(input("Number of nickles to deposit -> "))
                di = int(input("Number of dimes to deposit -> "))
                q = int(input("Number of quarters to deposit -> "))
                h = int(input("Number of half-dollars to deposit -> "))
                do = int(input("Number of dollars to deposit -> "))
                bugout = raw_input("Would you like this account to be a bug-out bag?(y,n): ")
                new_account = Account(owner,name,p,n,di,q,h,do,bugout)
                my_bank._accounts.update({name: new_account})
                next = raw_input("Create another account?(y,n): ")
                os.system('cls' if os.name == 'nt' else 'clear')
            print("All account(s): ")
            for key in my_bank._accounts:
                print key
            raw_input("\n**Press Enter to continue...")
        elif option == '5':
            x = 1
            while x == 1:
                if len(my_bank._accounts.items()) == 0:
                    print("Create an account first.")
                    raw_input("\n**Press Enter to continue...")
                    x = 0
                else:
                    print("All account(s): ")
                    for kv in my_bank._accounts.items():
                        print kv[0],'\t',kv[1]
                    print"----------------------------"
                    edit = raw_input("Enter nick-name of account to edit: ")
                    x = 2
                while x == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Account nick-name: {}\nWhat do you want to do?\n----------------------------\n1) Back...\n2) Withdraw"
                          "\n3) Deposit\n4) Transfer\n5) Get Balance\n6) Convert to Bitcoin\n-----------------------------".format(edit))
                    option = raw_input("(1-5) -> ")
                    if option == '6':
                        bcx = my_bank._accounts[edit].balance / 303.76
                        print"Balance in Bitcoin: {0:.2f} BCX".format(bcx)
                        raw_input("\n**Press Enter to continue...")
                    elif option == '5':
                        print("Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == '4':
                        if len(my_bank._accounts.items()) <= 1:
                            print("Create a second account first.")
                            raw_input("\n**Press Enter to continue...")
                        else:
                            acct_to = raw_input("Enter recieving account nick-name: ")
                            if my_bank._accounts[edit].owner != my_bank._accounts[acct_to].owner:
                                print "Error, cant not transfer coins from an account to an account owned by a different person."
                            else:
                                print("-----------------------------\nCurrent Account Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                                print("Recipient Account Balance: ${0:.2f}\n-----------------------------".format(my_bank._accounts[acct_to].balance))
                                p = int(input("Number of pennies to transfer -> "))
                                n = int(input("Number of nickles to transfer -> "))
                                di = int(input("Number of dimes to transfer -> "))
                                q = int(input("Number of quarters to transfer -> "))
                                h = int(input("Number of half-dollars to transfer -> "))
                                do = int(input("Number of dollars to transfer -> "))
                                my_bank._accounts[edit].withdraw(p,n,di,q,h,do)
                                if my_bank._accounts[edit].balance < 0:
                                    print("OVERDRAWN! Action declared invalid and undone! You will now be fined a huge ridiculous fee!")
                                    my_bank._accounts[edit].deposit(p,n,di,q,h,do)
                                    print("Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                                else:
                                    my_bank._accounts[acct_to].deposit(p,n,di,q,h,do)
                                    print("Transfer Compleate.")
                                    print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                            raw_input("\n**Press Enter to continue...")
                    elif option == '3':
                        p = int(input("Number of pennies to deposit -> "))
                        n = int(input("Number of nickles to deposit -> "))
                        di = int(input("Number of dimes to deposit -> "))
                        q = int(input("Number of quarters to deposit -> "))
                        h = int(input("Number of half-dollars to deposit -> "))
                        do = int(input("Number of dollars to deposit -> "))
                        my_bank._accounts[edit].deposit(p,n,di,q,h,do)
                        print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == '2':
                        p = int(input("Number of pennies to withdraw -> "))
                        n = int(input("Number of nickles to withdraw -> "))
                        di = int(input("Number of dimes to withdraw -> "))
                        q = int(input("Number of quarters to withdraw -> "))
                        h = int(input("Number of half-dollars to withdraw -> "))
                        do = int(input("Number of dollars to withdraw -> "))
                        my_bank._accounts[edit].withdraw(p,n,di,q,h,do)
                        if my_bank._accounts[edit].balance < 0:
                            print("OVERDRAWN! Action declared invalid and automatically undone! You will now be fined a huge ridiculous fee!")
                            my_bank._accounts[edit].deposit(p,n,di,q,h,do)
                            print("Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        else:
                            print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                        raw_input("\n**Press Enter to continue...")
                    elif option == '1':
                        x = 0
                    else:
                        print("Error: Enter (1-5): ")
                        raw_input("\n**Press Enter to continue...")
        else:
            print("Error: Enter (1-5): ")
            raw_input("\n**Press Enter to continue...")



if __name__ == '__main__':
    main()