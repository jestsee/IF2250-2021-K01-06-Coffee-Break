import tkinter as tk
import datetime
import sqlite3
import sys

global mood

mood=0000 # IDMOOD DI AWAL GIMANA NYETELNYA WKWK:(

today = datetime.date.today()
# print(today)

win = tk.Tk()
win.title("Mood")
win.geometry("800x500")

# photo = tk.PhotoImage(file=r"C:/Users/RHEA ELKA PANDUMPI/RPL/happy.png")

# Create a database or connect to one
conn = sqlite3.connect('mood.db')
# THIS WILL MAKE THE DATABASE

# cursor : the little thing you send off to do stuff, any sort of command the cursor does that
# Create a cursor

c = conn.cursor()

# a database is tables inside that do all the works
# designate what those columns are

# CREATE TABLE
# SQL COMMANDS

c.execute("""CREATE TABLE IF NOT EXISTS jurnal(
        moodId integer,
        date text,
        mood_record text,
        notes text
) """)

# COMMIT CHANGES

conn.commit()

# close connection

# Buat ngambil data dalam suatu tanggal
def getTheDataFromDay(i):
    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today - datetime.timedelta(days=i))
    # print(strDay)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    for row in rows:
        return row
    conn.close()

def initPage():
    if(getTheDataFromDay(0)==None):
        lbl = tk.Label(win, text="You haven't added any mood yet!",width=50, height=10).grid(column=100,row=0)
        button = tk.Button(win,text="Add Mood",command=lambda:[click(),switch(button)],padx=50,pady=15)
        buttonShow = button.grid(column=100,row=1)
    else:
        lbl = tk.Label(win, text="Your mood today", width=50, height=10).grid(column=100,row=0)
        lbl = tk.Label(win, text=getTheDataFromDay(0)[2], padx=50,pady=15).grid(column=100,row=1)
        #button = tk.Button(win,image=photo,padx=5,pady=5).grid(column=100,row=2) # CARA RESIZENYA GMN
        if(getTheDataFromDay(0)[3]==None):
            journal = tk.Button(win,text="Wanna add some journal?",command=lambda:[AddJournal(),switch(journal)], padx=50,pady=15)
            journalShow = journal.grid(column=100,row=2)
        else:
            journal= tk.Label(win,text=getTheDataFromDay(0)[3],padx=50,pady=15).grid(column=100,row=3)

def sidePage():
    threeDays = tk.Label(win, text="Last 3 days overview!",padx=50,pady=15).grid(column=200,row=0)
    for i in range(1,4):
        if(getTheDataFromDay(i)!=None):
            x = getTheDataFromDay(i)
            firstDay = tk.Label(win,text=getTheDataFromDay(i)[2],padx=50,pady=15).grid(column=200,row=i) # sesuain sama daatabase
            ######### button = tk.Button(win,)
            button = tk.Button(win,text="Journal",command=lambda:[journalPage(x)],padx=15,pady=10)
            buttonShow = button.grid(column=201,row=i)
            ##button = tk.Button(win,text="Edit",padx=15,pady=10).grid(column=202,row=i)
        else:
            firstDay = tk.Label(win,text="No entry yet",padx=50,pady=15).grid(column=200,row=i) # sesuain sama daatabase

def journalPage(x):
    win.destroy()
    win1 = tk.Tk()
    win1.title("Journal")
    win1.geometry("800x500")
    journal = tk.Label(win1,text=x[3],padx=50,pady=15)
    journal = journal.grid(column=200,row=0)
    goBack = tk.Button(win1,text="Go Back",command=lambda:goBackToPrevious(win1),padx=15,pady=10).grid(column=200,row=1)

def goBackToPrevious(win1):
    win1.destroy()
    import mood

'''
def delete(i):
    print(i)
    conn = sqlite3.connect('mood.db')
    strDay = str(today - datetime.timedelta(days=i))
    print(strDay)
    sql = "Delete from jurnal where date=?"
    c = conn.cursor()
    val = (strDay,)
    c.execute(sql,val)
    conn.commit()
    initPage()
    sidePage()

    conn = sqlite3.connect('mood.db')
    sql = "Select * from jurnal where date=?"
    c = conn.cursor()
    strDay = str(today - datetime.timedelta(days=i))
    # print(strDay)
    val = (strDay,)
    c.execute(sql,val)
    rows = c.fetchall()
    for row in rows:
        return row
    conn.close()

def edit(i): # males bangettt
    conn = sqlite3.connect('mood.db')
    strDay = str(today - datetime.timedelta(days=i))
    sql = "Delete from jurnal where date=?"
    sql = "Update jurnal set notes=? where date=?"
    c = conn.cursor()
    val = (strDay)
    c.execute(sql,val)
    conn.commit()

'''

def click():
    happy = tk.Button(win,text="Happy",command=lambda: [NextSection("Happy"),switch(happy),switch(sad),switch(good)],padx=50,pady=15)
    happyShow = happy.grid(column=100,row=1)
    sad = tk.Button(win,text="Sad",command=lambda: [NextSection("Sad"),switch(happy),switch(sad),switch(good)],padx=50,pady=15)
    sadShow = sad.grid(column=100,row=2)
    good = tk.Button(win,text="Good",command= lambda: [NextSection("Good"),switch(happy),switch(sad),switch(good)],padx=50,pady=15)
    goodShow = good.grid(column=100,row=3)
# button = tk.Button(win,text="Add Mood",command=click,image=photo).grid(column=0,row=1)

def NextSection(text):
    global mood
    conn = sqlite3.connect('mood.db')
    sql = "Insert into jurnal values (?, ?, ?, null)"
    c = conn.cursor()
    strToday = str(today)
    val = (mood,strToday,text) # date bisa pake library #moodId gimana?
    c.execute(sql,val)
    conn.commit()
    mood=mood+1
    # munculin = tk.Label(win,text="Mood successfully added",padx=50,pady=15).grid(column=100,row=5)
    initPage()
    sidePage()

def AddJournal():
    lbl = tk.Label(win, text="Write your journal here",width=50,height=10).grid(column=100,row=0)
    entry_1 = tk.StringVar()
    entry_widget_1 = tk.Entry(win, textvariable=entry_1).grid(column=100,row=1)
    submit = tk.Button(win,text="Submit",command=lambda: [getJournal(entry_1.get()),switch(submit)])
    submitShow = submit.grid(column=100,row=2)

def getJournal(text):
    conn = sqlite3.connect('mood.db')
    sql = "Update jurnal set notes=? where date=?"
    c = conn.cursor()
    strToday = str(today)
    val = (text,strToday) # date bisa pake library #moodId gimana?
    c.execute(sql,val)
    conn.commit()
    initPage()
    sidePage()

def switch(b1):
    b1.grid_forget()

initPage()
sidePage()

win.mainloop()
