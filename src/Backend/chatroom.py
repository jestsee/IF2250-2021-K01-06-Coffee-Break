'''
    Python file to process the chatroom related processing on the database
'''

import sqlite3
import uuid
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
backendSrc = dir_path + "/storage.db"

__fetchChatroomMessagesSQL = """
        SELECT messageId,content,timestamp,message.chatroomId, senderId 
        FROM chatroom, message
        WHERE (chatroom.chatroomId, message.chatroomId) = (:chatroomId, :chatroomId)
    """

__sendMessageSQL = """
    INSERT INTO message 
    VALUES(:messageId, :content, :timestamp, :chatroomId, :senderId )
"""

__deleteMessageSQL = """
    DELETE FROM message
    WHERE ( messageId, chatroomId ) = ( :messageId, :chatroomId )
"""

__clearChatroomMessagesSQL = """
    DELETE FROM message
    WHERE chatroomId = :chatroomId 
"""

def createChatroom(firstUserId, secondUserId) : 
    newChatroomQuery = """INSERT INTO chatroom VALUES(:chatroomId, :firstUserId, :secondUserId)"""
    chatroomId = str(uuid.uuid4())
    conn = sqlite3.connect(backendSrc)
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

    return chatroomId

def sendMessage(chatroomId, senderId, message) : 
        '''Sending message to the database using message string as argument'''
        if(type(message) != str) : 
            raise ValueError("Invalid argument for sending message.")
        conn = sqlite3.connect(backendSrc)
        c = conn.cursor()

        # Id Message 
        messageId = str(uuid.uuid4())

        #Mendapatkan waktu
        now = datetime.now()
        now_string = now.strftime("%d/%m/%Y %H:%M:%S")

        c.execute(__sendMessageSQL, {
            'messageId' : messageId,
            'content' : message,
            'timestamp': now_string,
            'senderId' : senderId,
            'chatroomId' : chatroomId
        })  

        #Commit changes
        conn.commit()

        #Close connection
        conn.close()
        
        return messageId

def deleteMessage(chatroomId, messageId) : 
    '''Delete message from the database using message string as argument'''
    if(type(chatroomId) != str or type(messageId) != str) : 
        raise ValueError("Invalid argument for deleting a message.")
    conn = sqlite3.connect(backendSrc)
    c = conn.cursor()

    c.execute(__deleteMessageSQL, {
        'messageId' : messageId,
        'chatroomId' : chatroomId
    })  

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

def fetchMessages(chatroomId) : 
    '''Fetching all messages from the database'''
    if(type(chatroomId) != str) : 
        raise ValueError("fetchMessages must be provided with a valid chatroomId of type str")
    conn = sqlite3.connect(backendSrc)
    c = conn.cursor()
    c.execute(__fetchChatroomMessagesSQL, {'chatroomId' : chatroomId});
    data = c.fetchall()
    
    #Close connection
    conn.close()
    return data

def clearChatroomMessages(chatroomId) : 
    '''Delete all messages of a certain chatroom from the database'''
    if(type(chatroomId) != str) : 
        raise ValueError("fetchMessages must be provided with a valid chatroomId of type str")
    conn = sqlite3.connect(backendSrc)
    c = conn.cursor()
    c.execute(__clearChatroomMessagesSQL, {'chatroomId' : chatroomId});
    #Commit changes
    conn.commit()

    #Close connection
    conn.close()