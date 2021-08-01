
class Banker():

    def __init__(self,shelved=0,balance=0):
        self.balance=balance
        self.shelved=shelved

    def shelf(self,amount_of_points:int):
        self.shelved=amount_of_points
        pass

    def bank(self):
        self.balance+=self.shelved
        self.shelved=0
        pass

    def clear_shelf(self):
        self.shelved=0
        pass