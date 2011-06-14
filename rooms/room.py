import re

from text_adventure import text

from archmage import resource
from archmage.rooms import room_descriptions

roomsByKey = {}
oppositeDirectionReference = {'north' : 'south',
                              'south' : 'north',
                              'east' : 'west',
                              'west' : 'east',
                              'up' : 'down',
                              'down' : 'up'}

class Room(resource.Resource):
    
    name = "room"
    
    def __init__(self,
                 key=None,
                 game=None):
        resource.Resource.__init__(self,
                                   key=key,
                                   game=game,
                                   inside=True)
    
        self.rooms = {}
    
    def getDescription(self):
        return self.description
    
    def handleBeingLookedAt(self):
        self.game.display(self.getDescription())
        return True
    
    def isRoom(self):
        return True
    
    def addRoom(self,
                otherRoom,
                direction):
        self.rooms[direction] = otherRoom
    
    def getRoom(self,
                direction):
        return self.rooms.get(direction)
        


def createRooms(game):
    storeByKey([Room(key='archmage_ritual_room'),
                Room(key='apprentice_ritual_room')])
    for (key, room) in roomsByKey.items():
        room.setGame(game)
        description = getattr(room_descriptions, key)
        room.setDescription(description)
    linkRooms()

def getRoom(key):
    return roomsByKey[key]
    
def linkRooms():
    addTwoWayLink('archmage_ritual_room',
                  'south',
                  'apprentice_ritual_room')

def addTwoWayLink(roomKey,
                  direction,
                  otherRoomKey):
    room = getRoom(roomKey)
    otherRoom = getRoom(otherRoomKey)
    room.addRoom(otherRoom,
                 direction)
    oppositeDirection = oppositeDirectionReference[direction]
    otherRoom.addRoom(room,
                      oppositeDirection)

def storeByKey(rooms):
    for room in rooms:
        roomsByKey[room.key] = room

