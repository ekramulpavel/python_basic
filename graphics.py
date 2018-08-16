import tkinter
g = tkinter.Tk()
g.mainloop()


import tkinter
def hello():
    tkinter.messagebox.showinfo("say hello","hello world")
top = tkinter.Tk()
top.title("Techtunes")
lbl = tkinter.Label(top, text = "Techtunes")
m = tkinter.Canvas(top, bg="blue", height=250, width=300)
c = tkinter.Checkbutton(top, text = "Techtunes")
b = tkinter.Checkbutton(top, text = "Python")
d = tkinter.Button(top, text ="Techtunes")
s = tkinter.Spinbox(top, from_=0, to=10)
h = tkinter.Button(top, text = "Python Tutorial",command = hello)
e = tkinter.Entry(top)
r = tkinter.Radiobutton(top, text = "Python Tutorial", value = 1)
lbl.pack()
m.pack()
c.pack()
b.pack()
d.pack()
s.pack()
h.pack()
e.pack()
r.pack()
top.mainloop()