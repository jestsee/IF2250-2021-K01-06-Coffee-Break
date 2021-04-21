import sqlite3
import uuid
import os
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
backendSrc = dir_path + "/storage.db"

# Memperoleh jurnal dari hari tertentu
def getTheDataFromDay(i):
    conn = sqlite3.connect(backendSrc)
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(datetime.date.today() - datetime.timedelta(days=i))
    # print(strDay)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    for row in rows:
        return row
    conn.close()

# Perubahan database setelah dipilih edit mood
def editMoodDatabase(text):
    conn = sqlite3.connect(backendSrc)
    sql = "Update jurnal set mood_record=? where date=?"
    c = conn.cursor()
    strToday = str(datetime.date.today())
    val = (text,strToday)
    c.execute(sql,val)
    conn.commit()
    conn.close()

def editJournalDatabase(text):
    conn = sqlite3.connect(backendSrc)
    sql = "Update jurnal set notes=? where date=?"
    c = conn.cursor()
    strToday = str(datetime.date.today())
    val = (text,strToday)
    c.execute(sql,val)
    conn.commit()
    conn.close()


# Memasukkan mood ke database
def NextSection(text):
    conn = sqlite3.connect(backendSrc)
    sql = "Insert into jurnal values (?, ?, ?, null)"
    c = conn.cursor()
    c.execute("SELECT COUNT(*) from jurnal")
    num_row=c.fetchone()[0]
    strToday = str(datetime.date.today())
    val = (num_row,strToday,text)
    c.execute(sql,val)
    conn.commit()
    conn.close()
    
# Memasukkan jurnal ke database

def getJournal(text):
    conn = sqlite3.connect(backendSrc)
    sql = "Update jurnal set notes=? where date=?"
    c = conn.cursor()
    strToday = str(datetime.date.today())
    val = (text,strToday)
    c.execute(sql,val)
    conn.commit()
    conn.close()