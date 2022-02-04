class Item:
    def __init__(self,production,pos):
        self.production = production
        self.pos = pos
    
    @property
    def NextSymbol(self):
        # print(self.production.right_side.symbol)
        if self.pos < len(self.production.right_side):
            return self.production.right_side[self.pos]
        return None
    
    @property
    def IsReduceItem(self):
        return self.pos == len(self.production.right_side)

    def NextItem(self):
        if self.pos < len(self.production.right_side):
            return Item(self.production,self.pos+1) 
    
    def __str__(self):
        return self.production.left_side.symbol + '->' + ''.join([symbol.symbol for symbol in self.production.right_side]) + str(self.pos)
    
    def __eq__(self, other):
        return self.production == other.production and self.pos == other.pos
    
    def __hash__(self):
        return hash((self.production,self.pos))