from archmage import resource

roomsByKey = {}

class Room(resource.Resource):
    def handleBeingLookedAt(self):
        print "You see the room"
        return True


def createRooms():
    roomsByKey = storeByKey([Room(key='archmage_ritual_room')])
    

def storeByKey(rooms):
    for room in rooms:
        roomsByKey[room.key] = room

def getRoom(key):
    return roomsByKey[key]