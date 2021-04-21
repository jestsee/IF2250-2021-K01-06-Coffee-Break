import tkinter as tk
import datetime
import sqlite3
import sys

global mood

mood=0000 

today = datetime.date.today()

win = tk.Tk()
win.title("Mood")
win.geometry("1280x720")

# photo = tk.PhotoImage(file=r"C:/Users/RHEA ELKA PANDUMPI/RPL/happy.png")

conn = sqlite3.connect('mood.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS jurnal(
        moodId integer,
        date text,
        mood_record text,
        notes text
) """)


conn.commit()

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
        lbl1 = tk.Label(win, text="Your mood today", width=50, height=10)
        lbl1.grid(column=100,row=0)
        lbl2 = tk.Label(win, text=getTheDataFromDay(0)[2], padx=50,pady=15)
        lbl2.grid(column=100,row=1)
        #button = tk.Button(win,image=photo,padx=5,pady=5).grid(column=100,row=2) # CARA RESIZENYA GMN
        if(getTheDataFromDay(0)[3]==None):
            journal = tk.Button(win,text="Wanna add some journal?",command=lambda:[AddJournal(),switch(journal)], padx=50,pady=15)
            editmood = tk.Button(win,text="Edit Mood?",command=lambda:[editMood(),switch(editmood),switch(lbl2)], padx=5,pady=5)
            journalShow = journal.grid(column=100,row=2)
        else:
            x = getTheDataFromDay(0)
            journal= tk.Label(win,text=getTheDataFromDay(0)[3],padx=50,pady=15)
            journal.grid(column=100,row=3)
            editjournal = tk.Button(win,text="Edit Journal?",command=lambda:[editJournal(),switch(editjournal),switch(editmood),switch(journal)], padx=50,pady=15)
            editjournal.grid(column=100,row=4)
            editmood = tk.Button(win,text="Edit Mood?",command=lambda:[editMood(),switch(editmood),switch(lbl2),switch(editjournal),switch(journal)], padx=5,pady=5)
        editmood.grid(column=100,row=2)

def sidePage():
    threeDays = tk.Label(win, text="Last 3 days overview!",padx=50,pady=15).grid(column=200,row=0)
    x=[0]
    button=[]
    for i in range(1,4):
        if(getTheDataFromDay(i)!=None):
            x.append(getTheDataFromDay(i))
            firstDay = tk.Label(win,text=getTheDataFromDay(i)[2],padx=50,pady=15).grid(column=200,row=i) 
            if(i==1):
                button1 = tk.Button(win,text="Journal",command=lambda:[journalPage(x[1])],padx=15,pady=10).grid(column=201,row=i)
            elif(i==2):
                button2 = tk.Button(win,text="Journal",command=lambda:[journalPage(x[2])],padx=15,pady=10).grid(column=201,row=i)
            elif(i==3):
                button3 = tk.Button(win,text="Journal",command=lambda:[journalPage(x[3])],padx=15,pady=10).grid(column=201,row=i)
        else:
            firstDay = tk.Label(win,text="No entry yet",padx=50,pady=15).grid(column=200,row=i)

def journalPage(x):
    win1 = tk.Tk()
    win1.title("Journal")
    win1.geometry("200x500")
    date = tk.Label(win1,text="Journal for " + x[1],padx=50,pady=50)
    date.grid(column=100,row=0)
    journal = tk.Label(win1,text=x[3],padx=50,pady=50)
    journal.grid(column=100,row=1)
    goBack = tk.Button(win1,text="Close",command=lambda:[destroy(win1)],padx=15,pady=10).grid(column=100,row=2)

def destroy(win1):
    win1.destroy()

def editJournal():
    lbl = tk.Label(win, text="Edit your journal here",width=50,height=10).grid(column=100,row=0)
    entry_1 = tk.StringVar()
    entry_widget_1 = tk.Entry(win, textvariable=entry_1).grid(column=100,row=1)
    submit = tk.Button(win,text="Submit",command=lambda: [getJournal(entry_1.get()),switch(submit)])
    submitShow = submit.grid(column=100,row=2)

def editMood():
    veryBad = tk.Button(win,text="Very Bad",command=lambda: [editMoodDatabase("Very Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    veryBad.grid(column=100,row=1)
    bad = tk.Button(win,text="Bad",command=lambda: [editMoodDatabase("Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    bad.grid(column=100,row=2)
    flat = tk.Button(win,text="Flat",command= lambda: [editMoodDatabase("Flat"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    flat.grid(column=100,row=3)
    happy = tk.Button(win,text="Happy",command= lambda: [editMoodDatabase("Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    happy.grid(column=100,row=4)
    veryHappy = tk.Button(win,text="Very Happy",command= lambda: [editMoodDatabase("Very Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    veryHappy.grid(column=100,row=5)

def editMoodDatabase(text):
    conn = sqlite3.connect('mood.db')
    sql = "Update jurnal set mood_record=? where date=?"
    c = conn.cursor()
    strToday = str(today)
    val = (text,strToday)
    c.execute(sql,val)
    conn.commit()
    initPage()
    sidePage()

def editJournalDatabase(text):
    conn = sqlite3.connect('mood.db')
    sql = "Update jurnal set notes=? where date=?"
    c = conn.cursor()
    strToday = str(today)
    val = (text,strToday)
    c.execute(sql,val)
    conn.commit()
    initPage()
    sidePage()

def click():
    veryBad = tk.Button(win,text="Very Bad",command=lambda: [NextSection("Very Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    veryBad.grid(column=100,row=1)
    bad = tk.Button(win,text="Bad",command=lambda: [NextSection("Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    bad.grid(column=100,row=2)
    flat = tk.Button(win,text="Flat",command= lambda: [NextSection("Flat"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    flat.grid(column=100,row=3)
    happy = tk.Button(win,text="Happy",command= lambda: [NextSection("Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    happy.grid(column=100,row=4)
    veryHappy = tk.Button(win,text="Very Happy",command= lambda: [NextSection("Very Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
    veryHappy.grid(column=100,row=5)

def NextSection(text):
    global mood
    conn = sqlite3.connect('mood.db')
    sql = "Insert into jurnal values (?, ?, ?, null)"
    c = conn.cursor()
    strToday = str(today)
    val = (mood,strToday,text)
    c.execute(sql,val)
    conn.commit()
    mood=mood+1
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
    val = (text,strToday)
    c.execute(sql,val)
    conn.commit()
    initPage()
    sidePage()

def switch(b1):
    b1.grid_forget()

initPage()
sidePage()

win.mainloop()