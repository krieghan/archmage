from archmage.items import (bookshelf, 
                            dusty_books)
from archmage.rooms import room

itemsByKey = {}

def createItems(game):
    
    #ritual room
    
    storeByKey([bookshelf.Bookshelf(key='archmage_bookshelf',
                                    on=True),
                dusty_books.DustyBooks(key='dusty_books')])
    
    for (key, item) in itemsByKey.items():
        item.setGame(game)
        
def getItem(key):
    return itemsByKey[key]


  

def storeByKey(items):
    for item in items:
        itemsByKey[item.key] = item

def placeItemsInContainers():
    placeItemInRoom('archmage_bookshelf', 'archmage_ritual_room')
    placeItemInContainer('dusty_books', 'archmage_bookshelf', 'on')

def placeItemInRoom(item_key, room_key):
    itemForKey = getItem(item_key)
    roomForKey = room.getRoom(room_key)
    itemForKey.changeOwner(roomForKey)
    
def placeItemInContainer(item_key, container_key, slotKey):
    itemForKey = getItem(item_key)
    containerForKey = getItem(container_key)
    itemForKey.changeOwner(containerForKey,
                           slotKey)
    
    

