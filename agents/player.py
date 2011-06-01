from archmage import resource

class Player(resource.Resource):
    nouns = ['me',
             'player']
    
    def findResource(self,
                     resourceName):
        resources = self.findResources(resourceName)
        if len(resources) == 0:
            raise exception.MissingObject('There is no %s here' % resourceName)
        elif len(resources) > 1:
            raise exception.AmbiguousEntity(resources)
        else:
            return resources[0]
    
    def findResources(self,
                      resourceName):
        resources = []
        resources.extend(self.currentOwner.findResourceFromInventory(resourceName))
        resources.extend(self.findResourceFromInventory(resourceName))
        return resources