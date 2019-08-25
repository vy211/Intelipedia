from tkinter import *
import os
from tkinter import messagebox
import wolframalpha
import pyttsx3

client = wolframalpha.Client('TV3KA5-7RRG64WVKQ')
engine = pyttsx3.init()
engine.setProperty('rate',150)
root = Tk()
root.geometry('800x200')
root.title("Intelipedia by Vipin Yadav")
label_1 = Label(root, text="Question:", width=20, font=("bold", 15))
label_1.place(x=10, y=50)
# label_2 = Label(root, text="Answer:",width=20,font=("bold", 15))
# label_2.place(x=10,y=100)
entry_1 = Entry(root, bd=3, width=40, font=('bold', 15))
entry_1.place(x=190, y=50)
entry_1.focus_set()



# entry_2 = Entry(root,bd=3,width=40,font=('bold',15))
# entry_2.place(x=190,y=100)
def txt():
    try:
        res = client.query(entry_1.get())
        output = next(res.results).text
        messagebox.showinfo("Answer:", output)
    except:
        messagebox.showinfo("Answer:", "Sorry!\nTry Another Question")


def spe():
    try:
        res = client.query(entry_1.get())
        output = next(res.results).text
        engine.say(output)
        engine.runAndWait()
    except:
        engine.say("Sorry, try another question answer not define!")
        engine.runAndWait();


def ts():
    try:
        res = client.query(entry_1.get())
        output = next(res.results).text
        print(output)
        engine.say(output)
        engine.runAndWait()
        messagebox.showinfo("Answer:", output)
    except:
        engine.say("Sorry, try another question answer not define!")
        engine.runAndWait();
        messagebox.showinfo("Answer:", "Sorry!\nTry another question!")



Button(root, text='Text', width=20, bg='brown', fg='white', command=txt).place(x=50, y=150)
Button(root, text='Text & Voice', width=20, bg='brown', fg='white', command=ts).place(x=310, y=150)
Button(root, text='Voice', width=20, bg='brown', fg='white', command=spe).place(x=560, y=150)

root.mainloop()

