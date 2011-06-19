from text_adventure import (exception,
                            inventory)

from archmage import resource
from archmage.agents import agent

class Player(agent.Agent):
    nouns = ['me',
             'player']
    name = 'the stalwart apprentice mage'
    
    description = "You can see a bit of your nose, but that's about it."
    
    
    def initState(self):
        stats = {'dominance' : 0,
                 'will' : 0}
        self.stats.update(stats)
    
    def changeOwner(self,
                    newOwner,
                    slotKey='inside'):
        agent.Agent.changeOwner(self,
                                newOwner,
                                slotKey)
        self.announceRoom()
    
    def findResource(self,
                     resourceName,
                     source='all'):
        resources = self.findResources(resourceName,
                                       source)
        if len(resources) == 0:
            raise exception.MissingObject('There is no %s here' % resourceName)
        elif len(resources) > 1:
            raise exception.AmbiguousResource(resources)
        else:
            return resources[0]
    
    def findResources(self,
                      resourceName,
                      source='all'):
        resources = []
        if source == 'all':
            resources.extend(self.currentOwner.findResourceFromInventory(resourceName))
            resources.extend(self.findResourceFromInventory(resourceName))
        elif source == 'room':
            resources.extend(self.currentOwner.findResourceFromInventory(resourceName))
        elif source == 'self':
            resources.extend(self.findResourceFromInventory(resourceName))

        return resources
    
    def findAgent(self,
                  agentKey=None):
        agents = self.currentOwner.getAgents()
        eligibleAgents = [agent for agent in agents if agent != self]
        if len(eligibleAgents) == 0:
            raise exception.NotPresent()
        elif len(eligibleAgents) > 1:
            raise exception.AmbiguousResource(eligibleAgents)
        else:
            return eligibleAgents[0]
        
    def announceRoom(self):
        self.game.display(self.currentOwner.getName())
        self.game.display(self.currentOwner.getDescription())
    
    def displayInventory(self):
        inventory.displayPlayerInventory(self.inventory)
        return True