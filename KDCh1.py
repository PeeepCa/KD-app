import tkinter as Tk
import PIL.ImageGrab

window = Tk.Tk()
window.title("KD")
window.geometry("1920x1080")
c = Tk.Canvas(window, width=1920, height=1080)

def stul(x,y,pocet_mist,orientace,tablen):
    def chair(ch,xa,ya,xb,yb):
        def clicked(*args):
            current_color = c.itemcget(ch, 'fill')
            if current_color == 'white':
                c.itemconfig(ch, fill='yellow')
            elif current_color == 'yellow':
                c.itemconfig(ch, fill='green')
            else:
                c.itemconfig(ch, fill='white')

        ch = c.create_rectangle(xa,ya,xb,yb,tags=ch)
        c.itemconfig(ch, fill='white')

        c.tag_bind(ch,"<Button-1>",clicked)
        c.pack()
    def stul(ch,cht,xa,ya,xb,yb,lblx,lbly,lbl):
        ch = c.create_rectangle(xa,ya,xb,yb,tags=ch)
        cht = c.create_text(lblx,lbly, text=lbl, font=('Ariel', 8), fill='blue',tags=ch)
        c.itemconfig(ch, fill='white')
        c.pack()
    if orientace == 'h':
        if pocet_mist == 10:
            chair('ch1',x,y+30,x+20,y+50) ##OK
            chair('ch2',x+20,y,x+40,y+20) ##OK
            chair('ch3',x+40,y,x+60,y+20) ##OK
            chair('ch4',x+60,y,x+80,y+20) ##OK
            chair('ch5',x+80,y,x+100,y+20) ##OK
            chair('ch6',x+100,y+30,x+120,y+50) ##OK
            chair('ch7',x+20,y+60,x+40,y+80) ##OK
            chair('ch8',x+40,y+60,x+60,y+80) ##OK
            chair('ch9',x+60,y+60,x+80,y+80) ##OK
            chair('ch10',x+80,y+60,x+100,y+80) ##OK
            stul('s1','st1',x+20,y+20,x+100,y+60,x+60,y+40,tablen) ##OK
        elif pocet_mist == 9:
            chair('ch1',x,y+30,x+20,y+50) ##OK
            chair('ch2',x+20,y,x+40,y+20) ##OK
            chair('ch3',x+40,y,x+60,y+20) ##OK
            chair('ch4',x+60,y,x+80,y+20) ##OK
            chair('ch5',x+80,y,x+100,y+20) ##OK
            chair('ch6',x+20,y+60,x+40,y+80) ##OK
            chair('ch7',x+40,y+60,x+60,y+80) ##OK
            chair('ch8',x+60,y+60,x+80,y+80) ##OK
            chair('ch9',x+80,y+60,x+100,y+80) ##OK
            stul('s1','st1',x+20,y+20,x+100,y+60,x+60,y+40,tablen) ##OK
        else:
            chair('ch1',x,y+30,x+20,y+50) ##OK
            chair('ch2',x+30,y,x+50,y+20) ##OK
            chair('ch3',x+60,y+30,x+80,y+50) ##OK
            chair('ch4',x+30,y+60,x+50,y+80) ##OK
            stul('s1','st1',x+20,y+20,x+60,y+60,x+40,y+40,tablen) ##OK
    else:
        if pocet_mist == 10:
            chair('ch1',x+30,y,x+50,y+20) ##OK
            chair('ch2',x,y+20,x+20,y+40) ##OK
            chair('ch3',x,y+40,x+20,y+60) ##OK
            chair('ch4',x,y+60,x+20,y+80) ##OK
            chair('ch5',x,y+80,x+20,y+100) ##OK
            chair('ch6',x+60,y+20,x+80,y+40) ##OK
            chair('ch7',x+60,y+40,x+80,y+60) ##OK
            chair('ch8',x+60,y+60,x+80,y+80) ##OK
            chair('ch9',x+60,y+80,x+80,y+100) ##OK
            chair('ch10',x+30,y+100,x+50,y+120) ##OK
            stul('s1','st1',x+20,y+20,x+60,y+100,x+40,y+60,tablen) ##OK
        elif pocet_mist == 9:
            chair('ch1',x+30,y,x+50,y+20) ##OK
            chair('ch2',x,y+20,x+20,y+40) ##OK
            chair('ch3',x,y+40,x+20,y+60) ##OK
            chair('ch4',x,y+60,x+20,y+80) ##OK
            chair('ch5',x,y+80,x+20,y+100) ##OK
            chair('ch6',x+60,y+20,x+80,y+40) ##OK
            chair('ch7',x+60,y+40,x+80,y+60) ##OK
            chair('ch8',x+60,y+60,x+80,y+80) ##OK
            chair('ch9',x+60,y+80,x+80,y+100) ##OK
            stul('s1','st1',x+20,y+20,x+60,y+100,x+40,y+60,tablen) ##OK
        else:
            chair('ch1',x,y+30,x+20,y+50) ##OK
            chair('ch2',x+30,y,x+50,y+20) ##OK
            chair('ch3',x+60,y+30,x+80,y+50) ##OK
            chair('ch4',x+30,y+60,x+50,y+80) ##OK
            stul('s1','st1',x+20,y+20,x+60,y+60,x+40,y+40,tablen) ##OK

def screenshot():
    im = PIL.ImageGrab.grab()
    im.show()

class GUI:
    def hlavni_sal():
        c.delete("all")
        stul(10,10,10,'h','1')
        stul(140,10,10,'v','3')
        stul(10,100,9,'h','2')
        stul(140,140,9,'v','4')
        stul(240,10,4,'h','5')
        stul(240,100,4,'v','6')
    def kino():
        c.delete("all")
        stul(240,10,4,'h','5')
        stul(240,100,4,'v','6') 
    
    B = Tk.Button(window , text = "Send" , command = screenshot , width = 10)
    B.place(x=500, y=115)
    B = Tk.Button(window , text = "sal" , command = hlavni_sal , width = 10)
    B.place(x=500, y=185)
    B = Tk.Button(window , text = "kino" , command = kino , width = 10)
    B.place(x=500, y=225)

window.mainloop()
