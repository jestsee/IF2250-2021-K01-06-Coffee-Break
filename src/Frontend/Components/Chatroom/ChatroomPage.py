import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image

import time

# Locals 
from Frontend.typeDefs.Chatroom import Chatroom
from Frontend.Components.Chatroom.Message import Message

import Backend.chatroom as chatroom_db
import Backend.user as user_db

class ChatroomPage(tk.Frame):
    # Data Dummy 
    __firstUsername = "Eru"
    __secondUsername = "Bukan Eru"
    __firstUserId = 20
    __secondUserId = 10
    __currentChatroomId = "2e88cf26-afb9-4c8e-a057-7dbb0e5a34c0"
    __currentChatroom = Chatroom(__currentChatroomId, __firstUserId, __secondUserId)
    def __init__(self, parent, controller):
        currentRow = 0
        tk.Frame.__init__(self, parent)
        
        self.title = Label(self, text=f"Chatroom With : {self.__secondUsername}")
        
        self.chatWindow = Frame(self)
        self.displayMessages()
        
        self.messageBox = Entry(self, width = 50)
        senderId = IntVar(None, 1)
        self.sendMessageButton = Button(
            self, text="send", padx = 15, 
            command = lambda : self.sendMessage(
                senderId = ( self.__currentChatroom.getFirstUserId() 
                if senderId.get() == 1 
                else self.__currentChatroom.getSecondUserId()), 
                message = self.messageBox.get()))
        # self.sendMessageButton.bind("<Key>", self.enterSendMessage)
        self.deleteAllMessagesButton = Button(
            self, text="delete history", padx = 15, 
            command = lambda : self.deleteChatHistory())

        self.selectUser = Frame(self)
        Radiobutton(self.selectUser, text=self.__firstUsername, variable=senderId, value=1).pack(anchor=W)
        Radiobutton(self.selectUser, text=self.__secondUsername, variable=senderId, value=2).pack(anchor=W)
        
        # Arranging the widgets
        self.title.grid(row = 0, pady = 2)
        self.chatWindow.grid(row = 1, columnspan = 3, pady = 10, padx = 20, sticky="EW")
        self.messageBox.grid(row = 2, column = 0, pady = 10, padx = 20)
        self.sendMessageButton.grid(row = 2, column = 2, pady = 10, padx = 5)
        self.deleteAllMessagesButton.grid(row = 2, column = 3, pady = 10, padx = 5)
        self.selectUser.grid(row=3, columnspan = 2)
    
    def displayMessages(self) :
        '''Display messages that are saved in the local to the screen'''
        Messages = self.__currentChatroom.getMessages()
        self.chatWindow.destroy()
        self.chatWindow = tk.Frame(self)
        self.chatWindow.grid(
            row = 1, columnspan = 2, 
            pady = 10, padx = 20, 
            ipadx = 20
        )

        # Dapat digunakan pada program final 
        # firstUsername = user_db.getUsername(self.__currentChatroom.getFirstUserId())
        # secondUsername = user_db.getUsername(self.__currentChatroom.getSecondUserId())

        firstUsername = "Eru"
        secondUsername = "Bukan Eru"
        for idx, newMessage in enumerate(Messages) :
            isCurrentUser = newMessage[4] == self.__currentChatroom.getFirstUserId() 
            message = Message(
                self.chatWindow,
                content = newMessage[1],
                timestamp = newMessage[2][11:16],
                username = (firstUsername
                    if isCurrentUser
                    else secondUsername))
            # message.grid(sticky = "W" if isCurrentUser else "E", padx = 5)
            message.grid(column = 0 if isCurrentUser else 1)

    def deleteChatHistory(self) :
        chatroom_db.clearChatroomMessages(self.__currentChatroom.getChatroomId())
        Messages = chatroom_db.fetchMessages(self.__currentChatroomId)
        self.__currentChatroom.setMessages(Messages)
        self.displayMessages()

    def enterSendMessage(self, event) :
        print(event.char)
        # if(event.keysys == "Enter") : 
        #     self.sendMessage(self.messageBox.get())

    def sendMessage(self, senderId, message) : 
        if(type(message) != str) : 
            raise ValueError("Invalid type") 
        try : 
            if(message == "") : 
                raise ValueError("Message input cannot be an empty string")
            chatroom_db.sendMessage(self.__currentChatroomId, senderId, message)
            self.messageBox.delete(0, END)
            Messages = chatroom_db.fetchMessages(self.__currentChatroomId)
            self.__currentChatroom.setMessages(Messages)
            self.displayMessages()
        except ValueError : 
            print("Exception")
        

