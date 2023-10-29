import tkinter
import serial
import tkinter.font as tkFont
root=tkinter.Tk()
master=tkinter.Frame(root,width=600, height=500)
root.title("ROV Control")
root.geometry("600x500")
master.place(in_=root, anchor="c", relx=.5, rely=.5)
ser = serial.Serial('com5', 9600)
ser.write(bytes('l', 'UTF-8'))
def read():
    b = ser.readline()         
    string_n = b.decode()  
    string = string_n.rstrip()
    label5["text"]=string
    master.after(1000, read)

def up():
    label4["text"]="UP"
    ser.write(bytes('h', 'UTF-8'))
    
def down():
    label4["text"]="DOWN"
    ser.write(bytes('l', 'UTF-8'))
   
def fwd():
    label4["text"]="FORWARD"
    ser.write(bytes('h', 'UTF-8'))
    

def bwd():
    label4["text"]="BACKWARD"
    ser.write(bytes('l', 'UTF-8'))
    

def lft():
    label4["text"]="LEFT"
    ser.write(bytes('l', 'UTF-8'))
    
def rgt():
    label4["text"]="RIGHT"
    ser.write(bytes('l', 'UTF-8'))
   
   

label4=tkinter.Label(master, text="Command", font=('Georgia 20 bold'))
label4.place(x=200,y=350,width=180,height=55)

label5=tkinter.Label(master, text="Response", font=('Georgia 20 bold'))
label5.place(x=200,y=430,width=180,height=55)


label1=tkinter.Label(master,text="ROV Control")
label1.place(x=220,y=30,width=146,height=30)
ft = tkFont.Font(family='Times',size=20)
label1["font"] = ft
label1["fg"] = "#333333"
label1["justify"] = "center"

button1=tkinter.Button(master, text="Level UP",command=up)
button1.place(x=40,y=190,width=100,height=50)
button1["bg"] = "#717171"
ft = tkFont.Font(family='Times',size=14)
button1["font"] = ft
button1["fg"] = "#90ee90"
button1["justify"] = "center"
button1["text"] = "Level UP"

button2=tkinter.Button(master, text="Level Down",command=down)
button2.place(x=40,y=280,width=100,height=50)
button2["bg"] = "#717171"
ft = tkFont.Font(family='Times',size=14)
button2["font"] = ft
button2["fg"] = "#90ee90"
button2["justify"] = "center"
button2["text"] = "Level Down"

button3=tkinter.Button(master, text="Forward",command=fwd)
button3.place(x=360,y=180,width=100,height=50)
button3["bg"] = "#717171"
ft = tkFont.Font(family='Times',size=14)
button3["font"] = ft
button3["fg"] = "#90ee90"
button3["justify"] = "center"
button3["text"] = "Forward"

button4=tkinter.Button(master, text="Backward",command=bwd)
button4.place(x=360,y=280,width=100,height=50)
button4["bg"] = "#717171"
ft = tkFont.Font(family='Times',size=14)
button4["font"] = ft
button4["fg"] = "#90ee90"
button4["justify"] = "center"
button4["text"] = "Backward"

button5=tkinter.Button(master, text="Left",command=lft)
button5.place(x=260,y=230,width=100,height=50)
button5["bg"] = "#717171"
ft = tkFont.Font(family='Times',size=14)
button5["font"] = ft
button5["fg"] = "#90ee90"
button5["justify"] = "center"
button5["text"] = "Left"

button6=tkinter.Button(master, text="Right",command=rgt)
button6.place(x=460,y=230,width=100,height=50)
button6["bg"] = "#717171"
ft = tkFont.Font(family='Times',size=14)
button6["font"] = ft
button6["fg"] = "#90ee90"
button6["justify"] = "center"
button6["text"] = "Right"

label2=tkinter.Label(master, text="Depth Control")
label2.place(x=20,y=130,width=136,height=37)
ft = tkFont.Font(family='Times',size=16)
label2["font"] = ft
label2["fg"] = "#333333"
label2["justify"] = "center"
label2["text"] = "Depth Control"

label3=tkinter.Label(master, text="Direction Control")
label3.place(x=330,y=110,width=165,height=67)
ft = tkFont.Font(family='Times',size=16)
label3["font"] = ft
label3["fg"] = "#333333"
label3["justify"] = "center"
label3["text"] = "Direction Control"

root.bind('8',lambda event:up())
root.bind('2',lambda event:down())
root.bind('w',lambda event:fwd())
root.bind('s',lambda event:bwd())
root.bind('a',lambda event:lft())
root.bind('d',lambda event:rgt())

read()
master.mainloop()
