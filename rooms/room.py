import re

from text_adventure import text

from archmage import resource
from archmage.rooms import room_descriptions

roomsByKey = {}

class Room(resource.Resource):
    
    def getDescription(self):
        return self.description
    
    def handleBeingLookedAt(self):
        print self.getDescription()
        return True


def createRooms():
    roomsByKey = storeByKey([Room(key='archmage_ritual_room')])
    for (key, room) in roomsByKey.items():
        description = text.process(getattr(room_descriptions, key))
        room.setDescription(description)
    

def storeByKey(rooms):
    for room in rooms:
        roomsByKey[room.key] = room
    return roomsByKey

def getRoom(key):
    return roomsByKey[key]