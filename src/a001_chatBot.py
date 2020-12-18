#Chatbot
#By: Hernie Jabien
#Copyright @ Syntaxer 2019 all rights reserved.

from tkinter import*
import time
userdata = []
db_data = {}
class Chatbot(Tk):
    def __init__(self, *arg, **args):
        Tk.__init__(self, *arg, **args)
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Splash, Home, Messenger):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Splash)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Splash(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        mframe = Frame(self, bg="#4343FF", height=400, width=300)
        mframe.pack(fill=BOTH, expand=True)
        br = Label(mframe, text="\n\n\n", bg="#4343FF")
        br.pack()
        logo = Label(mframe, text="B", fg="#ffffff", bg="#4343FF", font="Mono 50 bold")
        logo.pack()
        btn = Button(mframe, text="...", fg="#ffffff", bg="#4342FF", font="Mono 25 bold", command=lambda:controller.show_frame(Home))
        btn.pack()
        copyrights = Label(mframe, text="Chatbot by. Hernie Jabien\nCopyright @ Syntaxer 2019 all rights reserved.", fg="#ffffff", bg="#4343FF", font="Arial 8 italic")
        copyrights.pack(side=BOTTOM)


class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        mframe = Frame(self, bg="#ffffff", height=400, width=300)
        mframe.pack(fill=BOTH, expand=True)
        hframe = Frame(mframe, bg="#4343FF", height=100)
        hframe.pack(fill=X, side=TOP)
        logo = Label(hframe, text="Chat Bot", fg="#ffffff", bg="#4343FF", font="Mono 20 bold")
        logo.pack(side=LEFT)
        banner = Label(mframe, text="\n\nSign-up", fg="#1FAE00", bg="#ffffff", font="Mono 15 bold")
        banner.pack()
        br = Label(mframe, text="\nUsername\t	", bg="#ffffff", fg="#2B2B2B")
        br.pack()
        input1 = Entry(mframe, border="2", highlightbackground="#4342FF", fg="#2B2B2B", bg="#ffffff")
        input1.pack()
        br = Label(mframe, text="Bot name\t\t	", bg="#ffffff", fg="#2B2B2B")
        br.pack()
        input2 = Entry(mframe, border="2", highlightbackground="#4342FF", fg="#2B2B2B", bg="#ffffff")
        input2.pack()
        br = Label(mframe, text="", bg="#ffffff")
        br.pack()
        btn = Button(mframe, text="Confirm", highlightbackground="#4342FF", fg="#ffffff", bg="#4342FF", font="Mono 15 bold", width=11, command=lambda:self.Names(input1.get(), input2.get()))
        btn.pack()
        copyrights = Label(mframe, text="Chatbot by. Hernie Jabien\nCopyright @ Syntaxer 2019 all rights reserved.", fg="#ffffff", bg="#4343FF", font="Arial 8 italic")
        copyrights.pack(side=BOTTOM, fill=X)

    def Names(self, me, bot):
        if me and bot is not "":
            userdata.append(me)
            userdata.append(bot)
            self.controller.show_frame(Messenger)

class Messenger(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.stats = False
        self.counter = 0
        self.txt_bot = StringVar()
        self.txt_dot = StringVar()
        self.txt_stat = StringVar()
        self.txt_bot.set("")
        self.txt_dot.set("")
        self.txt_stat.set("Not connected to internet")
        mframe = Frame(self, bg="#ffffff", height=400, width=300)
        mframe.pack(fill=BOTH, expand=True)
        hframe = Frame(mframe, bg="#4343FF", height=100)
        hframe.pack(fill=X, side=TOP)
        fframe = Frame(mframe, bg="#4343FF", height=50)
        fframe.pack(fill=X, side=BOTTOM)
        logo = Label(hframe, textvariable=self.txt_dot, fg="#1FAE00", border="0", bg="#4343FF", font="Mono 20 bold")
        logo.pack(side=LEFT)
        name = Label(hframe, textvariable=self.txt_bot, fg="#ffffff", border="0", bg="#4343FF", font="Mono 15 bold")
        name.pack(side=LEFT)
        stats = Label(hframe, textvariable=self.txt_stat, fg="#ffffff", border="0", bg="#4343FF", font="Mono 10 bold")
        stats.pack(side=LEFT)
        refresh = Button(hframe, text="o", fg="#ffffff", border="0", bg="#4343FF", command=self.active)
        refresh.pack(side=RIGHT)
        self.input1 = Entry(fframe, bg="#ffffff", fg="#000000")
        self.input1.pack(side=LEFT, padx=(2,2), expand=True, fill=X)
        btn = Button(fframe, text="Send", fg="#ffffff", border="0", bg="#4343FF", command=lambda:self.send(userdata[0],self.input1.get()))
        btn.pack(side=RIGHT)
        self.lst = Listbox(mframe, bg="#ffffff", fg="#000000")
        self.lst.pack(expand=True, fill=BOTH)
        for i in range(18):
            self.lst.insert(END, "")


    def active(self):
        self.txt_bot.set(userdata[1])
        self.txt_dot.set("* ")
        self.txt_stat.set("")
        self.stats = True

    def send(self, sender, msg):
        bot = userdata[1]
        if self.stats and msg is not "":
            if "teach " in msg:
                msg = msg[6:len(msg)]
                db = open("db/chatbot.txt", "a+")
                db.write(msg)
                db.close()
                self.lst.insert(END, "System: Data added successfully.")
            elif "help" == msg:
                self.lst.insert(END, "System: Syntax~teach {message:response}")
            else:
                self.lst.insert(END, sender.upper() + ": "+ msg)
                respond = self.get_data(msg)
                if respond is not -1:
                    self.lst.insert(END, str(bot.upper()) + ": " + respond)
                else:
                    self.lst.insert(END, str(bot.upper()) + ": I don't understand you..")
        else:
            self.lst.insert(END, "System: Cannot communicate offline or you just send nothing.")
        self.input1.delete(0, END)
        self.lst.see(END)
        self.lst.see(END)


    def get_data(self, msg):
        response = ""
        db = open("db/chatbot.txt", "r+")
        tb = db.read()
        db.close()
        m = 0
        l = 0
        h = 0
        for a in range(len(tb)):
            for b in range(len(tb)):
                if l < len(tb) and h < len(tb) and m < len(tb):
                    if tb[l] == "{":
                        if tb[m] == ":":
                            if tb[h] == "}":
                                db_data[tb[l+1:m]] = tb[m+1:h]
                                l = m = h
                                h += 1
                            else:
                                h += 1
                        else:
                            m += 1
                    else:
                        l += 1
        if msg in tb:
            response = db_data[msg]
            return response
        else:
            return -1

app = Chatbot()
app.title("Chat Bot by. Hernie Jabien")
app.geometry("300x400")
app.resizable(0,0)
app.mainloop()
