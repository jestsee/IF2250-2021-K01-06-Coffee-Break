import sqlite3
import uuid

#  Local Import 
from Message import Message 
from datetime import datetime
class Chatroom : 
    
    __connectToChatroomTableSQL = """
        SELECT messageId,content,timestamp,message.chatroomId 
        FROM chatroom, message
        WHERE (chatroom.chatroomId, message.chatroomId) = (:chatroomId, :chatroomId)
    """

    __sendMessageSQL = """
        INSERT INTO message VALUES(:messageId, :content, :timestamp, :chatroomId)
    """

    def __init__(self, chatroomId, firstUserId, secondUserId) : 
        if(type(chatroomId) != str or type(firstUserId) != int or type(secondUserId) != int ) :
            raise ValueError("Invalid input for initiating object of type chat")
        # Values 
        self.__chatroomId = chatroomId
        self.__firstUserId = firstUserId
        self.__secondUserId = secondUserId

    def __init__(self, chatroomId, firstUserId, secondUserId, messages) : 
        if(type(chatroomId) != str or type(firstUserId) != int or type(secondUserId) != int) :
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
        '''result : Printing messages to the command line'''
        for message in self.__messages : 
            print(message);

    # Database Related Methods
    def fetchMessages(self) : 
        '''Fetching all messages from the database'''
        conn = sqlite3.connect('../../Backend/storage.db')
        c = conn.cursor()
        c.execute(self.__connectToChatroomTableSQL, {'chatroomId' : self.__chatroomId});
        data = c.fetchall()
        print(data)

    def sendMessage(self, message) : 
        '''Sending message to the database using message string as argument'''
        if(type(message) != str) : 
            raise ValueError("Invalid argument for sending message.")
        conn = sqlite3.connect('../../Backend/storage.db')
        c = conn.cursor()
        # Id Message 
        messageId = str(uuid.uuid4())

        #Mendapatkan waktu
        now = datetime.now()
        now_string = now.strftime("%d/%m/%Y %H:%M:%S")

        c.execute(self.__sendMessageSQL, {
            'messageId' : messageId,
            'content' : message,
            'timestamp': now_string,
            'chatroomId' : self.__chatroomId
        })  

        #Commit changes
        conn.commit()

        #Close connection
        conn.close()

    


        







