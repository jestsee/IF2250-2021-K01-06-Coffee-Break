import sqlite3

#Create or connect database activity
conn = sqlite3.connect('storage.db')
#Create cursor
c = conn.cursor()

#Create Activity Table 
c.execute("""
CREATE TABLE IF NOT EXISTS activity (
    activityId integer PRIMARY KEY,
    activityName text,
    activityDetail text,
    timestamp text
)
""")

# Create Jurnal Table
c.execute("""CREATE TABLE IF NOT EXISTS jurnal(
        moodId integer PRIMARY KEY,
        date text,
        mood_record text,
        notes text
) """)

# Create Chat Table 
c.execute("""CREATE TABLE IF NOT EXISTS chatroom(
        chatroomId VARCHAR(50) PRIMARY KEY NOT NULL,
        firstUserId integer,
        secondUserId integer
) """)

# Create Message Table 
c.execute("""CREATE TABLE IF NOT EXISTS message(
        messageId VARCHAR(50) PRIMARY KEY NOT NULL,
        content VARCHAR(255),
        timestamp DATETIME NOT NULL,
        chatroomId integer NOT NULL,
        FOREIGN KEY (chatroomId) REFERENCES chatroom(chatroomId)
) """)

#Commit changes
conn.commit()

#Close connection
conn.close()
