from archmage import resource
from archmage.agents import agent
from archmage.items import items
from archmage.items.books import book_of_dominance

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
    
    givenMission = False
    
    def handleBeingTalkedTo(self,
                            resources):
        toSay =\
            '''My friend, you have been my servant for many years, and I have not forgotten why you first came 
               to me as a child.  Today, your years as my servant come to an end, and I will begin training you to be
               a mage.  First, though, I have a mission for you.'''
        self.game.display(toSay)
        return True
            
    def handleBeingAsked(self,
                         resources):
        subject = resources['about']
        
        if subject == 'mission':
            toSay = ''
            mission =\
                '''"You must go into the cave near the waterfall west of town.  Inside the cave, you
                    will find something of great value.  Retrieve it for me and I will begin your tutelage." '''
            toSay += mission
            if not self.__class__.givenMission:
                takeABook =\
                    '''The old man strokes his gray beard for a moment.  "Oh, I almost forgot.  You will need
                       a certain something to carry out your mission."  He waves his hands toward the bookshelf
                       in the corner of the room.  "Choose a single book from my bookshelf.  Read it before your journey.
                       When you are finished reading it, place it on the bookshelf in your library." '''
                toSay += takeABook
                self.addBooksToBookshelf()
                self.__class__.givenMission = True
            self.game.display(toSay)
        elif subject == 'book':
            book =\
                '''Choose a book, young man.  Reading it will bestow upon you a measure of power.  The nature
                   of the power that you receive depends upon you, and which book you choose.  Choose wisely.'''
            self.game.display(book)
        elif subject == 'cave':
            cave =\
                '''I really cannot say what you might encounter inside the cave.  All I can tell you is that you
                   are ready to face it - or rather, that you will be when you have finished reading your first
                   book.'''
        else:
            self.game.display('''That does not pertain to your mission, my friend, and time is short.''')
        return True
    
    def addBooksToBookshelf(self):
        bookshelf = items.getItem('archmage_bookshelf')
        book_of_dominance.BookOfDominance(game=self.game).changeOwner(bookshelf,
                                                                      slotKey='on')
