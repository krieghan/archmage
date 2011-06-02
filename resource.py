from text_adventure import inventory

class Resource(object):
    
    nouns = []
    adjectives = []
    name = None
    
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
    
    def getName(self):
        return self.name if self.name else self.__class__.name
    
    def setGame(self,
                game):
        self.game = game
    
    def setDescription(self,
                       description):
        self.description = description
    
    def getDescription(self):
        return self.description if self.description else self.__class__.description
    
    def handleBeingLookedAt(self,
                            resources=None):
        print self.getDescription()
        return True
    
    def handleBeingTalkedTo(self,
                            resources=None):
        print "%s has nothing to say to you" % self.getName()
        return True
    
    def findResourceFromInventory(self,
                                  resourceName):
        return self.inventory.match(resourceName)
    
    def getAgents(self):
        from archmage.agents import agent
        allResources = self.inventory.getAll()
        return [resource for resource in allResources if isinstance(resource, agent.Agent)]
        