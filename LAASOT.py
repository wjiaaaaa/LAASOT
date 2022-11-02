
import tkinter as tk
from astroquery.jplhorizons import Horizons
import tkinter.messagebox as msgbox

UTS = {'lon': 151.20109,'lat': -33.88379,'elevation': 0}

window = tk.Tk()
window.title('Welcome to scearching system')
window.geometry('700x420')


#star information
tk.Label(window,text='Object ID:').place(x=50,y=190)
var_star_num=tk.StringVar()
entry_star_num=tk.Entry(window,textvariable=var_star_num)
entry_star_num.place(x=120,y=190)

#image
frame = tk.Frame(window)
frame.place(x=130,y=20)
img = tk.PhotoImage(file='laasot.PNG')
label_img = tk.Label(frame,image=img)
label_img.pack()


def star_search():

    obj = Horizons(id=entry_star_num.get(), location=UTS, epochs=None)
    eph = obj.ephemerides()
    eph_print = eph['AZ','EL']
    name = eph['targetname']
    EL = eph['EL']
    Cnst = eph['constellation']

    frame = tk.Frame(window, width=100, height=100)
    frame.place(x=420,y=30)
    lab1 = tk.Label(frame,text='Azimuth and Elevation:',font=('Arial','15','bold'),bg='yellow')
    lab2 = tk.Label(frame,text=eph_print)
    lab1.pack()
    lab2.pack()
    
    obj_fur = Horizons(id=entry_star_num.get(), location=UTS, epochs={'start':'2022-Oct-18 13:00:00','stop':'2022-Oct-18 16:00:00','step':'20m'})
    eph_fur = obj_fur.ephemerides()
    eph_fur_print = eph_fur['AZ','EL']

    frame = tk.Frame(window)
    frame.place(x=400,y=150)
    lab3 = tk.Label(frame,text='Future Trajectory (3 hours):',font=('Arial','15','bold'))
    lab4 = tk.Label(frame,text=eph_fur_print)
    lab3.pack()
    lab4.pack()

    frame = tk.Frame(window)
    frame.place(x=10,y=280)
    lab5 = tk.Label(frame,text=name,width=30, height=5)
    lab5.pack(expand=1)

    frame = tk.Frame(window)
    frame.place(x=240,y=287.5)
    lab6 = tk.Label(frame,text=Cnst)
    lab6.pack()


    
    if EL<=0:
        msgbox.showinfo(title='warning', message='The object is not visible now :)')

        
#search button
btn_search=tk.Button(window,text='Search',command=star_search)
btn_search.place(x=170,y=230)


window.mainloop()
