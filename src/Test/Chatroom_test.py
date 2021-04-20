import uuid
import pytest

from Frontend.typeDefs.Chatroom import Chatroom
from Frontend.typeDefs.Message import Message
from Backend.chatroom import *

'''
    Python file to test the Chatroom and Message data definition module,
    and also testing the backend chatroom module.

'''

__chatroomId = str(uuid.uuid4())
__firstUserId = 20
__secondUserId = 10
__chatroom = Chatroom(__chatroomId, __firstUserId, __secondUserId)

# Message module test
# def test_initMessage() :
#     message = Message(10, "Hello There", "21 November 2020")
#     assert message.getId() == 10

def test_initMessageEmpty() : 
    with pytest.raises(TypeError) : 
        Message()

def test_message_setId():
    message = Message(10, "Hello There", "21 November 2020")
    message.setId(20)
    assert message.getId() == 20 

# Chatroom module test
def test_initChatRoom() :
    assert __chatroom.getFirstUserId() == 20

# Test Setters and getters
def test_setFirstUserId() : 
    with pytest.raises(ValueError):
        __chatroom.setFirstUserId("Hey")

def test_setSecondUserId() :
    with pytest.raises(ValueError):
        __chatroom.setSecondUserId("What's Up?")

def test_setMessages() : 
    with pytest.raises(ValueError):
        __chatroom.setMessages(123)