import logging 

logging.basicConfig(level=logging.INFO)
class Account:

    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self) -> int:
        logging.info("Adding to balance")
        self.balance = self.balance + 50
        return self.balance

    def withdraw(self) -> int:
        if self.balance  >= 50:
            self.balance = self.balance -50 
            logging.info("Money withdrawn")
            return self.balance
        else:
            raise ValueError("Insufficient balance")
            logging.warning("insufficient balance")
            return self.balance