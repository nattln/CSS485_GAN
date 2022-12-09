from tkinter import *

def addtolist():
    global List

    List = []
    for item in varList:
        if item.get() != "":
            List.append(item.get())
    print(List)

# --- main ---
List = []
varList = []

root = Tk()
root.title('Face Generation')
root.geometry("700x500")

window = Label(root, text='Choose Your Feature', font="50")
window.pack()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

f1 = Checkbutton(root, text="1", variable=var1, onvalue="f1", offvalue="0", height=2, width=10)
f2 = Checkbutton(root, text="2", variable=var2, onvalue="f2", offvalue="0", height=2, width=10)
f3 = Checkbutton(root, text="3", variable=var3, onvalue="f3", offvalue="0", height=2, width=10)
f4 = Checkbutton(root, text="4", variable=var4, onvalue="f4", offvalue="0", height=2, width=10)
f1.pack()
f2.pack()
f3.pack()
f4.pack()

varList.append(var1)
varList.append(var2)
varList.append(var3)
varList.append(var4)

b1 = Button(root, text="Confirm", command=addtolist)
b1.pack()

mainloop()