import sqlite3
import os


#Create or connect database activity
dir_path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(dir_path + '/storage.db')

#Create cursor
c = conn.cursor()

# Create User Table
# Create table buat nampung data user
c.execute('''CREATE TABLE IF NOT EXISTS user
             (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
             nama TEXT, 
             dom TEXT, 
             hobi TEXT)''')

# Create table buat nampung data teman yg fk nya references ke table user
c.execute('''CREATE TABLE IF NOT EXISTS teman
             (user_id1 INTEGER, user_id2 INTEGER,
                PRIMARY KEY (user_id1, user_id2),
                FOREIGN KEY (user_id1) REFERENCES user (user_id),
                FOREIGN KEY (user_id2) REFERENCES user (user_id))''')

# Create Activity Table 
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
        senderId integer NOT NULL,
        FOREIGN KEY (chatroomId) REFERENCES chatroom(chatroomId)
        FOREIGN KEY (senderId) REFERENCES user(user_id)
) """)

# Create Psychologist table
c.execute("""
        CREATE TABLE IF NOT EXISTS psikolog (
                psikologId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                nama VARCHAR(255),
                asal_kota VARCHAR(255)
        )
""")

#Commit changes
conn.commit()

#Close connection
conn.close()
