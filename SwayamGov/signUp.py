from customtkinter import *
import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import mysql.connector
import gui as g
w1=CTk()
w1.title("signup")
w1.geometry("400x600")

frame1=ctk.CTkFrame(master=w,fg_color="lime green")
frame1.pack(pady=0,padx=0,fill='both',expand=True)

Slabel=CTkLabel(frame1,text="Signup",  text_color="white" , font=("times new roman",40,"bold"))
Slabel.place(x=140,y=50)

name=CTkEntry(master=frame1,placeholder_text="Name", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
name.place(x=100,y=130)

dob=CTkEntry(master=frame1,placeholder_text="Date Of Birth", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
dob.place(x=100,y=190)

gender=CTkEntry(master=frame1,placeholder_text="Gender", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
gender.place(x=100, y=250)

phoneNo=CTkEntry(master=frame1,placeholder_text="Phone No", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
phoneNo.place(x=100, y=310 )

address=CTkEntry(master=frame1,placeholder_text="Address", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
address.place(x=100, y=370)

Username=CTkEntry(master=frame1,placeholder_text="User Name", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
Username.place(x=100,y=430)

password=CTkEntry(master=frame1,placeholder_text="Password", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="white")
password.place(x=100, y=490)

def scomd():
    
    
    name1=name.get()
    dob1=dob.get()
    gender1=gender.get()
    phoneNo1=phoneNo.get()
    address1=address.get()
    Username1=Username.get()
    password1=password.get()
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="swapgov"
    )

    if conn.is_connected():
        print("Connected to MySQL database")
    cursor = conn.cursor()
    try:
        insert_query = "INSERT INTO signup (Name,DateOfBirth,Gender,PhoneNo,Address,UserName,Password) VALUES (%s,%s,%s,%s,%s,%s,%s)"


        values = (name1,dob1,gender1,phoneNo1,address1,Username1,password1)

        cursor.execute(insert_query, values)

        conn.commit()

        cursor.close()
        conn.close()
        
    except:
        tkmb.showwarning(title='Wrong input',message='this username is already selected by other') 

sign=CTkButton(master=frame,text='Sign Up',command=scomd,font=("times new roman",20, "bold"),fg_color="orange",text_color="brown")
sign.place(x=130,y=550)
w.mainloop()