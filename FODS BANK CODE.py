import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(sdiw):
        sdiw.accNo= int(input("Enter the account no : "))
        sdiw.name = input("Enter the account holder name : ")
        sdiw.type = input("Ente the type of account [C/S] : ")
        sdiw.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")
    
    def showAccount(sdiw):

        print("Account snumber : ",sdiw.accNo)
        print("Account Holder Name : ", sdiw.name)
        print("Type of Account",sdiw.type)
        print("Balance : ",sdiw.deposit)
 
    
    def modifyAccount(sdiw):
      a=int(input("Enter the admin password"))
      if a== 8899:
        print("Account snumber : ",sdiw.accNo)
        sdiw.name = input("Modify Account Holder Name :")
        sdiw.type = input("Modify type of Account :")
        sdiw.deposit = int(input("Modify Balance :"))
        
    def depositAmount(sdiw,amount):
        sdiw.deposit += amount
    
    def withdrawAmount(sdiw,amount):
        sdiw.deposit -= amount
    
    def report(sdiw):
        print(sdiw.accNo, " ",sdiw.name ," ",sdiw.type," ", sdiw.deposit)
    
    def getAccountNo(sdiw):
        return sdiw.accNo
    def getAcccountHolderName(sdiw):
        return sdiw.name
    def getAccountType(sdiw):
        return sdiw.type
    def getDeposit(sdiw):
        return sdiw.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\tLaxmiBank")
    print("\t\t\t\tDiwon Sigdel")
    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsdiwontxt(account)

def displayAll():
 a=int(input("Enter the admin password"))
 if a== 8899:
    diwontxt = pathlib.Path("C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt")
    if diwontxt.exists ():
        indiwontxt = open('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','rb')
        mylist = pickle.load(indiwontxt)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        indiwontxt.close()
    else :
        print("No records to display")
 else:
     print("Contact the Bank Admin")
        

def displaySp(snum): 
    diwontxt = pathlib.Path("C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt")
    if diwontxt.exists ():
        indiwontxt = open('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','rb')
        mylist = pickle.load(indiwontxt)
        indiwontxt.close()
        found = False
        for item in mylist :
            if item.accNo == snum :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this snumber")

def depositAndWithdraw(snum1,snum2): 
    diwontxt = pathlib.Path("C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt")
    if diwontxt.exists ():
        indiwontxt = open('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','rb')
        mylist = pickle.load(indiwontxt)
        indiwontxt.close()
        os.remove('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
        for item in mylist :
            if item.accNo == snum1 :
                if snum2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif snum2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")
                
    else :
        print("No records to Search")
    outdiwontxt = open('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','wb')
    pickle.dump(mylist, outdiwontxt)
    outdiwontxt.close()
    os.rename('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt', 'C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')

    
def deleteAccount(snum):
 a=int(input("Enter the admin password"))
 if a== 8899:
    diwontxt = pathlib.Path("C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt")
    if diwontxt.exists ():
        indiwontxt = open('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','rb')
        oldlist = pickle.load(indiwontxt)
        indiwontxt.close()
        newlist = []
        for item in oldlist :
            if item.accNo != snum :
                newlist.append(item)
        os.remove('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
        outdiwontxt = open('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','wb')
        pickle.dump(newlist, outdiwontxt)
        outdiwontxt.close()
        os.rename('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt', 'C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
 else:
     print("contact bank admin")
def modifyAccount(snum):
    diwontxt = pathlib.Path("C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt")
    if diwontxt.exists ():
        indiwontxt = open('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','rb')
        oldlist = pickle.load(indiwontxt)
        indiwontxt.close()
        os.remove('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
        for item in oldlist :
            if item.accNo == snum :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        
        outdiwontxt = open('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','wb')
        pickle.dump(oldlist, outdiwontxt)
        outdiwontxt.close()
        os.rename('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt', 'C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
   

def writeAccountsdiwontxt(account) : 
    
    diwontxt = pathlib.Path("C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt")
    if diwontxt.exists ():
        indiwontxt = open('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','rb')
        oldlist = pickle.load(indiwontxt)
        oldlist.append(account)
        indiwontxt.close()
        os.remove('C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
    else :
        oldlist = [account]
    outdiwontxt = open('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt','wb')
    pickle.dump(oldlist, outdiwontxt)
    outdiwontxt.close()
    os.rename('newC://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt', 'C://Users//sigde//OneDrive//Desktop//FODS BANK MANAGEMENT//accounts.txt')
    
        

ch=''
snum=0
intro()

while ch != 8:

    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT(*)")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST(*)")
    print("\t6. CLOSE AN ACCOUNT(*)")
    print("\t7. MODIFY AN ACCOUNT(*)")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    print("\tMenus with (*) requires admin authentication")
    ch = input()

    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        snum = int(input("\tEnter The account No. : "))
        depositAndWithdraw(snum, 1)
    elif ch == '3':
        snum = int(input("\tEnter The account No. : "))
        depositAndWithdraw(snum, 2)
    elif ch == '4':
        snum = int(input("\tEnter The account No. : "))
        displaySp(snum)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        snum =int(input("\tEnter The account No. : "))
        deleteAccount(snum)
    elif ch == '7':
        snum = int(input("\tEnter The account No. : "))
        modifyAccount(snum)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    


    
    
    
    
    
    
    
    
    
    
