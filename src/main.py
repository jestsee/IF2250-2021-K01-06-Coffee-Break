import tkinter as tk
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