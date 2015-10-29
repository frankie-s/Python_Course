import os
import csv
__author__ = 'frankie'


class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = {}

    def save(self):
        writer = csv.writer(open('transaction_log.csv', 'ab'))
        for k in self._accounts.items():
                writer.writerow([k[0], k[1].owner, k[1].acct_name, k[1].p, k[1].n, k[1].di, k[1].q, k[1].h, k[1].do, k[1].bug])

    @property
    def largest(self):
        total_lst = []
        name_lst = []
        for key, val in self._accounts.items():
            print("Account Name: {1}  \t  Balance: {0:>5.2f} USD".format(self._accounts[key].balance, self._accounts[key].acct_name))
            total_lst.append(self._accounts[key].balance)
            name_lst.append(self._accounts[key].acct_name)
        return name_lst[total_lst.index(max(total_lst))]

    @property
    def grand_total(self):
        gt = 0
        for key in self._accounts:
            gt += self._accounts[key].balance
        return gt


class Account:
    current_acct_nu = 100

    def __init__(self, owner, acct_name, p, n, di, q, h, do, bug_out):
        self._owner = owner
        self._acct_name = acct_name
        self._bug_out = bug_out
        self._p = p
        self._n = n
        self._di = di
        self._q = q
        self._h = h
        self._do = do
        self._balance = 0

    def deposit(self, p, n, di, q, h, do):
        self._p += p
        self._n += n
        self._di += di
        self._q += q
        self._h += h
        self._do += do
        self._add = p * .01 + n * .05 + di * .10 + q * .25 + h * .50 + do * 1.00
        return self._add

    def withdraw(self, p, n, di, q, h, do):
        self._p -= p
        self._n -= n
        self._di -= di
        self._q -= q
        self._h -= h
        self._do -= do
        self._remove =  p * .01 + n * .05 + di * .10 + q * .25 + h * .50 + do * 1.00
        return self._remove

    @property
    def owner(self):
        return self._owner

    @property
    def acct_name(self):
        return self._acct_name

    @property
    def bug(self):
        return self._bug_out

    @property
    def p(self):
        return self._p

    @property
    def n(self):
        return self._n

    @property
    def di(self):
        return self._di

    @property
    def q(self):
        return self._q

    @property
    def h(self):
        return self._h

    @property
    def do(self):
        return self._do

    @property
    def balance(self):
        return (self._p * .01) + (self._n * .05) + (self._di * .10) + (self._q * .25) + (self._h * .50) + (self._do * 1.00)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    my_bank = Bank("First Bank of Matratze")  # make the bank bank
    exists = os.path.isfile('transaction_log.csv')  # check if file exists
    if exists == True:
            load = raw_input("Welcome Back! Do you want to load previously saved data?:(y,n) ")
            if load == "y":
                reader = csv.reader(open("transaction_log.csv"))
                for row in reader:
                    new_account = Account(row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), row[9])
                    my_bank._accounts.update({row[0]: new_account})
                print("Data Loaded.")
                raw_input("**Press Enter to continue...")
    x = 0
    while x == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----------------------------\nWelcome to the {}!\nPlease select an option: "
              "\n1) SAVE & QUIT\n2) Grand Total in Bank\n3) Largest Account\n4) Make New Account(s)"
              "\n5) Edit Account(s)\n----------------------------".format(my_bank._name))
        option = raw_input("-> ")
        if option == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            my_bank.save()
            os._exit(0)
        elif option == '2':
            print("Total: ${0:.2f}".format(my_bank.grand_total))  # all_accounts.balance)
            raw_input("\n**Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        elif option == '3':
            if len(my_bank._accounts.items()) == 0:
                print("Create an account first.")
                raw_input("\n**Press Enter to continue...")
            else:
                print("The largest account at this bank is {}.".format(my_bank.largest))  # all_accounts.balance)
                raw_input("\n**Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        elif option == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            do_next = 'y'
            while do_next == 'y':
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
                new_account = Account(owner, name, p, n, di, q, h, do, bugout)
                my_bank._accounts.update({name: new_account})
                do_next = raw_input("Create another account?(y,n): ")
                os.system('cls' if os.name == 'nt' else 'clear')
            print("All account(s): ")
            for k in my_bank._accounts.items():
                print('Nick-Name: {0}\tOwner: {1}\tBugout?: {2:>5}'.format(k[0], k[1].owner, k[1].bug))
            print"----------------------------"
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
                    for k in my_bank._accounts.items():
                        print('Nick-Name: {0}\tOwner: {1}\tBugout?: {2}'.format(k[0], k[1].owner, k[1].bug))
                    edit = raw_input("\nEnter nick-name of account to edit: ")
                    x = 2
                    while x == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Account nick-name: {}\nWhat do you want to do?\n----------------------------\n1) Back...\n2) Withdraw"
                              "\n3) Deposit\n4) Transfer\n5) Get Balance\n6) Exchange Rates\n-----------------------------".format(edit))
                        option = raw_input("(1-5) -> ")
                        if option == '6':
                            bcx = my_bank._accounts[edit].balance / 303.76
                            euro = my_bank._accounts[edit].balance * 0.90
                            yen = my_bank._accounts[edit].balance * 120.57
                            print(u"Balance in Bitcoin: {0:.4f} \u0243".format(bcx))
                            print("Balance in Euro: {0:.2f} \xe2\x82\xac".format(euro))
                            print(u"Balance in Yen: {0:.2f} \u00A5".format(yen))
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
                                    my_bank._accounts[edit].withdraw(p, n, di, q, h, do)
                                    if my_bank._accounts[edit].p < 0:
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Error: Too few pennies to transfer")
                                    elif my_bank._accounts[edit].n < 0:
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Error: Too few nickles to transfer")
                                    elif my_bank._accounts[edit].di < 0:
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Error: Too few dimes to transfer")
                                    elif my_bank._accounts[edit].q < 0:
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Error: Too few quarters to transfer")
                                    elif my_bank._accounts[edit].h < 0:
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Error: Too few half-dollars to transfer")
                                    elif my_bank._accounts[edit].do < 0:
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Error: Too few dollars to transfer")
                                    elif my_bank._accounts[edit].balance < 0:
                                        print("OVERDRAWN! Action declared invalid and undone! You will now be fined a huge ridiculous fee!")
                                        my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                        print("Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                                    else:
                                        my_bank._accounts[acct_to].deposit(p, n, di, q, h, do)
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
                            my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                            print("New Balance: ${0:.2f}".format(my_bank._accounts[edit].balance))
                            raw_input("\n**Press Enter to continue...")
                        elif option == '2':
                            print("Balance: ${0:.2f}\n-----------------------------".format(my_bank._accounts[edit].balance))
                            p = int(input("Number of pennies to withdraw -> "))
                            n = int(input("Number of nickles to withdraw -> "))
                            di = int(input("Number of dimes to withdraw -> "))
                            q = int(input("Number of quarters to withdraw -> "))
                            h = int(input("Number of half-dollars to withdraw -> "))
                            do = int(input("Number of dollars to withdraw -> "))
                            my_bank._accounts[edit].withdraw(p, n, di, q, h, do)
                            if my_bank._accounts[edit].p < 0:
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                print("Error: Too few pennies to withdraw")
                            elif my_bank._accounts[edit].n < 0:
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                print("Error: Too few nickles to withdraw")
                            elif my_bank._accounts[edit].di < 0:
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                print("Error: Too few dimes to withdraw")
                            elif my_bank._accounts[edit].q < 0:
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                print("Error: Too few quarters to withdraw")
                            elif my_bank._accounts[edit].h < 0:
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                print("Error: Too few half-dollars to withdraw")
                            elif my_bank._accounts[edit].do < 0:
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
                                print("Error: Too few dollars to withdraw")
                            elif my_bank._accounts[edit].balance < 0:
                                print("OVERDRAWN! Action declared invalid and automatically undone! You will now be fined a huge ridiculous fee!")
                                my_bank._accounts[edit].deposit(p, n, di, q, h, do)
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