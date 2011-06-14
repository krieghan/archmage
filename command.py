from archmage.rooms import room
from text_adventure import exception

class Command(object):
    def __init__(self,
                 sentence,
                 game):
        self.sentence = sentence
        self.game = game
    
    def findResources(self,
                      source='all'):
        resources = {}
        for prepositionalPhrase in self.sentence.prepositionalPhrases.values():
            resourceName = prepositionalPhrase.object
            resource = self.game.player.findResource(resourceName,
                                                     source=source)
            resources[prepositionalPhrase.preposition] = resource
            
        if self.sentence.object:
            resource = self.game.player.findResource(self.sentence.object,
                                                     source=source)
            resources[None] = resource
            
        return resources
            
    def act(self):
        
        if self.isTravelling():
            direction = self.sentence.object
            currentRoom = self.game.player.currentOwner
            newRoom = currentRoom.getRoom(direction)
            if not isinstance(newRoom, room.Room):
                if newRoom is None:
                    response = 'You cannot go that way'
                else:
                    response = newRoom
                    
                raise exception.CannotGoThatWay(response)
            
            self.game.player.changeOwner(newRoom)
            return True
        
        if self.isCheckingInventory():
            return self.game.player.displayInventory()
        
        if self.isLookingAtRoom():
            return self.game.player.currentOwner.handleBeingLookedAt()
        if self.isLookingAtResource():
            resources = self.findResources()
            
            if self.sentence.object:
                return resources[None].handleBeingLookedAt(resources)
            
            mainPhrase = self.sentence.prepositionalPhrases['main']
            mainPreposition = mainPhrase.preposition
            if mainPreposition == 'at':
                return resources['at'].handleBeingLookedAt(resources)
            
        if self.isTalking():
            resources = self.findResources()
            
            toPhrase = self.sentence.prepositionalPhrases['to']
            if toPhrase is not None:
                return resources['to'].handleBeingTalkedTo(resources)
            
        if self.isAsking():
            resources = {}
            if self.sentence.object:
                resources[None] = self.game.player.findResource(self.sentence.object)
            else:
                resources[None] = self.game.player.findAgent()
            
            for prepositionalPhrase in self.sentence.prepositionalPhrases.values():
                preposition = prepositionalPhrase.preposition
                object = prepositionalPhrase.object
                resources[preposition] = object
                
            return resources[None].handleBeingAsked(resources)
        
        if self.isGetting():
            resources = self.findResources(source='room')
            return resources[None].handleBeingRetrieved(resources)
        
        if self.isReading():
            resources = self.findResources()
            resources[None].handleBeingRead(resources)
            return True
        
        if self.isPlacing():
            resources = self.findResources()
            resources[None].handleBeingPlaced(resources)
            return True
                
    
    def isTravelling(self):
        if self.sentence.verb == 'go':
            return True
        else:
            return False
        
    def isLookingAtRoom(self):
        atPhrase = self.sentence.prepositionalPhrases.get('at')
        aroundPhrase = self.sentence.prepositionalPhrases.get('around')
        
        if self.sentence.verb == 'look':
            if self.sentence.verbOnly():
                return True
            if atPhrase is not None and atPhrase.object == 'room':
                return True
            if aroundPhrase is not None:
                return True
            
    
        return False
        
    def isLookingAtResource(self):
        if self.sentence.verb == 'look':
            if self.sentence.prepositionalPhrases:
                return True
            if self.sentence.object:
                return True
        
        return False
        
    def isReading(self):
        if self.sentence.verb == 'read':
            return True
        else:
            return False
        
    def isGetting(self):
        if self.sentence.verb == 'get':
            return True
        else:
            return False
        
    def isPlacing(self):
        if self.sentence.verb == 'put':
            return True
        else:
            return False
    
    def isThrowing(self):
        if self.verb == 'throw':
            return True
        else:
            return False
    
    def isThrowingAt(self):
        if ((self.verb == 'throw') and
            (self.preposition == 'at')):
            return True
        else:
            return False
        
    def isThrowingIn(self):
        if ((self.verb == 'throw') and
            (self.preposition == 'in')):
            return True
        else:
            return False
        
        
    def isCheckingInventory(self):
        atPhrase = self.sentence.prepositionalPhrases.get('at')
        inPhrase = self.sentence.prepositionalPhrases.get('in')
        if ((self.sentence.object == 'inventory' or 
             (atPhrase and atPhrase.object == 'inventory') or
             (inPhrase and inPhrase.object == 'inventory')) and
            (self.sentence.verb == 'look' or
             self.sentence.verb is None)):
            return True
        else:
            return False
            
        
    def isQuitting(self):
        if self.verb == 'quit':
            return True
        else:
            return False
        
    def isSaving(self):
        if self.verb == 'save':
            return True
        else:
            return False
        
    def isRestoring(self):
        if self.verb == 'restore':
            return True
        else:
            return False
        
    def isEating(self):
        if self.verb == 'eat':
            return True
        else:
            return False
        
    def isDestroying(self):
        if self.verb == 'destroy':
            return True
        else:
            return False
        
    def isCutting(self):
        if self.verb == 'cut':
            return True
        else:
            return False
        
    def isTalking(self):
        if self.sentence.verb == 'talk':
            return True
        else:
            return False
        
    def isAsking(self):
        if self.sentence.verb == 'ask':
            return True
        else:
            return False
        
    def isWriting(self):
        if self.verb == 'write':
            return True
        else:
            return False
        
    def isPositioningSelf(self):
        if ((self.verb == 'get' or
             self.verb == 'go' or
             self.verb == 'climb') and
            (self.preposition == 'under' or
             self.preposition == 'on')):
            return True
        else:
            return False
        
    def isSwimming(self):
        if self.verb == 'swim':
            return True
        else:
            return False
        
    def isKissing(self):
        if self.verb == 'kiss':
            return True
        else:
            return False
        
    def isListening(self):
        if self.verb == 'listen':
            return True
        else:
            return False
        
    def isTasting(self):
        if self.verb == 'taste':
            return True
        else:
            return False
        
    def isSmelling(self):
        if self.verb == 'smell':
            return True
        else:
            return False
        
    def isFeeling(self):
        if self.verb == 'feel':
            return True
        else:
            return False
        
    def isHugging(self):
        if self.verb == 'hug':
            return True
        else:
            return False
        
    def isAttaching(self):
        if self.verb == 'attach':
            return True
        else:
            return False
        
    def isUnattaching(self):
        if self.verb == 'unattach':
            return True
        else:
            return False
        
    def isReplacing(self):
        if self.verb == 'replace':
            return True
        else:
            return False
        
    def isTearing(self):
        if self.verb == 'tear':
            return True
        else:
            return False
        
    def isStriking(self):
        if self.verb == 'strike':
            return True
        else:
            return False
        
    def isOpening(self):
        if self.verb == 'open':
            return True
        else:
            return False
        
    def isClosing(self):
        if self.verb == 'close':
            return True
        else:
            return False
        
    def isLocking(self):
        if self.verb == 'lock':
            return True
        else:
            return False
        
    def isUnlocking(self):
        if self.verb == 'unlock':
            return True
        else:
            return False
        
    def isBlocking(self):
        if self.verb == 'block':
            return True
        else:
            return False
        
    def isUnblocking(self):
        if self.verb == 'unblock':
            return True
        else:
            return False
        
    def isDipping(self):
        if self.verb == 'dip':
            return True
        else:
            return False
        
    def isGiving(self):
        if self.verb == 'give':
            return True
        else:
            return False
        
    def isSearching(self):
        if self.verb == 'search':
            return True
        else:
            return False
        
    def isClimbing(self):
        if self.verb == 'climb':
            return True
        else:
            return False