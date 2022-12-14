# Class for medcine inventory management

class Medicine:
    def __init__(self, id:str, quantity:float=0): # constructor
        self.id = id
        self.quantity = quantity
    
    def add(self, quantity:int): # add quantity
        self.quantity += quantity
    
    def remove(self, quantity:int): # remove quantity
        self.quantity -= quantity
    
    def getQuantity(self): # get quantity
        return self.quantity
    
    def getId(self): # get id
        return self.id
        
