from agents import (baldevarth,
                    player)
from archmage.rooms import room

agentsByKey = {}

def createAgents(game):
    storeByKey([baldevarth.Baldevarth(key='baldevarth'),
                player.Player(key='player')])
    for (key, agent) in agentsByKey.items():
        agent.setGame(game)

def getAgent(agent_key):
    return agentsByKey[agent_key]

def placeAgentsInRooms():
    placeAgentInRoom('player', 'archmage_ritual_room')
    placeAgentInRoom('baldevarth', 'archmage_ritual_room')



    
def storeByKey(agents):
    for agent in agents:
        agentsByKey[agent.key] = agent
    
def placeAgentInRoom(agent_key, room_key):
    agentForKey = getAgent(agent_key)
    roomForKey = room.getRoom(room_key)
    agentForKey.changeOwner(roomForKey)