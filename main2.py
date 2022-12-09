import tkinter as tk

def add_list():
    global hlist
    hlist = []
    
    for item in varList:
        if item.get() != "":
            hlist.append(item.get())
    print(hlist)

def add_plist():
    global plist
    plist = []
    
    for item in varList:
        if item.get() != "":
            plist.append(item.get())
    print(plist)

def add_alist():
    global alist
    alist = []
    
    for item in varList:
        if item.get() != "":
            alist.append(item.get())
    print(alist)

def feature_command():
    return

# --- main ---

master = tk.Tk()
master.title('Face Generation')
master.geometry("800x500")


tk.Label(master,text="Choose your feature:").grid(row=0)
tk.Label(master,text="1) Hair :").grid(row=3)
tk.Label(master,text="2) Pose :").grid(row=6)
tk.Label(master,text="3) Age :").grid(row=9)

h1 = tk.Entry(master, width=5)
h2 = tk.Entry(master, width=5)
h3 = tk.Entry(master, width=5)
p1 = tk.Entry(master, width=5)
p2 = tk.Entry(master, width=5)
p3 = tk.Entry(master, width=5)
a1 = tk.Entry(master, width=5)

tk.Label(master,text="R").grid(row=2,column=1)
tk.Label(master,text="G").grid(row=2,column=2)
tk.Label(master,text="B").grid(row=2,column=3)
h1.grid(row=3, column=1)
h2.grid(row=3, column=2)
h3.grid(row=3, column=3)

tk.Label(master,text="Yaw").grid(row=5,column=1)
tk.Label(master,text="Pitch").grid(row=5,column=2)
tk.Label(master,text="Roll").grid(row=5,column=3)
p1.grid(row=6, column=1)
p2.grid(row=6, column=2)
p3.grid(row=6, column=3)

tk.Label(master,text="Age").grid(row=8,column=1)
a1.grid(row=9, column=1)

button1 = tk.Button(master, text='Confirm', command=feature_command()).grid(column=2,pady=30)#, sticky=tk.W, pady=4)


tk.mainloop()
