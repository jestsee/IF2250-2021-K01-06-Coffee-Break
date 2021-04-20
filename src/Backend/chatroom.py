'''
    Python file to process the chatroom related processing on the database
'''

import sqlite3
import uuid
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
# backendSrc = '../../Backend/storage.db'
backendSrc = dir_path + "/storage.db"

__connectToChatroomTableSQL = """
        SELECT messageId,content,timestamp,message.chatroomId 
        FROM chatroom, message
        WHERE (chatroom.chatroomId, message.chatroomId) = (:chatroomId, :chatroomId)
    """

__sendMessageSQL = """
    INSERT INTO message 
    VALUES(:messageId, :content, :timestamp, :chatroomId)
"""

__deleteMessageSQL = """
    DELETE FROM message
    WHERE ( messageId, chatroomId ) = ( :messageId, :chatroomId )
"""

def createChatroom(firstUserId, secondUserId, chatroomId) : 
    newChatroomQuery = """INSERT INTO chatroom VALUES(:chatroomId, :firstUserId, :secondUserId)"""
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

def sendMessage(chatroomId, message) : 
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
            'chatroomId' : chatroomId
        })  

        #Commit changes
        conn.commit()

        #Close connection
        conn.close()

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
    c.execute(__connectToChatroomTableSQL, {'chatroomId' : chatroomId});
    data = c.fetchall()
    print(data)

