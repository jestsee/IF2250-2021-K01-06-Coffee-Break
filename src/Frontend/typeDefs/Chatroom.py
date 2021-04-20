#  Local Import 

'''
    Python file to define the Chatroom datatype
'''

import Backend.chatroom as chatroom_db
from Frontend.typeDefs.Message import Message 
from datetime import datetime


class Chatroom : 
    def __init__(self, chatroomId, firstUserId, secondUserId, messages = []) : 
        if(type(chatroomId) != str or type(firstUserId) != int or type(secondUserId) != int) :
            raise ValueError("Invalid input for initiating object of type chat")
        # Values
        if(type(messages) != list or ( len(messages) > 0 and type(messages[0]) != Message )) : 
            raise ValueError("Invalid input for initiating object of type chat; messages parameter must be a list of object Message")
        self.__chatroomId = chatroomId
        self.__firstUserId = firstUserId
        self.__secondUserId = secondUserId
        self.__messages = chatroom_db.fetchMessages(self.__chatroomId) if messages == [] else messages
    
    # General Methods 
    def setFirstUserId(self, firstUserId) : 
        if(type(firstUserId) != int) : 
            raise ValueError("Invalid input for setFirstUserId") 
        self.__firstUserId = firstUserId
        
    def getChatroomId(self) : 
        return self.__chatroomId

    def getFirstUserId(self) : 
        return self.__firstUserId
    
    def setSecondUserId(self, secondUserId) : 
        if(type(secondUserId) != int) : 
            raise ValueError("Invalid input for setFirstUserId")
        self.__secondUserId = secondUserId

    def getSecondUserId(self) : 
        return self.__secondUserId

    def setMessages(self, messages):
        if(type(messages) != list or ( len(messages) > 0 and type(messages[0]) != Message )) : 
            raise ValueError("Invalid input for setting messages on chat. Messages attribute must be a list of object Message")
        self.__messages = messages; 
    
    def getMessages(self) : 
        return self.__messages
    
    def printMessages(self) : 
        '''result : Printing messages to the command line'''
        for message in self.__messages : 
            print(message);


    


        







