import sqlite3

deleteAllChatroomQuery = 'DELETE FROM chatroom'
deleteAllMessagesQuery = 'DELETE FROM message'

conn = sqlite3.connect('../../Backend/storage.db')
c = conn.cursor()
c.execute(deleteAllChatroomQuery)  
#Commit changes
conn.commit()

c.execute(deleteAllMessagesQuery)  

#Commit changes
conn.commit()

#Close connection
conn.close()