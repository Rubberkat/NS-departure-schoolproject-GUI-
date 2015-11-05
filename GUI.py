__author__ = 'Roy'
from ns_api import *
import sys
from tkinter import *
from tkinter.messagebox import *

NS = Tk()
NS.geometry('1680x1050+300+50')
NS.title('Actuele vertrektijden')
NS.configure(background='#F4D31A')
label1 = Label(NS,text='Actuele Vertrektijden',font=("Helvetica", 30, "bold"),fg = "#000066", bg="#F4D31A").place(x=500,y=60)


def zoek_reistijden(text):
    if is_geldig_station(text):
        vertrektijdendict = vertrektijden_lijst(text)
        yyy=345
        Label(NS, text = 'Tijd: \tEindbestemming: \tTreinsoort: \tVertrekspoor:', font = ('Helvetica', 25, 'bold'), fg = '#000066', bg = '#F4D31A').place(x = 200, y = 300)
        for vertrekken in vertrektijdendict['ActueleVertrekTijden']['VertrekkendeTrein']:
                Label(NS, text = vertrekken['VertrekTijd'][11:19], font = ('Helvetica', 15, 'bold'), fg = '#000066', bg = '#F4D31A').place(x=200, y= yyy)
                Label(NS, text = vertrekken['EindBestemming'], font = ('Helvetica', 15, 'bold'), fg = '#000066', bg = '#F4D31A').place(x=345, y=yyy)
                Label(NS, text = vertrekken['TreinSoort'], font = ('Helvetica', 15, 'bold'), fg = '#000066', bg = '#F4D31A').place(x=635, y=yyy)
                Label(NS, text = vertrekken['VertrekSpoor']['#text'], font = ('Helvetica', 15, 'bold'), fg = '#000066', bg = '#F4D31A').place(x=920, y=yyy)
                if vertrekken['VertrekSpoor']['@wijziging'] == 'true':
                    wijziging = 'Gewijzigd vertrekspoor'
                    Label(NS, text = wijziging, font = ('Helvetica', 15, 'bold'), fg = '#000066', bg = '#F4D31A').place(x=1200, y=yyy)
                yyy +=25
    else:
        showerror("Ongeldig station","Ongeldig station")

label = Label(NS, text='Voer station in:', font = ('Helvetica', 25, 'bold'), fg = '#000066', bg = '#F4D31A')
label.place(x = 560, y = 100)
naam = Entry(NS)
naam.place(x = 610, y = 140)
button = Button(NS, text='Zoek tijden', font = ('Helvetica', 25, 'bold'), fg = 'white', bg ='#000066',height=2,width=10,command=lambda: zoek_reistijden(naam.get()))
button.place(x = 570, y = 170)


def quit():
    NS.destroy()

button5 = Button(NS,text='Terug',font = ('Helvetiva', 25, 'bold'), fg="white",bg="#000066",height=2,width=10,command=lambda: quit()).place(x=25,y=25)


NS.mainloop()
