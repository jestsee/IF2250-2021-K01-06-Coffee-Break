# friend_gui.py
import sys
import os.path
sys.path.insert(0, r'..\Frontend\typeDefs')
sys.path.insert(0, r'..\Frontend\typeDefs')
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
sys.path.insert(1, '../typeDefs')
import Frontend.typeDefs.User as u 
from Backend.user import *
from tkinter import *

class FriendPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # initialize
        self.res = []
        self.friendl = []

        #setting window size
        # width=1280
        # height=720
        # screenwidth = root.winfo_screenwidth()
        # screenheight = root.winfo_screenheight()
        # alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # root.geometry(alignstr)
        # root.resizable(width=False, height=False)

        # search friend text
        search_label=tk.Label(self)
        search_label["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=24)
        search_label["font"] = ft
        search_label["fg"] = "#333333"
        search_label["justify"] = "center"
        search_label["text"] = "Search Friend"
        search_label.place(x=10,y=40,width=232,height=47)

        # display search result
        self.searchresult=tk.Listbox(self)
        self.searchresult["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=12)
        self.searchresult["font"] = ft
        self.searchresult["fg"] = "#333333"
        # self.searchresult["justify"] = "center"
        self.searchresult.place(x=50,y=90,width=480,height=533)

        # searchbox to input search query
        self.searchbox=tk.Entry(self) # cara get entry : searchbox.get()
        self.searchbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.searchbox["font"] = ft
        self.searchbox["fg"] = "#333333"
        self.searchbox["justify"] = "center"
        self.searchbox["text"] = "type 'all' to see all users . ."
        self.searchbox.place(x=230,y=40,width=225,height=40)
        
        # submit search query button
        searchbutton=tk.Button(self)
        searchbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        searchbutton["font"] = ft
        searchbutton["fg"] = "#000000"
        searchbutton["justify"] = "center"
        searchbutton["text"] = "go"
        searchbutton.place(x=470,y=40,width=58,height=40)
        searchbutton["command"] = self.searchbutton_command

        # add friend button
        addfriendbutton=tk.Button(self)
        addfriendbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        addfriendbutton["font"] = ft
        addfriendbutton["fg"] = "#000000"
        addfriendbutton["justify"] = "center"
        addfriendbutton["text"] = "Add Friend"
        addfriendbutton.place(x=50,y=630,width=230,height=40)
        addfriendbutton["command"] = self.addfriendbutton_command

        # chat button
        chatbutton=tk.Button(self)
        chatbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        chatbutton["font"] = ft
        chatbutton["fg"] = "#000000"
        chatbutton["justify"] = "center"
        chatbutton["text"] = "Chat"
        chatbutton.place(x=300,y=630,width=230,height=40)
        chatbutton["command"] = self.chatbutton_command

        # my friend text
        myfriend=tk.Label(self, anchor="w")
        myfriend["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=24)
        myfriend["font"] = ft
        myfriend["fg"] = "#333333"
        myfriend["justify"] = "center"
        myfriend["text"] = "My Friend"
        myfriend.place(x=550,y=40,width=232,height=47)

        # friend list
        self.friendlist=tk.Listbox(self)
        self.friendlist["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.friendlist["font"] = ft
        self.friendlist["fg"] = "#333333"
        self.friendlist["justify"] = "center"
        self.friendlist.place(x=550,y=90,width=180,height=476)
        # fill friend list box by default
        self.refresh_friendlist()
        #print(self.friendl)

        # chat friend button
        self.chatfriendbutton=tk.Button(self)
        self.chatfriendbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        self.chatfriendbutton["font"] = ft
        self.chatfriendbutton["fg"] = "#000000"
        self.chatfriendbutton["justify"] = "center"
        self.chatfriendbutton["text"] = "chat friend"
        self.chatfriendbutton.place(x=550,y=580,width=180,height=40)
        self.chatfriendbutton["command"] = self.chatfriendbutton_command

        # delete friend button
        self.deletefriendbutton=tk.Button(self)
        self.deletefriendbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        self.deletefriendbutton["font"] = ft
        self.deletefriendbutton["fg"] = "#000000"
        self.deletefriendbutton["justify"] = "center"
        self.deletefriendbutton["text"] = "delete friend"
        self.deletefriendbutton.place(x=550,y=630,width=180,height=40)
        self.deletefriendbutton["command"] = self.deletefriendbutton_command

        # my friend text
        self.chat=tk.Label(self, anchor="w")
        self.chat["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=24)
        self.chat["font"] = ft
        self.chat["fg"] = "#333333"
        self.chat["justify"] = "center"
        self.chat["text"] = "Chatroom"
        self.hide(self.chat)

        # chatroom box
        self.chatroom=tk.Listbox(self)
        self.chatroom["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.chatroom["font"] = ft
        self.chatroom["fg"] = "#333333"
        # self.chatroom["justify"] = "center"
        self.hide(self.chatroom)

        # input message box
        self.messagebox=tk.Entry(self)
        self.messagebox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.messagebox["font"] = ft
        self.messagebox["fg"] = "#333333"
        self.messagebox["justify"] = "center"
        self.messagebox["text"] = "type here . . ."
        self.hide(self.messagebox)
        
        # send message button
        self.sendbutton=tk.Button(self)
        self.sendbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        self.sendbutton["font"] = ft
        self.sendbutton["fg"] = "#000000"
        self.sendbutton["justify"] = "center"
        self.sendbutton["text"] = "send"
        self.hide(self.sendbutton)
        self.sendbutton["command"] = self.sendbutton_command

    # message related
    def show_mtool(self):
        self.sendbutton.place(x=1128,y=630,width=103,height=40)
        self.messagebox.place(x=750,y=630,width=369,height=40)
        self.chatroom.place(x=750,y=90,width=480,height=533)
        self.chat.place(x=750,y=40,width=232,height=47)

    # display search result when clicked
    def searchbutton_command(self):
        # reset result
        self.searchresult.delete(0,"end")
        self.res = []
        # get query
        query = self.searchbox.get()
        for user in get_user_by_all(query):
            self.res.append(user)
            self.searchresult.insert("end",user)

        if(query=="all" or query =="All"):
            for user in get_users():
                self.res.append(user)
                self.searchresult.insert("end",user)
        elif(len(get_user_by_all(query))==0):
            # show pop up message
            tkinter.messagebox.showinfo("Error","User not found")
        self.searchbox.delete(0, tk.END)

    def addfriendbutton_command(self):
        index = self.searchresult.curselection()
        if(len(index)!=0):
            
            # print(self.res[index[0]])
            myid = 2 # misal id user nya 2
            friendid = u.get_id(self.res[index[0]])
            if(u.add_friend(myid, friendid)==-99):
                tkinter.messagebox.showinfo("Error","Kamu tidak bisa menambahkan teman yang sudah ada")
            self.friendlist.delete(0,"end")
            # update friendlist box
            #self.friendlist.insert("end",self.res[index[0]])
            #self.friendl.append(self.res[index[0]])
            self.refresh_friendlist()
            print(self.friendl)

        else:
            tkinter.messagebox.showinfo("Error","Kamu belum memilih teman untuk ditambahkan")

    def deletefriendbutton_command(self):
        try:
            index = self.friendlist.curselection()
            print(self.friendl[index[0]])
            frenid = u.get_id(self.friendl[index[0]])
            print(u.delete_friend(2,frenid))
            self.friendlist.delete((index))
            self.refresh_friendlist()
        except IndexError:
            index = -99
            tkinter.messagebox.showinfo("Error","Kamu belum memilih teman untuk dihapus")

    def refresh_friendlist(self):
        self.friendlist.delete(0,"end")
        self.friendl=[]
        for user in get_friends(2):
            self.friendl.append(user)
            self.friendlist.insert("end",user.nama)

    def chatfriendbutton_command(self):
        self.show_mtool()
        self.chatroom.delete(0,"end")
        try:
            index = self.friendlist.curselection()
            print(self.friendl[index[0]])
            self.chatroom.insert("end","  memulai obrolan dengan "+self.friendl[index[0]].nama+" . . .")
        except IndexError:
            index = -99
            self.chatroom.insert("end","  Kamu belum memilih teman untuk diajak chatting")

    def chatbutton_command(self):
        self.show_mtool()
        index = -99
        self.chatroom.delete(0,"end")
        try:
            index = self.searchresult.curselection()
            print(index[0])
            self.chatroom.insert("end","  memulai obrolan dengan "+self.res[index[0]].nama+" . . .")
        except IndexError:
            index = -99
            self.chatroom.insert("end","  Kamu belum memilih teman untuk diajak chatting")

    def sendbutton_command(self):
        self.chatroom.insert("end"," me : "+self.messagebox.get())
        self.messagebox.delete(0, tk.END)
        
    def hide(self, item):
        item.place_forget()

class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #Creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 720)
        window.grid_columnconfigure(0, minsize = 1280)

        self.frames = {}

        frame = FriendPage(window, self)
        self.frames[FriendPage] = frame
        frame.grid(row = 0, column = 0, sticky="nsew")        

        self.show_frame(FriendPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
