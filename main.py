import sys

from text_adventure.grammar import interpreter
from text_adventure import (exception,
                            text)

from archmage import (dictionary,
                      command)
from archmage.agents import player
from archmage.rooms import room


class Game(object):
    
    def __init__(self,
                 communicator):
        self.communicator = communicator
    
    def run(self):
        self.player = player.Player(key='Player',
                                    game=self)
        room.createRooms(game=self)
        
        
        parser = interpreter.Interpreter(dictionary=dictionary.dictionary,
                                         thesaurus=dictionary.thesaurus)
        self.player.changeOwner(room.getRoom('archmage_ritual_room'))
        
        while(True):
            commandText = raw_input('>')
            
            try:
                sentence = parser.evaluate(commandText)
                parsedCommand = command.Command(sentence=sentence,
                                                game=game)
                succeeded = parsedCommand.act()
                if not succeeded:
                    raise exception.CouldNotInterpret('I understood "%s", but did not know what to do with it.' % commandText)
            except exception.DenyInput, e:
                print e
                continue
            except exception.PlayerDeath:
                print "You have died"
                sys.exit()
    
    def display(self,
                text):
        self.communicator.output(text)

if __name__ == '__main__':
    communicator = text.StandardCommunicator(wrapLength=80)
    game = Game(communicator=communicator)
    game.run()