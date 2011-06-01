from text_adventure import inventory

class Resource(object):
    
    nouns = []
    adjectives = []
    
    def __init__(self,
                 key,
                 game=None):
        self.currentOwner = None
        self.inventory = inventory.InventoryManager(inside=True)
        self.key = key
        self.game = game
        self.description = None
    
    def changeOwner(self,
                    newOwner,
                    slotKey='inside'):
        self.currentOwner = newOwner
        self.currentOwner.addToInventory(self,
                                         slotKey)
    
    def addToInventory(self,
                       resource,
                       slotKey):
        self.inventory.add(resource,
                           slotKey)
    
    def setGame(self,
                game):
        self.game = game
    
    def setDescription(self,
                       description):
        self.description = description
    
    def getDescription(self):
        return self.description
    
    def handleBeingLookedAt(self,
                            resources=None):
        print self.getDescription()
        return True
    
    def findResourceFromInventory(self,
                                  resourceName):
        return self.inventory.match(resourceName)
        