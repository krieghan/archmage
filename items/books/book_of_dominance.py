from archmage.items import item

class BookOfDominance(item.Item):
    adjectives = ['black']
    nouns = ['book',
             'book of dominance']
    name = 'book of dominance'
    defaultKey = 'book_of_dominance'
    retrievable = True
    
    
    def __init__(self,
                 key=None,
                 game=None,
                 statIncrease=5):
        self.statIncrease = statIncrease
        item.Item.__init__(self, 
                           key=key, 
                           game=game)
        
    def initState(self):
        self.hasBeenRead = False
    
    def handleBeingRead(self,
                        resources):
        if self.inPlayerInventory():
            if self.hasBeenRead:
                self.game.display('You can gain no further knowledge from this book.')
            else:
                self.game.display('You feel smarter.')
                self.game.player.updateStats('dominance', self.statIncrease)
                self.hasBeenRead = True
        else:
            self.game.display('You do not have it.')
            
    
    