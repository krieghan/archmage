from text_adventure import (inventory,
                            exception)

class Resource(object):
    
    nouns = []
    adjectives = []
    name = None
    retrievable = False
    
    def __init__(self,
                 key=None,
                 game=None,
                 inside=False,
                 on=False,
                 under=False,
                 inventoryExposed=True):
        if key is None:
            key = self.__class__.defaultKey
        self.currentOwner = None
        self.inventory = inventory.InventoryManager(inside=inside,
                                                    on=on,
                                                    under=under,
                                                    exposed=inventoryExposed)
        self.key = key
        self.game = game
        self.description = None
        self.initState()
    
    def initState(self):
        pass
    
    def isRoom(self):
        return False
    
    def changeOwner(self,
                    newOwner,
                    slotKey='inside'):
        if newOwner.inventory.slots.get(slotKey) is None:
            raise exception.CannotPerformAction("You cannot put the %s %s the %s" % (self.getName(),
                                                                                     slotKey,
                                                                                     newOwner.getName()))
        if self.currentOwner:
            self.currentOwner.removeFromInventory(self)
        self.currentOwner = newOwner
        self.currentOwner.addToInventory(self,
                                         slotKey)
    
    def addToInventory(self,
                       resource,
                       slotKey):
        self.inventory.add(resource,
                           slotKey)
        
    def removeFromInventory(self,
                            resource,
                            slotKey=None):
        self.inventory.remove(resource,
                              slotKey)
    
    def getName(self):
        return getattr(self, 'name', self.__class__.name)
    
    def inPlayerInventory(self):
        return self.currentOwner == self.game.player
    
    def isRetrievable(self):
        return getattr(self, 'retrievable', self.__class__.retrievable)
    
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
        self.game.display(self.getDescription())
        return True
    
    def handleBeingTalkedTo(self,
                            resources=None):
        self.game.display("%s has nothing to say to you" % self.getName())
        return True
    
    def handleBeingAsked(self,
                         resources=None):
        self.game.display("%s knows nothing about that subject" % self.getName())
        return True
    
    def handleBeingRetrieved(self,
                             resources=None):
        if self.isRetrievable():
            self.changeOwner(self.game.player)
            self.game.display("You pick up the %s" % self.getName())
        else:
            self.game.display("For the life of you, you cannot figure out why you would want %s" % self.getName())
        return True
    
    def handleBeingRead(self,
                        resources=None):
        self.game.display("You'd like to be able to read the %s, but there are no words on it" % self.getName())
        
    def handleBeingPlaced(self,
                          resources=None):
        if self.isRetrievable():
            if resources.get('in'):
                newOwner = resources['in']
                slotKey = 'inside'
            elif resources.get('on'):
                newOwner = resources['on']
                slotKey = 'on'
            elif resources.get('under'):
                newOwner = resources['under']
                slotKey = 'under'
            else:
                newOwner = self.game.player.currentOwner
                slotKey = 'inside'
            
            self.changeOwner(newOwner, 
                             slotKey)
            
            if newOwner.isRoom():
                preposition = 'on'
                noun = 'ground'
            else:
                preposition = slotKey
                noun = newOwner.getName()
            
            self.game.display("You place the %s %s the %s" % (self.getName(),
                                                              preposition,
                                                              noun))
            
        else:
            self.game.display("The %s is too heavy to pick up" % self.getName())
    
    def findResourceFromInventory(self,
                                  resourceName):
        return self.inventory.match(resourceName)
    
    def getAgents(self):
        from archmage.agents import agent
        allResources = self.inventory.getAll()
        return [resource for resource in allResources if isinstance(resource, agent.Agent)]
    
        