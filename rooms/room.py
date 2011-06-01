import re

from text_adventure import text

from archmage import resource
from archmage.rooms import room_descriptions

roomsByKey = {}

class Room(resource.Resource):
    
    def getDescription(self):
        return self.description
    
    def handleBeingLookedAt(self):
        self.game.display(self.getDescription())
        return True


def createRooms(game):
    storeByKey([Room(key='archmage_ritual_room')])
    for (key, room) in roomsByKey.items():
        room.setGame(game)
        description = getattr(room_descriptions, key)
        room.setDescription(description)
        
def getRoom(key):
    return roomsByKey[key]


  

def storeByKey(rooms):
    for room in rooms:
        roomsByKey[room.key] = room

