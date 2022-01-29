class Item:
    def __init__(self,production,pos):
        self.production = production
        self.pos = pos
    
    @property
    def NextSymbol(self):
        if self.pos < len(self.production.right_side):
            return self.production.right_side[self.pos]
        return None
    
    @property
    def IsReduceItem(self):
        return self.pos == len(self.production.right_side)

    def NextItem(self):
        if self.pos < len(self.production.right_side):
            return Item(self.production,self.pos+1) 
        