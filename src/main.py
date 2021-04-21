import tkinter as tk
from Frontend.Components.Activity import ActivityPage
from Frontend.Components.Chatroom.ChatroomConsultPage import ChatroomConsultPage as ConsultPage
from Frontend.Components.Friend import FriendPage
from Frontend.Components.Mood import MoodPage
class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #Creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 720)
        window.grid_columnconfigure(0, minsize = 1280)

        menu = tk.Menu(self)
        self.config(menu=menu)
        filemenu = tk.Menu(self)
        menu.add_cascade(label='Menu', menu=filemenu)
        filemenu.add_command(label='Activity', command = lambda : self.show_frame(ActivityPage))
        filemenu.add_command(label='Consult', command = lambda : self.show_frame(ConsultPage))
        filemenu.add_command(label='Friend', command = lambda : self.show_frame(FriendPage))
        filemenu.add_command(label='Mood', command = lambda : self.show_frame(MoodPage))

        self.frames = {}

        for F in (ActivityPage, ConsultPage, FriendPage, MoodPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")       
            
        self.show_frame(FriendPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.mainloop()