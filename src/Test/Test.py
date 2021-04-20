from Frontend.typeDefs.Chatroom import Chatroom
from Frontend.typeDefs.Message import Message
from Backend.chatroom import *
import uuid


# # Testing 
# message = Message(1, "Hey", "There")
# print(type(message) == Message)

# Testing 
# Create chatroom in backend 
# Chatroom.createChatroom();

testChatroomId = str(uuid.uuid4())
testFirstUserId = 12
testSecondUserId = 10
# createChatroom(testChatroomId, testFirstUserId, testSecondUserId)

message = Message(1, "Hey", "12 Nov 2020")
chat = Chatroom(testChatroomId, testFirstUserId, testSecondUserId)
sendMessage(chat.getChatroomId(), "Hey There")