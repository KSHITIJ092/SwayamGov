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
def DOWNLOAD():
    w4=CTkToplevel()
    w4.title("download")
    w4.geometry("500x400")
    # frame7=ctk.CTkFrame(master=w4,fg_color="slate blue")
    # frame7.pack(pady=0,padx=0,fill='both',expand=True)

    Slabe4=CTkLabel(w4,text="Download",font=("times new roman",40,"bold"))
    Slabe4.place(x=170,y=50)

    Anum=CTkEntry(w4,placeholder_text="Enter addhar number",width=220, height=35,font=('arial',20),corner_radius=20)
    Anum.place(x=140,y=130) 
    num=Anum.get()

    PNA=CTkEntry(w4,placeholder_text="Enter Pan number",width=220, height=35,font=('arial',20),corner_radius=20)
    PNA.place(x=140,y=250) 


    def addow():
                num=Anum.get()
                conn1 = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="swapgov"
                    )

                if conn1.is_connected():
                    print("Connected to MySQL database")

                cursor1 = conn1.cursor()

                num_query1 = f"SELECT addharNo FROM addhar "
                cursor1.execute(num_query1)
                num_result1 = cursor1.fetchall()
                addhano1= ', '.join(row[0] for row in num_result1)
                add=addhano1.split()

                print(addhano1)
                cursor1.close()
                conn1.close()

                print(num)

                if num not in add:
                    tkmb.showwarning(title='Wrong input',message='your Pan no are not in database please first create your addharcard')
                

                elif num=="":
                    tkmb.showwarning(title='Wrong input',message='please enter a Pan Number')
                
                else:

                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="swapgov")

                    if conn.is_connected():
                            print("Connected to MySQL database")

                    cursor = conn.cursor()


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
                        


                    cursor.close()
                    conn.close()

                    filename = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                    if filename:
                                with open(filename, "wb") as f:
                                    si=(600,350)
                                    c = canvas.Canvas(f, pagesize=si)
                                    c.drawImage("addTemplate.jpg", 0, 0, width=600, height=300)  # Assuming image1 is a CTkImage object
                                    c.drawImage(img, 10, 70, width=150, height=150)  # Assuming image2 is a CTkImage object
                                    c.drawString(180, 210, name)
                                    c.drawString(180, 180, f"Date of Birth: {DOB}")
                                    c.drawString(180, 150, f"Gender: {gender}")
                                    c.drawString(180, 120, f"Phone Number: {phoneNo}")
                                    c.drawString(180, 90, f"Address:{Address}")
                                    c.drawString(200, 60, num)
                                    c.setEncrypt("bhai")
                                    c.setFont("Helvetica-Bold", 70)

                                    c.showPage()
                                    c.save()


    def padow():
                PNAM=PNA.get()
                conn2 = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="swapgov"
                    )

                if conn2.is_connected():
                    print("Connected to MySQL database")

                cursor2 = conn2.cursor()

            
            

                pan_query = f"SELECT panNumber FROM pancard ;"
                cursor2.execute(pan_query)
                pan_result1 = cursor2.fetchall()
                pan= ', '.join(row[0] for row in pan_result1)
                pan1= pan.split(", ")
            
                print(pan1)
                
                


                cursor2.close()
                conn2.close()
                    
                if PNAM not in pan1:
                    tkmb.showwarning(title='Wrong input',message='your Pan no are not in database please first create your addharcard')
                

                elif PNAM=="":
                    tkmb.showwarning(title='Wrong input',message='please enter a Pan Number')
                
                else:

                    conn1 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="swapgov"
                        )

                    if conn1.is_connected():
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
                



    adow=CTkButton(w4,font=("times new roman",20, "bold"),command=addow,text="Addhar Download")
    adow.place(x=160,y=200)

    adow=CTkButton(w4,font=("times new roman",20, "bold"),command=padow,text="Pan Download")
    adow.place(x=160,y=320)
    w4.mainloop()