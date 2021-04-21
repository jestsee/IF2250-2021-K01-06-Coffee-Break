import tkinter as tk
from tkinter import *
import datetime
import sqlite3
import sys
from Backend.mood import * 

class MoodPage(tk.Frame):
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
            submit = tk.Button(self,text="Submit",command=lambda: [getJournalSwitch(entry_1.get())])
            submitShow = submit.grid(column=100,row=2)

        # Tampilan edit mood

        def editMood():
            veryBad = tk.Button(self,text="Very Bad",command=lambda: [editMoodDatabaseSwitch("Very Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryBad.grid(column=100,row=1)
            bad = tk.Button(self,text="Bad",command=lambda: [editMoodDatabaseSwitch("Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            bad.grid(column=100,row=2)
            flat = tk.Button(self,text="Flat",command= lambda: [editMoodDatabaseSwitch("Flat"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            flat.grid(column=100,row=3)
            happy = tk.Button(self,text="Happy",command= lambda: [editMoodDatabaseSwitch("Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            happy.grid(column=100,row=4)
            veryHappy = tk.Button(self,text="Very Happy",command= lambda: [editMoodDatabaseSwitch("Very Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryHappy.grid(column=100,row=5)

        # Setelah opsi add mood dipilih

        def click():
            veryBad = tk.Button(self,text="Very Bad",command=lambda: [NextSectionSwitch("Very Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryBad.grid(column=100,row=1)
            bad = tk.Button(self,text="Bad",command=lambda: [NextSectionSwitch("Bad"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            bad.grid(column=100,row=2)
            flat = tk.Button(self,text="Flat",command= lambda: [NextSectionSwitch("Flat"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            flat.grid(column=100,row=3)
            happy = tk.Button(self,text="Happy",command= lambda: [NextSectionSwitch("Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            happy.grid(column=100,row=4)
            veryHappy = tk.Button(self,text="Very Happy",command= lambda: [NextSectionSwitch("Very Happy"),switch(veryBad),switch(bad),switch(flat),switch(happy),switch(veryHappy)],padx=50,pady=15)
            veryHappy.grid(column=100,row=5)

        # Menambahkan jurnal

        def AddJournal():
            lbl = tk.Label(self, text="Write your journal here",width=50,height=10).grid(column=100,row=0)
            entry_1 = tk.StringVar()
            entry_widget_1 = tk.Entry(self, textvariable=entry_1).grid(column=100,row=1)
            submit = tk.Button(self,text="Submit",command=lambda: [getJournalSwitch(entry_1.get())])
            submitShow = submit.grid(column=100,row=2)

        # Menghilangkan tampilan suatu button

        def switch(b1):
            b1.grid_forget()

        def editMoodDatabaseSwitch(text):
            editMoodDatabase(text)
            initPage()
            sidePage()

        def editJournalDatabaseSwitch(text):
            editJournalDatabase(text)
            initPage()
            sidePage()

        def NextSectionSwitch(text):
            NextSection(text)
            initPage()
            sidePage()

        def getJournalSwitch(text):
            getJournal(text)
            initPage()
            sidePage()

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

if __name__ == "__main__":
    app = Application()
    app.mainloop()