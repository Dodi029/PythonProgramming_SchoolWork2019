import bank
import random
saving_accounts=[]
check_accounts=[]
for i in range(5):
    var=bank.SavingsAccount('sav'+str(i),i,(i+1)+100000,i+1*6.3)
    saving_accounts.append(var)
    var=bank.CheckingAccount('che'+str(i),i+5,(i+1)*10000)
    check_accounts.append(var)

sum_sav=0
sum_che=0
for i in range(5):
    sum_sav+=saving_accounts[i].deposit(random.randint(10000,1000000))
    sum_che+=check_accounts[i].deposit(random.randint(10000,1000000))

print("Saving Account Total:",sum_sav)
print("Checking Account Total:",sum_che)
accounts=check_accounts+saving_accounts
accounts=sorted(accounts,key=lambda accounts:accounts._BankAccount__balance)
print("최고액 보유자:",accounts[len(accounts)-1].name,"잔액 :",accounts[len(accounts)-1]._BankAccount__balance)