from archmage import resource
from archmage.agents import agent

class Baldevarth(agent.Agent):
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
            '''My friend, you have been my servant for many years, and I have not forgotten why you first came 
               to me as a child.  Today, your years as my servant come to an end, and I will begin training you to be
               a mage.  First, though, I have a mission for you.'''
        self.game.display(toSay)
        return True
            
    def handleBeingAsked(self,
                         subject):
            
        mission =\
            '''"You must go into the cave near the waterfall west of town.  Inside the cave, you
                will find something of great value.  Retrieve it for me and I will begin your tutelage."'''
                
        takeABook =\
                '''The old man strokes his gray beard for a moment.  "Oh, I almost forgot.  You will need
                   a certain something to carry out your mission."  He waves his hands toward the bookshelf
                   in the corner of the room.  "Choose a single book from my bookshelf.  Read it before your journey.
                   When you are finished reading it, place it on the bookshelf in your library."'''
        self.game.display('%s %s' % (mission, takeABook))
        return True