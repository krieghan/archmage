class Resource(object):
    
    def __init__(self,
                 key,
                 game=None):
        self.currentOwner = None
        self.key = key
        self.game = game
        self.description = None
    
    def changeOwner(self,
                    newOwner):
        self.currentOwner = newOwner
        
    def setGame(self,
                game):
        self.game = game
    
    def setDescription(self,
                       description):
        self.description = description
    
    def getDescription(self):
        return self.description
        
    def handleBeingLookedAt(self):
        print self.getDescription()
        return True