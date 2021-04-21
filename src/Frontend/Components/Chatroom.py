import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image

import time

# Locals 
from Frontend.typeDefs.Chatroom import Chatroom
import Backend.chatroom as chatroom_db
class ChatroomPage(tk.Frame):
    __currentChatroomId = "194682b6-cac9-4b35-88f2-955a0519ed36"
    __currentChatroom = Chatroom(__currentChatroomId, 20, 10)
    def __init__(self, parent, controller):
        currentRow = 0
        tk.Frame.__init__(self, parent)
        self.width = 1000
        self.username = Label(self, text="username")
        
        self.username.grid(row = 0, sticky = "nsew", pady = 2)
        
        self.chatWindow = Text(self, height=10, padx = 10, pady = 5)
        self.chatWindow.grid(
            row = 1, columnspan = 2, 
            pady = 10, padx = 20, 
            ipadx = 20)
        # self.chatWindow.config(state=DISABLED)
        # chatWindow.place(relheight = 0.745,relwidth = 1,rely = 0.08)
        self.displayMessages()
        
        self.messageBox = Entry(self, width = 50)
        self.sendMessageButton = Button(self, text="send", padx = 15, command = lambda : self.sendMessage(self.messageBox.get()))
        
        self.messageBox.grid(row = 2, column = 0, pady = 10, padx = 20)
        self.sendMessageButton.grid(row = 2, column = 1, pady = 10, padx = 5)
    
    def displayMessages(self, check = False) :
        Messages = self.__currentChatroom.getMessages()
        self.chatWindow.delete("1.0","end")
        for idx, Message in enumerate(Messages) : 
            # if(idx == 0) : 
            #     self.chatWindow.insert(1.0, "")
            #     continue
            self.chatWindow.insert(INSERT, Message[1] + " " + Message[2] + "\n")

    def sendMessage(self, message) : 
        if(type(message) != str) : 
            raise ValueError("Invalid type") 
        try : 
            if(message == "") : 
                raise ValueError("Message input cannot be an empty string")
            chatroom_db.sendMessage(self.__currentChatroomId, message)
            self.messageBox.delete(0, END)
            Messages = chatroom_db.fetchMessages(self.__currentChatroomId)
            self.__currentChatroom.setMessages(Messages)
            self.displayMessages()
        except ValueError : 
            print("Exception")
        

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