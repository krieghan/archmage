from archmage import resource

class Agent(resource.Resource):
    def __init__(self,
                 key=None,
                 game=None):
        resource.Resource.__init__(self,
                                   key=key,
                                   game=game,
                                   inside=True,
                                   inventoryExposed=False)

