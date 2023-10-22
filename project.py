from deep_translator import GoogleTranslator
from customtkinter import *
from tkinter import *
import pyttsx3
def trsnfr():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="fr").translate(one.get())
    two.insert(0,str(tr))
    
def trsnen():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="en").translate(one.get())
    two.insert(0,str(tr))
    
def trsnar():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="ar").translate(one.get())
    two.insert(0,str(tr))
    
def trsnsp():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="es").translate(one.get())
    two.insert(0,str(tr))
    
def trsnGrm():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="de").translate(one.get())
    two.insert(0,str(tr))
    
def trsnitl():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="it").translate(one.get())
    two.insert(0,str(tr))
    
def trsntrk():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="tr").translate(one.get())
    two.insert(0,str(tr))
    
def trsnrss():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="ru").translate(one.get())
    two.insert(0,str(tr))

def trsnchns():
    two.delete(0,"end")
    tr=GoogleTranslator(source="auto",target="zh-TW").translate(one.get())
    two.insert(0,str(tr))
    
def voiceel():
    rt=pyttsx3.init()
    nm=one.get()
    rt.say(nm)
    return rt.runAndWait()

def voiceer():
    rt=pyttsx3.init()
    nm=two.get()
    rt.say(nm)
    return rt.runAndWait()
    
    
    
rot=CTk()
rot.geometry("800x420")
rot.title("OFPPT TRADUCTION")
rot.iconbitmap("trd.ico")

tlt=CTkLabel(rot,text="Welcom to Translator OFPPT",font=("System",25))
tlt.place(x=210,y=10)

one=CTkEntry(rot,width=300,height=150,corner_radius=int("15"),placeholder_text="Enter")
on=CTkLabel(rot,text="your language",font=("Candara",20))
on.place(x=80,y=100)
one.place(x=10,y=150)



two=CTkEntry(rot,width=300,height=150,corner_radius=int("15"))
tw=CTkLabel(rot,text="Translation",font=("Candara",20))
tw.place(x=570,y=100)
two.place(x=490,y=150)

bt1=CTkButton(rot,text="French",command=trsnfr,hover_color="green")
bt1.place(x=330,y=105)

bt2=CTkButton(rot,text="English",command=trsnen,hover_color="green")
bt2.place(x=330,y=140)

bt3=CTkButton(rot,text="Arabic",command=trsnar,hover_color="green")
bt3.place(x=330,y=175)

bt4=CTkButton(rot,text="Spanish",command=trsnsp,hover_color="green")
bt4.place(x=330,y=210)

bt5=CTkButton(rot,text="German",command=trsnGrm,hover_color="green")
bt5.place(x=330,y=245)

bt6=CTkButton(rot,text="Italian",command=trsnitl,hover_color="green")
bt6.place(x=330,y=280)

bt7=CTkButton(rot,text="Turkish",command=trsntrk,hover_color="green")
bt7.place(x=330,y=315)

bt8=CTkButton(rot,text="Russian",command=trsnrss,hover_color="green")
bt8.place(x=330,y=350)

bt9=CTkButton(rot,text="Chinese",command=trsnchns,hover_color="green")
bt9.place(x=330,y=385)

ph=PhotoImage(file= r"3687408.png")
rs=ph.subsample(1,1)
vss1=CTkLabel(rot,text="voice",font=("Kristen ITC",12))
vss1.place(x=100,y=325)
vs1=CTkButton(rot,text=" ",image=rs,fg_color="#262a30",command=voiceel)
vs1.place(x=50,y=350)


vss2=CTkLabel(rot,text="voice",font=("Kristen ITC",12))
vss2.place(x=630,y=325)
vs2=CTkButton(rot,text=" ",image=rs,fg_color="#262a30",command=voiceer)
vs2.place(x=580,y=350)

rot.mainloop()
