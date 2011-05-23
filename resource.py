class Resource(object):
    
    def __init__(self,
                 key):
        self.currentOwner = None
        self.key = key
    
    def changeOwner(self,
                    newOwner):
        self.currentOwner = newOwner
        
    def handleBeingLookedAt(self):
        return "It defies description"