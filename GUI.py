__author__ = 'Roy'
from ns_api import *
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk

MS = Tk()
MS.attributes("-fullscreen", True)
MS.title('Home')
MS.configure(background='#F4D31A')
Label(MS,text='Welkom bij NS',font=("Helvetica", 30, "bold"),fg = "#000066", bg="#F4D31A").place(x=530,y=60)
photo = ImageTk.PhotoImage(Image.open("NS-scherm.png"))
Label(MS, image=photo).place(x=450,y=250)



button1 = Button(MS,text='Ik wil naar \n Amsterdam',fg="white",bg="#000066",height=3,width=15,font=(2)).place(x=300,y=550)
button2 = Button(MS,text='Kopen \n los kaartje',fg="white",bg="#000066",height=3,width=15,font=(2)).place(x=460,y=550)
button3 = Button(MS,text='Kopen \n Ov-chipkaart',fg="white",bg="#000066",height=3,width=15,font=(2)).place(x=620,y=550)
button4 = Button(MS,text='Ik wil naar \n het buitenland',fg="white",bg="#000066",height=3,width=15,font=(2)).place(x=780,y=550)
button5 = Button(MS,text='actuele \n vertrekinformatie',fg="white",bg="#000066",height=3,width=15,font=(2),command=lambda: departure()).place(x=940,y=550)
Button(MS, text ='Quit \n(testing purposes)', fg='white', bg='#000066', height=4, width=20, font=(2), command=lambda: MS.destroy()).place(x=25, y=25)


def departure():
    NS = Tk()
    NS.attributes("-fullscreen", True)
    NS.geometry('1680x1050+300+50')
    NS.title('Actuele vertrektijden')
    NS.configure(background='#F4D31A')
    Label(NS,text='Actuele Vertrektijden',font=("Helvetica", 30, "bold"),fg = "#000066", bg="#F4D31A").place(x=500,y=60)
    Button(NS,text='Terug',font = ('Helvetiva', 25, 'bold'), fg="white",bg="#000066",height=2,width=10,command=lambda: NS.destroy()).place(x=25,y=25)
    label = Label(NS, text='Voer station in:', font = ('Helvetica', 25, 'bold'), fg = '#000066', bg = '#F4D31A')
    label.place(x = 560, y = 100)
    naam = Entry(NS)
    naam.place(x = 610, y = 140)
    button = Button(NS, text='Zoek tijden', font = ('Helvetica', 25, 'bold'), fg = 'white', bg ='#000066',height=2,width=10,command=lambda: zoek_reistijden(naam.get(),NS))
    button.place(x = 570, y = 170)

    NS.mainloop()

def zoek_reistijden(text, pFrame):

    if is_geldig_station(text):
        vertrektijdendict = vertrektijden_lijst(text)
        yyy=345
        Label(pFrame, text = 'Tijd: \tEindbestemming: \tTreinsoort: \tVertrekspoor:', font = ('Helvetica', 25, 'bold'), fg = '#000066', bg = '#F4D31A').place(x = 200, y = 300)
        counter=0
        for vertrekken in vertrektijdendict['ActueleVertrekTijden']['VertrekkendeTrein']:
                if counter is 15:
                    break

                Label(pFrame, text = vertrekken['VertrekTijd'][11:19], font = ('Helvetica', 15, 'bold'),anchor='w', width=10, fg = '#000066', bg = '#F4D31A').place(x=200, y= yyy)
                Label(pFrame, text = vertrekken['EindBestemming'], font = ('Helvetica', 15, 'bold'),anchor='w', width=20, fg = '#000066', bg = '#F4D31A').place(x=345, y=yyy)
                Label(pFrame, text = vertrekken['TreinSoort'], font = ('Helvetica', 15, 'bold'),anchor='w', width=15,  fg = '#000066', bg = '#F4D31A').place(x=635, y=yyy)
                Label(pFrame, text = vertrekken['VertrekSpoor']['#text'], font = ('Helvetica', 15, 'bold'),anchor='w',  width=10, fg = '#000066', bg = '#F4D31A').place(x=920, y=yyy)
                if vertrekken['VertrekSpoor']['@wijziging'] == 'true':
                    wijziging = 'Gewijzigd vertrekspoor'
                if vertrekken['VertrekSpoor']['@wijziging'] == 'false':
                    wijziging = '  '
                Label(pFrame, text = wijziging, font = ('Helvetica', 15, 'bold'), width=20, fg = '#000066', bg = '#F4D31A').place(x=1200, y=yyy)
                yyy +=30
                counter += 1

    else:
        showerror("Ongeldig station","Ongeldig station")







MS.mainloop()


