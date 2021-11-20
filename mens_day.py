import smtplib
from tkinter import *
import mysql.connector
window = Tk()
def comm():
    s = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "root",
        database = "email"
    )
    details = s.cursor()
    en1 = e1.get()
    en2 = e2.get()
    en3 = e3.get()
    en4 = e4.get()
    en5 = e5.get()
    server  = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
    server.login(en1, en2)
    server.sendmail(en3 , en4 , en5)
    details.execute("insert into user_data values(%s , %s , %s , %s , %s);" , (en1 , en2 , en3 , en4 , en5))
    s.commit()
    server.quit()
    
window.geometry("400x400")
e1 = StringVar()
label1 = Label(window , text = "Enter email").place(relx = 0.25  , rely = 0.15 , anchor = "center")
entry1 = Entry(window , textvar = e1).place(relx = 0.5 , rely = 0.15, anchor = "center")

e2 = StringVar()
label2 = Label(window , text = "Enter password").place(relx = 0.235 , rely = 0.30 , anchor = "center")
entry2 = Entry(window , textvar = e2).place(relx = 0.5  , rely = 0.30 , anchor = "center")

e3 = StringVar()
label3 = Label(window , text = "Enter email").place(relx  = 0.25 , rely = 0.45 , anchor = "center")
entry3 = Entry(window , textvar = e3).place(relx = 0.5 , rely = 0.45 , anchor = "center")

e4 = StringVar()
label4 = Label(window , text = "Recipient email").place(relx = 0.24 , rely = 0.60 , anchor = "center")
entry4 = Entry(window , textvar = e4).place(relx = 0.5 , rely = 0.60 , anchor = "center")

e5 = StringVar()
label5 = Label(window , text = "Message").place(relx = 0.24 , rely = 0.75 , anchor = "center")
entry5 = Entry(window , textvar = e5).place(relx = 0.5 , rely = 0.75 , anchor = "center")

b1 = Button(window , text = "Mail" , command = comm).place(relx = 0.5 , rely = 0.90 ,anchor = "center")
window.mainloop()