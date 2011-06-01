from archmage import resource

class Baldevarth(resource.Resource):
    nouns = ['archmage',
             'baldevarth',
             'wizard',
             'master',
             'man']
    adjectives = ['old',
                  'wise']
    name = 'Baldevarth'
    
    description = 'It is Baldevarth, the archmage.'
    
    def handleBeingTalkedTo(self,
                            resources):
        toSay =\
            '''The time has come, my young friend, for you to embark upon your first journey
               as an apprentice mage.  Venture into the cave near the waterfall.  Bring back
               adequate proof that you are ready to be my pupil.'''