class Resource(object):
    
    def __init__(self,
                 key):
        self.currentOwner = None
        self.key = key
        self.description = None
    
    def changeOwner(self,
                    newOwner):
        self.currentOwner = newOwner
    
    def setDescription(self,
                       description):
        self.description = description
    
    def getDescription(self):
        return self.description
        
    def handleBeingLookedAt(self):
        print self.getDescription()
        return True