from archmage import resource

class Agent(resource.Resource):
    def __init__(self,
                 key=None,
                 game=None):
        self.stats = {'will' : 0,
                      'dominate' : 0}
        resource.Resource.__init__(self,
                                   key=key,
                                   game=game,
                                   inside=True,
                                   inventoryExposed=False)
        
        
    def updateStats(self,
                    statName,
                    increase):
        self.stats[statName] += increase

