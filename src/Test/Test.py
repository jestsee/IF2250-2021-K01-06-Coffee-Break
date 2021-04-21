from Frontend.typeDefs.Chatroom import Chatroom
from Frontend.typeDefs.Message import Message
import Backend.chatroom as chatroom_db
import uuid


# # Testing 
# message = Message(1, "Hey", "There")
# print(type(message) == Message)

# # Testing 
# # Create chatroom in backend 
# # Chatroom.createChatroom();

# testChatroomId = str(uuid.uuid4())
# testFirstUserId = 12
# testSecondUserId = 10
# # createChatroom(testChatroomId, testFirstUserId, testSecondUserId)

# message = Message(1, "Hey", "12 Nov 2020")
# chat = Chatroom(testChatroomId, testFirstUserId, testSecondUserId)
# chatroom_db.sendMessage(chat.getChatroomId(), "Hey There")


# __firstUserId = 20
# __secondUserId = 10
# __chatroomId = chatroom_db.createChatroom(__firstUserId, __secondUserId)
# __chatroom = Chatroom(__chatroomId, __firstUserId, __secondUserId)

__currentChatroomId = "2e88cf26-afb9-4c8e-a057-7dbb0e5a34c0"
__chatroom = Chatroom(__currentChatroomId, 20, 10)

# chatroom_db.clearChatroomMessages(__currentChatroomId)

# chatroom_db.sendMessage(__chatroom.getChatroomId(), str(uuid.uuid4()))
# chatroom_db.sendMessage(__chatroom.getChatroomId(), str(uuid.uuid4()))
# chatroom_db.sendMessage(__chatroom.getChatroomId(), str(uuid.uuid4()))

# def test_sendMessage() :
#     unique_string = str(uuid.uuid4())
#     chatroom_db.sendMessage(__chatroom.getChatroomId(), unique_string)
    
#     for Message in chatroom_db.fetchMessages(__chatroom.getChatroomId()) : 
#         for content in Message : 
#             print(content)

# test_sendMessage()
