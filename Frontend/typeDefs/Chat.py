import sqlite3

#  Local Import 
from Message import Message 

class Chat : 
    __connectToChatroomTable = """
        SELECT messageId,content,timestamp,chatroomId, FROM chatroom, message
        WHERE (chatroom.chatroomId, message.chatroomId) = ({self.__chatroomId}, {self.__chatroomId})
    """

    def __init__(self, chatroomId, firstUserId, secondUserId) : 
        if(type(id) != int or type(firstUserId) != int or type(secondUserId) != int ) :
            raise ValueError("Invalid input for initiating object of type chat")
        # Values 
        self.__chatroomId = chatroomId
        self.__firstUserId = firstUserId
        self.__secondUserId = secondUserId

    def __init__(self, chatroomId, firstUserId, secondUserId, messages) : 
        if(type(chatroomId) != int or type(firstUserId) != int or type(secondUserId) != int) :
            raise ValueError("Invalid input for initiating object of type chat")
        # Values 
        if(type(messages) != list or ( len(messages) > 0 and type(messages[0]) != Message )) : 
            raise ValueError("Invalid input for initiating object of type chat; messages parameter must be a list of object Message")
        self.__chatroomId = chatroomId
        self.__firstUserId = firstUserId
        self.__secondUserId = secondUserId
        self.__messages = messages
    
    # General Methods 
    def setMessages(self, messages):
        if(type(messages) != list or ( len(messages) > 0 and type(messages[0]) != Message )) : 
            raise ValueError("Invalid input for setting messages on chat. Messages attribute must be a list of object Message")
        self.__messages = messages; 
    
    def printMessages(self) : 
        '''
            result : Printing messages to the command line
        '''
        for message in self.__messages : 
            print(message);

    # Database Related Methods
    def fetchMessages(self) : 
        conn = sqlite3.connect('../../Backend/storage.db')
        
        c = conn.cursor()
        c.execute(self.__connectToChatroomTable);
        data = c.fetchall
        print(data)

    def sendMessages(self, message) : 
        if(type(message) != Message) : 
            raise ValueError("Invalid argument for sending message.")
        conn = sqlite3.connect('../../Backend/storage.db')
        c = conn.cursor()
        



# Testing 
message = Message(1, "Hey", "12 Nov 2020")
chat = Chat(12, 12, 12, [message])
chat.printMessages();



