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
        moodId integer,
        date text,
        mood_record text,
        notes text
) """)


# c.execute("DELETE FROM activity")

#Commit changes
conn.commit()

#Close connection
conn.close()
