from customtkinter import *
import customtkinter as ctk

from PIL import Image, ImageTk
import tkinter.messagebox as tkmb
import mysql.connector
def FEEDBACK():
    w4=CTkToplevel()
    w4.title("download")
    w4.geometry("500x400")
    # frame7=ctk.CTkFrame(master=w4,fg_color="slate blue")
    # frame7.pack(pady=0,padx=0,fill='both',expand=True)

    Slabe4=CTkLabel(w4,text="FeedBack",font=("times new roman",40,"bold"))
    Slabe4.place(x=170,y=50)

    fnum=CTkEntry(w4,placeholder_text="feedback id",width=220, height=35,font=('arial',20),corner_radius=20)
    fnum.place(x=140,y=130) 

    feed=CTkEntry(w4,placeholder_text="Enter feedback",width=220, height=35,font=('arial',20),corner_radius=20)
    feed.place(x=140,y=200) 


    def feedba():
                fe=feed.get()
                fnum1=fnum.get()
                conn1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="swapgov"
            )
                cursor1 = conn1.cursor()
                
                try:
                    insert_query1 = "INSERT INTO feedback (feedbac,fnum) VALUES (%s,%s)"
                            
                        
                    values1 = (fe,fnum1)
                    print(type(values1))

                    
                    cursor1.execute(insert_query1, values1)
                    conn1.commit()
                    tkmb.showinfo(title='success',message='your feedback is added succesfully')
                    
                except:
                    tkmb.showwarning(title='warning',message='please enter unique feedback id')
                    
                
                cursor1.close()
                conn1.close()



    adow=CTkButton(w4,font=("times new roman",20, "bold"),command=feedba,text="ADD")
    adow.place(x=160,y=250)
    w4.mainloop()
