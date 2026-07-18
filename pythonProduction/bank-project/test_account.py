from account import Account 

myAccount = Account(30)

def test_deposit():
    assert(myAccount.deposit()) == 80 
def test_withdraw():
    assert (myAccount.withdraw())==30

