import tkinter as tk
from tkinter import *
import datetime
import sqlite3
import sys
import pytest

# photo = tk.PhotoImage(file=r"C:/Users/RHEA ELKA PANDUMPI/RPL/happy.png")

# Memperoleh jurnal dari hari tertentu

class Mood(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        # Bagian kiri
        def initPage():
            if(getTheDataFromDay(0)==None):
                lbl = tk.Label(self, text="You haven't added any mood yet!",width=50, height=10).grid(column=100,row=0)
                button = tk.Button(self,text="Add Mood",command=lambda:[click(),switch(button)],padx=50,pady=15)
                buttonShow = button.grid(column=100,row=1)
            else:        
                lbl1 = tk.Label(self, text="Your mood today", width=50, height=10)
                lbl1.grid(column=100,row=0)
                lbl2 = tk.Label(self, text=getTheDataFromDay(0)[2], padx=50,pady=15)
                lbl2.grid(column=100,row=1)
                #button = tk.Button(win,image=photo,padx=5,pady=5).grid(column=100,row=2)
                if(getTheDataFromDay(0)[3]==None):
                    journal = tk.Button(self,text="Wanna add some journal?",command=lambda:[AddJournal(),switch(journal),switch(editmood)], padx=50,pady=15)
                    editmood = tk.Button(self,text="Edit Mood?",command=lambda:[editMood(),switch(editmood),switch(lbl2),switch(journal)], padx=5,pady=5)
                    journalShow = journal.grid(column=100,row=6)
                else:
                    x = getTheDataFromDay(0)
                    journal= tk.Label(self,text=getTheDataFromDay(0)[3],padx=50,pady=15)
                    journal.grid(column=100,row=3)
                    editjournal = tk.Button(self,text="Edit Journal?",command=lambda:[editJournal(),switch(editjournal),switch(editmood),switch(journal)], padx=50,pady=15)
                    editjournal.grid(column=100,row=4)
                    editmood = tk.Button(self,text="Edit Mood?",command=lambda:[editMood(),switch(editmood),switch(lbl2),switch(editjournal),switch(journal)], padx=5,pady=5)
                editmood.grid(column=100,row=2)
            threeDays = tk.Label(self, text="Last 3 days overview!",padx=50,pady=15).grid(column=200,row=0)
        # Bagian kanan
        def sidePage():
            x=[0]
            button=[]
            for i in range(1,4):
                if(getTheDataFromDay(i)!=None):
                    x.append(getTheDataFromDay(i))
                    firstDay = tk.Label(self,text=getTheDataFromDay(i)[2],padx=50,pady=15).grid(column=200,row=i) 
                    if(i==1):
                        button1 = tk.Button(self,text="Journal",command=lambda:[journalPage(x[1])],padx=15,pady=10).grid(column=201,row=i)
                    elif(i==2):
                        button2 = tk.Button(self,text="Journal",command=lambda:[journalPage(x[2])],padx=15,pady=10).grid(column=201,row=i)
                    elif(i==3):
                        button3 = tk.Button(self,text="Journal",command=lambda:[journalPage(x[3])],padx=15,pady=10).grid(column=201,row=i)
                else:
                    firstDay = tk.Label(self,text="No entry yet",padx=50,pady=15).grid(column=200,row=i)
       
        # Jurnal
        def journalPage(x):
            win1 = tk.Tk()
            win1.title("Journal")
            win1.geometry("200x500")
            date = tk.Label(win1,text="Journal for " + x[1],padx=50,pady=50)
            date.grid(column=100,row=0)
            journal = tk.Label(win1,text=x[3],padx=50,pady=50)
            journal.grid(column=100,row=1)
            goBack = tk.Button(win1,text="Close",command=lambda:[destroy(win1)],padx=15,pady=10).grid(column=100,row=2)

        # Tutup jendela

        def destroy(win1):
            win1.destroy()

        # Edit jurnal yang dipilih

        def editJournal():
            lbl = tk.Label(self, text="Edit your journal here",width=50,height=10).grid(column=100,row=0)
            entry_1 = tk.StringVar()
            entry_widget_1 = tk.Entry(self, textvariable=entry_1).grid(column=100,row=1)
            submit = tk.Button(self,text="Submit",command=lambda: [getJournal(entry_1.get()),switch(submit)])
            submitShow = submit.grid(column=100,row=2)

        # Tampilan edit mood

        def editMood():
            veryBad = tk.Button(self,text="Very Bad",command=lambda: [editMoodDatabase("Very Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryBad.grid(column=100,row=1)
            bad = tk.Button(self,text="Bad",command=lambda: [editMoodDatabase("Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            bad.grid(column=100,row=2)
            flat = tk.Button(self,text="Flat",command= lambda: [editMoodDatabase("Flat"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            flat.grid(column=100,row=3)
            happy = tk.Button(self,text="Happy",command= lambda: [editMoodDatabase("Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            happy.grid(column=100,row=4)
            veryHappy = tk.Button(self,text="Very Happy",command= lambda: [editMoodDatabase("Very Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryHappy.grid(column=100,row=5)

        # Perubahan database setelah dipilih edit mood

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

        # Perubahan database setelah dipilih edit journal

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

        # Setelah opsi add mood dipilih

        def click():
            veryBad = tk.Button(self,text="Very Bad",command=lambda: [NextSection("Very Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryBad.grid(column=100,row=1)
            bad = tk.Button(self,text="Bad",command=lambda: [NextSection("Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            bad.grid(column=100,row=2)
            flat = tk.Button(self,text="Flat",command= lambda: [NextSection("Flat"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            flat.grid(column=100,row=3)
            happy = tk.Button(self,text="Happy",command= lambda: [NextSection("Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            happy.grid(column=100,row=4)
            veryHappy = tk.Button(self,text="Very Happy",command= lambda: [NextSection("Very Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryHappy.grid(column=100,row=5)

        # Memasukkan mood ke database

        def NextSection(text):
            conn = sqlite3.connect('mood.db')
            sql = "Insert into jurnal values (?, ?, ?, null)"
            c = conn.cursor()
            c.execute("SELECT COUNT(*) from jurnal")
            num_row=c.fetchone()[0]
            strToday = str(today)
            val = (num_row,strToday,text)
            c.execute(sql,val)
            conn.commit()
            initPage()
            sidePage()

        # Menambahkan mood

        def AddJournal():
            lbl = tk.Label(self, text="Write your journal here",width=50,height=10).grid(column=100,row=0)
            entry_1 = tk.StringVar()
            entry_widget_1 = tk.Entry(self, textvariable=entry_1).grid(column=100,row=1)
            submit = tk.Button(self,text="Submit",command=lambda: [getJournal(entry_1.get()),switch(submit)])
            submitShow = submit.grid(column=100,row=2)

        # Menambahkan jurnal ke database

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

        # Menghilangkan tampilan suatu button

        def switch(b1):
            b1.grid_forget()
        
        # Tampilkan
        initPage()
        sidePage()

class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        win = tk.Frame(self)
        win.pack()
        win.grid_rowconfigure(0,minsize=720)
        win.grid_columnconfigure(0,minsize=1280)
        self.frames = {}
        frame = Mood(win,self)
        self.frames[Mood] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(Mood)
    def show_frame(self,page):
        frame = self.frames[page]
        frame.tkraise()

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

conn = sqlite3.connect('mood.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS jurnal(
        moodId integer PRIMARY KEY,
        date text,
        mood_record text,
        notes text
) """)

today = datetime.date.today()

conn.commit()
conn.close()
app = Application()

app.mainloop()