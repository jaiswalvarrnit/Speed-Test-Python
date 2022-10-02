from tkinter import *
from PIL import Image
from PIL import ImageTk
import speedtest

def checkSpeed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + "Mbps"
    up = str(round(sp.upload()/(10**6), 3)) + "Mbps" 
    lab_down.config(text=down)
    lab_up.config(text=up)


st = Tk() # st stands for speedtest
st.title("Internet Speed Test")
st.geometry("500x800")
st.config(bg="#0b0c1b")

lab = Label(st, text="Internet Speed Test", font = ("Times New Roman", 30, "bold"))
lab.place(x = 60, y= 250, height=50 , width= 380)

lab = Label(st, text="Download Speed ", font = ("Times New Roman", 30, "bold"))
lab.place(x = 60, y= 330, height=50 , width= 380)

lab_down = Label(st, text="00", font = ("Times New Roman", 30, "bold"))
lab_down.place(x = 60, y= 400, height=50 , width= 380)

lab = Label(st, text="Upload Speed", font = ("Times New Roman", 30, "bold"))
lab.place(x = 60, y= 490, height=50 , width= 380)

lab_up = Label(st, text="00", font = ("Times New Roman", 30, "bold"))
lab_up.place(x = 60, y= 560, height=50 , width= 380)

go_but = ImageTk.PhotoImage(Image.open("C:\\Users\\geniu\\Desktop\\Projects\\SpeedTest\\go_button.png"))
my_but = Button(st,image = go_but, borderwidth= 0,command= checkSpeed)
my_but.pack()

st.mainloop()