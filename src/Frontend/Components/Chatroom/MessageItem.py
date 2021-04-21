import tkinter as tk
from tkinter import * 

class MessageItem(tk.Frame) : 
    def __init__(
        self, parent,
        content = "", 
        timestamp = "", 
        username = "Anonym"):
        tk.Frame.__init__(self, parent)

        # Initiation
        self.username = Label(self, text=username)
        self.content = Label(self, text=content)
        self.timestamp = Label(self, text=timestamp)

        # Arranging the fields
        self.username.grid(row=0, padx=2, pady=2, sticky = "EW")
        self.content.grid(row=1, column=0, columnspan=3, padx=5, pady=2, sticky = "W")
        self.timestamp.grid(row=1, column=4, padx=2, pady=2, sticky = "E")

        # self.username.grid(row=0, column=0, padx=2, pady=2, sticky = "W")
        # self.content.grid(row=0, column=1, columnspan=2, padx=5, pady=2, sticky = "W")
        # self.timestamp.grid(row=0, column=4 , padx=2, pady=2, sticky = "W")
