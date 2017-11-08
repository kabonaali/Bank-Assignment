#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="banking_system")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need


cur = db.cursor()
print('---------------------WELCOME TO SKYNET BANK--------------------')

opn = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM customer")

cur.execute("SELECT * FROM account")
cur.execute("SELECT * FROM bank")
cur.execute("SELECT * FROM loan")
cur.execute("SELECT * FROM savings")
cur.execute("SELECT * FROM checking")




print('--------------------Kampala And Jinja Tellers-------------------------')


for row in cur:
    print(row)

cur.close()
  
opn.execute("SELECT * FROM teller")
for row in opn:
    print(row)

opn.close()

#print all the first cell of all the rows
#for row in cur.fetchall():
  #  print row[0]

#db.close()


class Bank(object):
    def __init__(self,bankId,name,location):
        self.bankId = bankId
        self.name = name
        self.location = location

    def detail(self):
        print("\n+++++ Name:",self.name,"\n+++++ Location:",self.location,"\n+++++ BANK#:",self.bankId,"\n",'*'*50,"\n\n")

    
class Teller(Bank):
    
    def __init__(self,Bank,Id,Name):
        self.Bank = Bank
        self.Id = Id
        self.Name = Name
        
    def detail(self):
        print("\nBANK: ",self.Bank.name,"TELLER ID",self.Id,"TELLER NAME:",self.Name)
        
    def CollectMoney(Customer,amt):
        if(Customer.Bank.bankId == self.Bank.bankId):
            Customer.AccountBal+=amt
            print("Collecting Money")
        else:
            print("Look For Your BANK")

    def OpenAccount():
        print("Opening Account")

    def CloseAcount():
        print("Closing Account")

    def loanRequest():
        print("Load Request")

    def ProvideInfo():
        print("Provide Info")

    def IssueCard():
        print("Issue Card")


## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        
class Customer(Bank):
    AccountBal = 0
    LoanAmt = 0
    def __init__(self,Bank,Id,Name,Address,PhoneNo,AcctNo):
        self.Bank = Bank
        self.Name = Name
        self.Id = Id
        self.Address = Address
        self.PhoneNo = PhoneNo
        self.AcctNo = AcctNo

    def detail(self):
        print("*"*60,
              "\n-------- Customer ID:",self.Id,
              "\n-------- BANK:",self.Bank.name,
              "\n-------- NAME:",self.Name,
              "\n-------- ADDRESS:",self.Address,
              "\n-------- PHONE NO:",self.PhoneNo,
              "\n-------- AC\\NO:",self.AcctNo+"\n"+"*"*60
              )

    def GeneralInquiry(self):
        print("General Inquiry")

    def DepositMoney(self, amt):
        self.AccountBal += amt
        print("deposit of ",amt," UGX\n")
    
    def WithdrawMoney(self, amt):
        if(amt < self.AccountBal):
            self.AccountBal -= amt
            print("withdraw of ",amt," UGX\n")
        else:
            print("-- INSUFFICIENT BALANCE --")

    def OpenAccount(self):
        print("open account")

    def CloseAcount(self):
        print("Close account")

    def ApplyForLoan(self, amt):
        print("apply for loan")

    def RequestCard(self):
        print("request card")

class Account(Customer):
    def __init__(self, Customer,Id,CustomerId):
        self.Customer = Customer
        self.Id = Id
        self.CustomerId = CustomerId

class Loan(Customer):
    def __init__(self, Customer,Id,CustomerId):
        self.Customer = Customer
        self.Id = Id
        self.CustomerId = CustomerId

class Savings(Account):
    def __init__(self,Account,Id,CustomerId):
        self.Account = Account
        self.Id = Id
        self.CustomerId = CustomerId
        print("SAVINGS: ",self.Account.AccountBal)
              
class Checking(Account):
    def __init__(self,Account,Id,CustomerId):
        self.Account = Account
        self.Id = Id
        self.CustomerId = CustomerId
        print("checking... \n BALANCE: ",self.Account.AccountBal)
    
B1 = Bank(4800052,"bank 003","Makerere") ##bank 1
B2 = Bank(4900065,"02 bank ltd","Wandegeya") ## bank 2

#B1.detail() #details of bank 1
#B2.detail() #details of bank 2


# BANK 1 TELLERS
#B1_T1 = Teller(B1,2400622,"Ojambo James")
#B1_T2 = Teller(B1,2303342,"Nakamanya Procy")
#B1_T3 = Teller(B1,2100230,"Nvili Malia,")


#B1_T1.detail()
#B1_T2.detail()
#B1_T3.detail()

# BANK 2 TELLERS
#B2_T1 = Teller(B2,202245,"Bwogi Richard")
#B2_T2 = Teller(B2,233424,"Kato Arushad")
#B2_T3 = Teller(B2,213023,"Olwit Emmanuel")
#
#B2_T1.detail()
#B2_T2.detail()
#B2_T3.detail()


print('-------------------------Welcome  Customers----------------------')
### CUSTOMERS
print("CUSTOMERS of ",B1.name,"\n","_")
CS_B1 = [
    Customer(B1,58220,"Wagalu Sadat","Wandegeya","0772525667","021154785"),
    Customer(B1,58221,"Kasagga Joel","Munyonyo","0778278782","0415432156"),
    Customer(B1,58222,"Lukungu Yassin","Kansanga","0786678096","0411234567"),
    Customer(B1,58223,"Kakole Peter","Kibuye ","0757707933","0311545452"),
    Customer(B1,58224,"Lubwama Peter ","Kawempe","0784537658","0470545454"),
    Customer(B1,58225,"Among Jckline","Kamwokya","0784525606","0411845494"),
    Customer(B1,58226,"Ibra Byeso","Hotel Africana","0754525136","071154645"),
    Customer(B1,58227,"Amanya Zaid","Munyonyo","0754645459","0611545474"),
    Customer(B1,58228,"Ayo Omond","Bwayise","0774535450","0413545658"),
    Customer(B1,58229,"James lwanyi","Nakawa","0752535457","0771548807")
    ]

for sc in CS_B1:    
    print(sc.detail())

print("CUSTOMERS of ",B2.name,"\n","_")
CS_B2 = [
    Customer(B2,58490,"Mulwanyi Josh","Kagongo","0772225607","5211540854597"),
    Customer(B2,58491,"Zawede Ziad","Main street","0778268784","6415438156707"),
    Customer(B2,58492,"Okello Ali","Katale","0756678136","0751239567781"),
    Customer(B2,58493,"Alimu Kasozi","Namanve","0757507966","3311547452748"),
    Customer(B2,58494,"Kifuko Julious ","Katosi","0784507618","1470566454517"),
    Customer(B2,58495,"Ojok Patrick","Mpuwmwile","0784530306","3411847494549"),
    Customer(B2,58496,"Ayebare Ginnah","Jaja","0754991136","2711546457106"),
    Customer(B2,58497,"Roberto Carros","Kitagata","0754545803","3611565474545"),
    Customer(B2,58498,"Joseph Patrick","Gasani","0772581750","0493545058570"),
    Customer(B2,58499,"Agatha Agange","Buwenge","0752001457","5771548803842")
    ]

for sc in CS_B2:    
    print(sc.detail())

#### withdraw and deposit
# ACCOUNT
CB1 = Customer(B1,55848,"Alitwala Rwebecca","Kabalagala","+256755569893","55556601111254")
CB1_A = Account(CB1,25004,1)



