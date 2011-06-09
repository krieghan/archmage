from text_adventure import (exception,
                            inventory)

from archmage import resource
from archmage.agents import agent

class Player(agent.Agent):
    nouns = ['me',
             'player']
    name = 'the stalwart apprentice mage'
    
    description = "You can see a bit of your nose, but that's about it."
    
    def findResource(self,
                     resourceName):
        resources = self.findResources(resourceName)
        if len(resources) == 0:
            raise exception.MissingObject('There is no %s here' % resourceName)
        elif len(resources) > 1:
            raise exception.AmbiguousResource(resources)
        else:
            return resources[0]
    
    def findResources(self,
                      resourceName):
        resources = []
        resources.extend(self.currentOwner.findResourceFromInventory(resourceName))
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
        
    
    def displayInventory(self):
        inventory.displayPlayerInventory(self.inventory)
        return True