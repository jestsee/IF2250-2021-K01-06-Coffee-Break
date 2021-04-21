import tkinter as tk
from tkinter import * 

# Local Imports 
from Frontend.Components.Chatroom.ChatroomPage import ChatroomPage

class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #Creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 720)
        window.grid_columnconfigure(0, minsize = 1280)

        self.frames = {}

        frame = ChatroomPage(window, self)
        self.frames[ChatroomPage] = frame
        frame.grid(row = 0, column = 0, sticky="nsew")        

        self.show_frame(ChatroomPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

#Main program
app = Application()
app.mainloop()