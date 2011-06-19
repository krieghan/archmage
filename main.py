import sys

from text_adventure.grammar import interpreter
from text_adventure import (exception,
                            text)

from archmage import (dictionary,
                      command)
from archmage.agents import agents
from archmage.rooms import room
from archmage.items import items


class Game(object):
    
    def __init__(self,
                 communicator):
        self.communicator = communicator
    
    def run(self):
        room.createRooms(game=self)
        agents.createAgents(game=self)
        items.createItems(game=self)
        agents.placeAgentsInRooms()
        items.placeItemsInContainers()
                
        self.player = agents.getAgent('player')
        
        parser = interpreter.Interpreter(dictionary=dictionary.dictionary,
                                         thesaurus=dictionary.thesaurus,
                                         singleToPlural=dictionary.singleToPlural,
                                         pluralToSingle=dictionary.pluralToSingle)
        self.addResourcesToParser(parser)
        
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
                self.display(str(e))
                continue
            except exception.PlayerDeath:
                print "You have died"
                sys.exit()
    
    def display(self,
                text):
        self.communicator.output(text)

    def addResourcesToParser(self,
                             parser):
        resources = self.getAllResources()
        nouns = []
        adjectives = []
        for resource in resources:
            nouns += resource.nouns
            adjectives += resource.adjectives
        
        parser.addWords(nouns,
                        'noun')
        parser.addWords(adjectives,
                        'adjective')
        
    def getAllResources(self):
        return room.roomsByKey.values() + agents.agentsByKey.values() + items.itemsByKey.values()

if __name__ == '__main__':
    communicator = text.StandardCommunicator(wrapLength=80)
    game = Game(communicator=communicator)
    game.run()