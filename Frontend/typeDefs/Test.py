from Chatroom import Chatroom
from Message import Message
import uuid
def createChatroom(firstUserId, secondUserId, chatroomId) : 
    newChatroomQuery = """INSERT INTO chatroom VALUES(:chatroomId, :firstUserId, :secondUserId)"""
    

    conn = sqlite3.connect('../../Backend/storage.db')
    c = conn.cursor()
    c.execute(newChatroomQuery, {
        'chatroomId' : chatroomId,
        'firstUserId' : firstUserId,
        'secondUserId' : secondUserId
    })  

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

# # Testing 
# message = Message(1, "Hey", "There")
# print(type(message) == Message)

# Testing 
# Create chatroom in backend 
# Chatroom.createChatroom();

testChatroomId = uuid.uuid4()
testFirstUserId = 12
testSecondUserId = 10
createChatroom(testChatroomId, testFirstUserId, testSecondUserId)

message = Message(1, "Hey", "12 Nov 2020")
chat = Chatroom(testChatroomId, testFirstUserId, testSecondUserId, [])
chat.sendMessage(message)
chat.sendMessage("There")
chat.fetchMessages()