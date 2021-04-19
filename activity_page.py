import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from activity_list import activity_list
from datetime import datetime

class ActivityPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # #Setting background
        # bg = Image.open("img/background.png")
        # bg = bg.resize((int(bg.size[0]*1.6), int(bg.size[1]*1.6)))
        # bg = ImageTk.PhotoImage(bg)
        # bg_label = tk.Label(self, image=bg, bg="white")
        # bg_label.image = bg
        # bg_label.place(x=0,y=0)

        #Membuat side kiri
        Label = tk.Label(self, text="Here's what we got for you", font=("Helvetica Bold", 15))
        Label.place(x=35, y=10)

        left_canvas = tk.Canvas(self, bg="BLUE")
        left_canvas.config(width=550, height=550)
        left_canvas.place(x=35, y=60)

        #Membuat act1 inside side kiri
        act1_canvas = tk.Canvas(self, bg="WHITE")
        act1_canvas.config(width=475, height=80)
        act1_canvas.place(x=70, y=80)
        act1_canvas.create_text(40, 20, text="Activity 1")

        #Membuat act2 inside side kiri
        act2_canvas = tk.Canvas(self, bg="WHITE")
        act2_canvas.config(width=475, height=80)
        act2_canvas.place(x=70, y=180)
        act2_canvas.create_text(40, 20, text="Activity 2")

        #Membuat act3 inside side kiri
        act3_canvas = tk.Canvas(self, bg="WHITE")
        act3_canvas.config(width=475, height=80)
        act3_canvas.place(x=70, y=280)
        act3_canvas.create_text(40, 20, text="Activity 3")         

        #Membuat act4 inside side kiri
        act4_canvas = tk.Canvas(self, bg="WHITE")
        act4_canvas.config(width=475, height=80)
        act4_canvas.place(x=70, y=380)
        act4_canvas.create_text(40, 20, text="Activity 4") 
        
        #Membuat act5 inside side kiri
        act5_canvas = tk.Canvas(self, bg="WHITE")
        act5_canvas.config(width=475, height=80)
        act5_canvas.place(x=70, y=480)
        act5_canvas.create_text(40, 20, text="Activity 5") 

        #Membuat side kanan
        right_canvas = tk.Canvas(self, bg="BLUE")
        right_canvas.config(width=550, height=550)
        right_canvas.place(x=680, y=60)

        #Membuat current activites inside side kanan
        current_canvas = tk.Canvas(self, bg="WHITE")
        current_canvas.config(width=475, height=400)
        current_canvas.place(x=715, y=80)
        current_canvas.create_text(60, 20, text="Current Activities")

        #Menuliskan 3 current activites
        curr_act_label = tk.Label(self, text=show_top3_act())
        curr_act_label.place(x=800, y=120)

        #Membuat button See My Activity
        see_my_act_button = tk.Button(self, text="See My Activity", bg="WHITE", command=all_activity_page)
        see_my_act_button.config(width=15, height=3)
        see_my_act_button.place(x=1050, y=400)

        #Membuat button add new activity
        add_act_button = tk.Button(self, text="Add new activity", bg="WHITE", command=add_activity_page)
        add_act_button.config(width=67, height=4)
        add_act_button.place(x=715, y=500)



#Database
#Create or connect database activity
conn = sqlite3.connect('activity.db')

#Create cursor
c = conn.cursor()

#Create table activity
c.execute("""
CREATE TABLE IF NOT EXISTS activity (
    activityId integer PRIMARY KEY,
    activityName text,
    activityDetail text,
    timestamp text
)
""")

# c.execute("DELETE FROM activity")

#Commit changes
conn.commit()

#Close connection
conn.close()

#Create add_activity function
def add_activity(no_act):
    #Create or connect database activity
    conn = sqlite3.connect('activity.db')

    #Create cursor
    c = conn.cursor()

    #Menghitung jumlah record
    c.execute("SELECT COUNT(*) from activity")
    num_row = c.fetchone()[0]

    #Mendapatkan waktu
    now = datetime.now()
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")

    #Insert into table
    c.execute("INSERT INTO activity VALUES (:act_id, :act_name, :act_detail, :timestamp)",
    {
        'act_id': num_row,
        'act_name': activity_list()[no_act][0],
        'act_detail': activity_list()[no_act][1],
        'timestamp': now_string
    })

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

def add_activity1():
    add_activity(0)

def add_activity2():
    add_activity(1)

def add_activity3():
    add_activity(2)

def add_activity4():
    add_activity(3)

def add_activity5():
    add_activity(4)

def add_activity6():
    add_activity(5)

def add_activity7():
    add_activity(6)

def add_activity8():
    add_activity(7)

#Create add activity page
def add_activity_page():
    newWindow = Toplevel(app)
    newWindow.title("Add new activity")
    newWindow.geometry("390x510")
    
    #Add activity 1
    add_act1_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act1_canvas.config(width=350, height=50)
    add_act1_canvas.place(x=20, y=20)
    add_act1_canvas.create_text(40, 20, text=activity_list()[0][0])
    add_act1_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity1)
    add_act1_btn.config(width=3, height=2)
    add_act1_btn.place(x=300, y=27)

    #Add activity 2
    add_act2_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act2_canvas.config(width=350, height=50)
    add_act2_canvas.place(x=20, y=80)
    add_act2_canvas.create_text(40, 20, text=activity_list()[1][0])
    add_act2_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity2)
    add_act2_btn.config(width=3, height=2)
    add_act2_btn.place(x=300, y=87)

    #Add activity 3
    add_act3_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act3_canvas.config(width=350, height=50)
    add_act3_canvas.place(x=20, y=140)
    add_act3_canvas.create_text(40, 20, text=activity_list()[2][0])
    add_act3_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity3)
    add_act3_btn.config(width=3, height=2)
    add_act3_btn.place(x=300, y=147)

    #Add activity 4
    add_act4_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act4_canvas.config(width=350, height=50)
    add_act4_canvas.place(x=20, y=200)
    add_act4_canvas.create_text(40, 20, text=activity_list()[3][0])
    add_act4_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity4)
    add_act4_btn.config(width=3, height=2)
    add_act4_btn.place(x=300, y=207)

    #Add activity 5
    add_act5_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act5_canvas.config(width=350, height=50)
    add_act5_canvas.place(x=20, y=260)
    add_act5_canvas.create_text(40, 20, text=activity_list()[4][0])
    add_act5_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity5)
    add_act5_btn.config(width=3, height=2)
    add_act5_btn.place(x=300, y=267)

    #Add activity 6
    add_act6_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act6_canvas.config(width=350, height=50)
    add_act6_canvas.place(x=20, y=320)
    add_act6_canvas.create_text(40, 20, text=activity_list()[5][0])
    add_act6_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity6)
    add_act6_btn.config(width=3, height=2)
    add_act6_btn.place(x=300, y=327)

    #Add activity 7
    add_act7_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act7_canvas.config(width=350, height=50)
    add_act7_canvas.place(x=20, y=380)
    add_act7_canvas.create_text(40, 20, text=activity_list()[6][0])
    add_act7_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity7)
    add_act7_btn.config(width=3, height=2)
    add_act7_btn.place(x=300, y=387)

    #Add activity 8
    add_act8_canvas = tk.Canvas(newWindow, bg="WHITE")
    add_act8_canvas.config(width=350, height=50)
    add_act8_canvas.place(x=20, y=440)
    add_act8_canvas.create_text(40, 20, text=activity_list()[7][0])
    add_act8_btn = tk.Button(newWindow, bg="YELLOW", text="+", command=add_activity8)
    add_act8_btn.config(width=3, height=2)
    add_act8_btn.place(x=300, y=447)

#Create show all activity page
def all_activity_page():
    newWindow = Toplevel(app)
    newWindow.title("See my activity")
    newWindow.geometry("390x510")

    label = tk.Label(newWindow, text=show_all_act())
    label.place(x=10, y=10)


#Show 3 current activities
def show_top3_act():
    #Create or connect database activity
    conn = sqlite3.connect('activity.db')

    #Create cursor
    c = conn.cursor()

    #Menghitung jumlah record
    c.execute("SELECT COUNT(*) from activity")
    num_row = c.fetchone()[0]

    #Mendapatkan 3 aktivitas terakhir
    if (num_row <= 3):
        c.execute("SELECT * from activity")
    else:
        start_row = num_row-2
        c.execute("SELECT * from activity ORDER BY activityId desc LIMIT 3")


    records = c.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record[0]) + " " + record[1] + " " + record[3] + "\n"

    return print_record

#Show all my activities
def show_all_act():
    #Create or connect database activity
    conn = sqlite3.connect('activity.db')

    #Create cursor
    c = conn.cursor()

    #Mendapatkan semua aktivitas
    c.execute("SELECT * from activity ORDER BY activityId")

    records = c.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record[0]) + " " + record[1] + " " + record[3] + "\n"

    return print_record

#Main program
app = Application()

app.mainloop()