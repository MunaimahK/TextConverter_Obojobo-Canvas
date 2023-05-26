# Munaimah Khan
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


def addFilesC_O():
    try:
        file1 = open(fd.askopenfilename(), "r")
    except FileNotFoundError:
        return
    try:
        file2 = open(fd.askopenfilename(), "w")
    except FileNotFoundError:
        return

    rep = {"[M]":"M = ", "[m]":"m = ","[v1]":"v_1 = ", "[v0]": "v_0 = ",
            "[h]": "h = ", "[k]":"k = ", "[L]":"L = ", "[m1]": "m_1 = ", "[m2]": "m_2 = ",
           "m/s":"\,\mathrm{m/s}" , "kg":"\,\mathrm{kg}", "meters": "\mathrm{m}", "N/m":"\,\mathrm{N/m}"}
    s = file1.read()
    for key in rep:
        s = s.replace(key, rep[key])
    file2.write(s)

    j = file1.read()
    for key in j:
        if(key.isnumeric()):
            j = ""
    file2.write(j)

def addFilesO_C():
    try:
        file1 = open(fd.askopenfilename(), "r")
    except FileNotFoundError:
        return
    try:
        file2 = open(fd.askopenfilename(), "w")
    except FileNotFoundError:
        return

    rep = {"M=": "[M]", "m=": "[m]", "v_1 =": "[v1]", "v_0 =": "[v0]", "h =": "[h]", "k = ": "[k]", "L =": "[L]",
           "m_1 = ": "[m1]", "m_2 = ": "[m2]","F_2=":"[F2]","F_B=":"[FB]","F_A=":"[FA]","F_B =":"[FB]","\\theta =":"[theta]","\\theta=":"[theta]","\theta=":"[theta]", "\\mu_s =":"[mu]", "\\mu_s=":"[mu]","\\;\\mathrm{N}":"N",
           "\,\mathrm{m/s}": "m/s", "\\;\\mathrm{m/s}": "m/s", "\\mathrm{m/s}": "m/s", "\,\mathrm{kg}": "kg", "\mathrm{kg}": "kg", "\,\mathrm{m}": "meters", "\,\mathrm{N/m}": "N/m",
           "\\;\\mathrm{kg}": "kg", "\\;\\mathrm{N}": "N", "\mathrm{N}": "N", "\\degree":"°"}
    s = file1.read()
    for key in rep:
        s = s.replace(key, rep[key])
    file2.write(s)

# This code has been developed based off the GeeksforGeeks code structure
# Not all credit fo the code is given to me or GeeksforGeeks
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(1, weight = 1)
        container.grid_columnconfigure(1, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 1, column = 1, sticky ="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        # label = ttk.Label(self, text ="Startpage", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        # label.grid(row = 2, column = 2)

        button1 = ttk.Button(self, text ="Obojobo -> Canvas",
        command = lambda : controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 200, pady = 30)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Canvas -> Obojobo",
        command = lambda : controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text ="1. Select file with Obojobo Text")
        label1.grid(row = 0, column = 2, padx = 10, pady = 10)
        label2 = ttk.Label(self, text ="2. Select destination file for Canvas Text")
        label2.grid(row = 1, column = 2, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Go Back",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Add Files", command = addFilesO_C)

        # putting the button in its place by
        # using grid
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text ="1. Select file with Canvas Text")
        label1.grid(row = 0, column = 2, padx = 10, pady = 10)
        label2 = ttk.Label(self, text ="2. Select destination file for Obojobo Text")
        label2.grid(row = 1, column = 2, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Add Files",
                            command = addFilesC_O)

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Go Back",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
