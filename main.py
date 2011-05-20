import sys

from text_adventure.grammar import interpreter

from archmage import dictionary
from archmage.agents import player


class Game(object):
    def run(self):
        self.player = player.Player(name='Player')
        parser = interpreter.Interpreter(dictionary=dictionary.dictionary,
                                         thesaurus=dictionary.thesaurus)
        self.player.changeOwner(room.getRoom('archmage_ritual_room'))
        
        while(True):
            actionText = raw_input('>')
            
            try:
                action = interpreter.evaluate(actionText)
                succeeded = self.actOnAction(action)
                if not succeeded:
                    raise CouldNotInterpret('I understood "%s", but did not know what to do with it.' % actionText)
            except DenyInput, e:
                print e
                continue
            except PlayerDeath:
                print "You have died"
                sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()