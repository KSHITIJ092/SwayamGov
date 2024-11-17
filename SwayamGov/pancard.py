from customtkinter import *
import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from tkinter.filedialog import asksaveasfilename
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from PIL import Image, ImageTk
from PIL import Image as PILImage
import string
from reportlab.lib.utils import ImageReader

import random
def PANCARD():
    w4=CTkToplevel()
    w4.title("signup")
    w4.geometry("400x400")
    def generate_pan_number():
        letters = string.ascii_uppercase
        first_five = ''.join(random.choice(letters) for i in range(5))
        next_four = ''.join(random.choice(string.digits) for i in range(4))
        last_char = random.choice(letters)
        pan_number = f'{first_five}{next_four}{last_char}'
        return pan_number


    new_image=CTkImage(Image.open("add.png"), size=(25, 25))

    frame7=ctk.CTkFrame(master=w4,fg_color="slate blue")
    frame7.pack(pady=0,padx=0,fill='both',expand=True)

    Slabe3=CTkLabel(frame7,text="PAN",  text_color="orange red" , font=("times new roman",40,"bold"))
    Slabe3.place(x=170,y=50)

    AddharNo=CTkEntry(master=frame7,placeholder_text="Addhar Number", width=220, height=35, text_color="chocolate3",font=('arial',20),corner_radius=20,fg_color="powder blue")
    AddharNo.place(x=100,y=130)

    FatherName=CTkEntry(master=frame7,placeholder_text="Father Name", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="#6c6cf4")
    FatherName.place(x=100,y=190)
    pnum=generate_pan_number()
    name_check={'0','1','2','3','4','5','6','7','8','9',"!","@","#","$","%","^","&","*","<",">","?","/",":","{","}","|","'","+","-","(",")"}
    def pancomd():
            PNAM=generate_pan_number()
            num=AddharNo.get()
            fname=FatherName.get()
            mum1=list(num)
            print(num)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="swapgov"
                )

            if conn.is_connected():
                print("Connected to MySQL database")

            cursor = conn.cursor()

            num_query1 = f"SELECT addharNo FROM addhar "
            cursor.execute(num_query1)
            num_result1 = cursor.fetchall()
            addhano1= ', '.join(row[0] for row in num_result1)
            print(addhano1)

            def check_adnum(y):
                if set(addhano1).intersection(y):
                    return True
                else:
                    False

            
            if check_adnum(mum1)==False:
                tkmb.showwarning(title='Wrong input',message='your addhar no are not in database please first create your addharcard')
                
            elif set(name_check).intersection(fname) or fname==" " :
                tkmb.showwarning(title='Wrong input',message='please enter a alphabate not a number and a symbol')
            else:
            
                try:
                
                
                    name_query = f"SELECT Name FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(name_query)
                    name_result = cursor.fetchall()
                    name= ', '.join(row[0] for row in name_result)
                    print(name)
            

                    DOB_query = f"SELECT DateOfBirth FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(DOB_query)
                    DOB_result = cursor.fetchall()
                    DOB = ', '.join(row[0].strftime('%Y-%m-%d') for row in DOB_result)

                    gender_query = f"SELECT Gender FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(gender_query)
                    gender_result = cursor.fetchall()
                    gender= ', '.join(row[0] for row in gender_result)
                    print(gender)


                    phone_query = f"SELECT phoneNO FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(phone_query)
                    phone_result = cursor.fetchall()
                    phoneNo= ', '.join(row[0] for row in phone_result)
                    print(DOB)

                    Address_query = f"SELECT Address FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(Address_query)
                    Address_result = cursor.fetchall()
                    Address= ', '.join(row[0] for row in Address_result)
                    print(Address)

                    num_query = f"SELECT addharNo FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(num_query)
                    num_result = cursor.fetchall()
                    addhano= ', '.join(row[0] for row in num_result)
                    print(addhano)

                    img_query = f"SELECT img FROM addhar WHERE addharNo='{num}';"
                    cursor.execute(img_query)
                    img_result = cursor.fetchall()
                    print(img_result)
                    img= img_result[0][0].decode()
                except:
                    tkmb.showwarning(title='Wrong input',message='enter valid details')

                
            cursor.close()
            conn.close()

            conn1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="swapgov"
                )
            cursor1 = conn1.cursor()
            
            try:
                insert_query1 = "INSERT INTO pancard (panNumber,Name,DateOfBirth,fatherName,img,phoneNumber,addharnum) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    
                
                values1 = (PNAM,name,DOB,fname,img,phoneNo,num)

            
                cursor1.execute(insert_query1, values1)
                conn1.commit()
            except:
                tkmb.showwarning(title='Wrong input',message='enter different addhar number')
                
            cursor1.close()
            conn1.close()


            conn1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="swapgov"
                )

            if conn.is_connected():
                print("Connected to MySQL database")

            cursor1 = conn1.cursor()

        
            print(PNAM)

            name_query1 = f"SELECT Name FROM pancard WHERE panNumber='{PNAM}';"
            cursor1.execute(name_query1)
            name_result1 = cursor1.fetchall()
            name1= ', '.join(row[0] for row in name_result1)
            print(name1)

            DOB_query1 = f"SELECT DateOfBirth FROM  pancard WHERE panNumber='{PNAM}';"
            cursor1.execute(DOB_query1)
            DOB_result1 = cursor1.fetchall()
            DOB1 = ', '.join(row[0].strftime('%Y-%m-%d') for row in DOB_result1)
            print(DOB1)

            father_query1 = f"SELECT fatherName FROM pancard WHERE panNumber='{PNAM}' ;"
            cursor1.execute(father_query1)
            father_result1 = cursor1.fetchall()
            fatherN1= ', '.join(row[0] for row in father_result1)
            print(fatherN1)


            pannu_query1 = f"SELECT panNumber FROM pancard WHERE panNumber='{PNAM}';"
            cursor1.execute(pannu_query1)
            pannu_result1 = cursor1.fetchall()
            pannu1= ', '.join(row[0] for row in pannu_result1)
            print(pannu1)

        
            img1_query = f"SELECT img  FROM pancard WHERE panNumber='{PNAM}';"
            cursor1.execute(img1_query)
            img_result1 = cursor1.fetchall()
            img1= img_result1[0][0].decode()
            print(img1)
            cursor1.close()
            conn1.close()

            ad_frame = CTkToplevel()
            ad_frame.title("signup")
            ad_frame.geometry("600x350")
            ad_frame.resizable(False, False)

            image1 = CTkImage(light_image=Image.open("pan-card.jpg"), size=(600, 350))
            image2 = CTkImage(light_image=Image.open(img1), size=(115, 105))
            image3 = CTkImage(light_image=Image.open("icons8-export-pdf-60.png"), size=(20, 20))

            add_template = CTkLabel(ad_frame, image=image1, text='')
            add_template.pack(pady=0, padx=0, fill='both', expand=True)

            pimg=CTkLabel(ad_frame, image=image2, text='')
            pimg.place(x=20,y=90)

            pn=CTkLabel(ad_frame, text=pannu1, text_color="black",height=10,width=40, font=("times new roman", 22, "bold"), bg_color="light blue")
            pn.place(x=200, y=140)


            n = CTkLabel(ad_frame, text=name1, text_color="black",height=10,width=40, font=("times new roman", 16, "bold"), bg_color="light blue")
            n.place(x=30, y=210)


            fn=CTkLabel(ad_frame, text=fatherN1, text_color="black",height=10,width=40, font=("times new roman", 16, "bold"), bg_color="light blue")
            fn.place(x=30, y=260)

            dn=CTkLabel(ad_frame, text=DOB1, text_color="black",height=10,width=40, font=("times new roman", 16, "bold"), bg_color="light blue")
            dn.place(x=30, y=320)

            def save_as_pdf():
                    
                    filename = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                    if filename:
                        with open(filename, "wb") as f:
                            si=(600,350)
                            c = canvas.Canvas(f, pagesize=si)
                            c.drawImage("pan-card.jpg", 0, 0, width=600, height=350)  # Assuming image1 is a CTkImage object
                            c.drawImage(img1, 20, 150, width=113, height=107)  # Assuming image2 is a CTkImage object
                            c.drawString(250, 190, pannu1)
                            c.drawString(30, 120, name1)
                            c.drawString(30, 80, fatherN1)
                            c.drawString(30, 10, DOB1)
                            c.setEncrypt("bhai")
                            c.setFont("Helvetica-Bold", 70)


                            c.showPage()
                            c.save()


            save_button = CTkButton(ad_frame, text='Save as PDF', command=save_as_pdf, font=("times new roman", 20, "bold"), fg_color="orange", text_color="brown")
            save_button.place(x=30, y=70)
            ad_frame.mainloop()
            


    sign2=CTkButton(master=frame7,image=new_image,text='new',command=pancomd,font=("times new roman",20, "bold"),fg_color="orange",text_color="brown")
    sign2.place(x=130,y=250)
    w4.mainloop()

