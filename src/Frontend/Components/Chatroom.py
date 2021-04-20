import tkinter as tk
from PIL import ImageTk, Image
class ActivityPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #Creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 720)
        window.grid_columnconfigure(0, minsize = 1280)

        self.frames = {}

        frame = ActivityPage(window, self)
        self.frames[ActivityPage] = frame
        frame.grid(row = 0, column = 0, sticky="nsew")        

        self.show_frame(ActivityPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()