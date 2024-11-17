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
from reportlab.lib.utils import ImageReader

import random
def ADDHAR():
    w4=CTkToplevel()
    w4.title("signup")
    w4.geometry("400x600")


    frame3=ctk.CTkFrame(master=w4,fg_color="#f46c6c")
    frame3.pack(pady=0,padx=0,fill='both',expand=True)

    Slabe2=CTkLabel(frame3,text="addhar",  text_color="white" , font=("times new roman",40,"bold"))
    Slabe2.place(x=140,y=50)

    name2=CTkEntry(master=frame3,placeholder_text="Name", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="#6c6cf4")
    name2.place(x=100,y=130)

    dob2=CTkEntry(master=frame3,placeholder_text="Date Of Birth", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="#6c6cf4")
    dob2.place(x=100,y=190)
    options = ["Male", "Female", "Transgender"]

    gender2=CTkComboBox(master=frame3,values=options, width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="#6c6cf4")
    gender2.place(x=100, y=250)

    phoneNo2=CTkEntry(master=frame3,placeholder_text="Phone No", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="#6c6cf4")
    phoneNo2.place(x=100, y=310 )

    address2=CTkEntry(master=frame3,placeholder_text="Address", width=220, height=35, text_color="black",font=('arial',20),corner_radius=20,fg_color="#6c6cf4")
    address2.place(x=100, y=370)
    new_image=CTkImage(Image.open("add.png"), size=(25, 25))
    open_img=CTkImage(Image.open("download-folder.png"), size=(25, 25))

    name3=name2.get()
    dob3=dob2.get()
    gender3=gender2.get()
    phoneNo3=phoneNo2.get()
    address3=address2.get()
    def rand_num():
        random_number ="".join( random.choices('0123456789', k=10))
        return random_number
    def fil_op():
        global fi_name
        fi_name=filedialog.askopenfilename()


    def check(y):
        try:
            datetime.strptime(y,"%Y-%m-%d")
            return True
        except:
            return False
    def addharcomd():
        
        
        name3=name2.get()
        dob3=dob2.get()
        gender3=gender2.get()
        phoneNo3=phoneNo2.get()
        address3=address2.get()
    
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="swapgov"
        )

        if conn.is_connected():
            print("Connected to MySQL database")
        cursor = conn.cursor()
        name_check={'0','1','2','3','4','5','6','7','8','9',"!","@","#","$","%","^","&","*","<",">","?","/",":","{","}","|","'","+","-","(",")"}
        name_list=list(name3)
        number_check={'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        number_list=list(phoneNo3)

        if set(name_check).intersection(name3) or name3==" " :
            tkmb.showwarning(title='Wrong input',message='please enter a alphabate not a number and a symbol')
        elif check(dob3)==False:
            tkmb.showwarning(title='Wrong input',message='please enter a valid date of birth')
        
        elif set(number_check).intersection(number_list) or len(number_list)!=10:
            tkmb.showwarning(title='Wrong input',message='please enter a valid number')
        
        elif address3==" ":
            tkmb.showwarning(title='Wrong input',message='please enter some thing')
        else:
            global fi_name
            num=rand_num()
            with open(fi_name, 'rb') as file:
                image_data = file.read()
            # try:
            
            insert_query = "INSERT INTO addhar (Name,DateOfBirth,Gender,PhoneNo,Address,addharNo,img) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            
            num=rand_num()
            values = (name3,dob3,gender3,phoneNo3,address3,num,fi_name)

            cursor.execute(insert_query, values)

            conn.commit()

            cursor.close()
            conn.close()
            

                
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="swapgov"
                )

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


            ad_frame = CTkToplevel()
            ad_frame.title("signup")
            ad_frame.geometry("600x350")
            ad_frame.resizable(False, False)

            image1 = CTkImage(light_image=Image.open("addTemplate.jpg"), size=(600, 350))
            image2 = CTkImage(light_image=Image.open(img), size=(150, 150))
            image3 = CTkImage(light_image=Image.open("icons8-export-pdf-60.png"), size=(20, 20))

            add_template = CTkLabel(ad_frame, image=image1, text='')
            add_template.pack(pady=0, padx=0, fill='both', expand=True)

            s = CTkLabel(ad_frame, image=image2, text='')
            s.place(x=10, y=70)

            n = CTkLabel(ad_frame, text=name, text_color="black", font=("times new roman", 16, "bold"), bg_color="white")
            n.place(x=180, y=70)

            d = CTkLabel(ad_frame, text=f"date of birth:{DOB}", text_color="black", font=("times new roman", 16, "bold"), bg_color="white")
            d.place(x=180, y=100)

            g = CTkLabel(ad_frame, text=f"Gender:{gender}", text_color="black", font=("times new roman", 16, "bold"), bg_color="white")
            g.place(x=180, y=130)

            p = CTkLabel(ad_frame, text=f"Phone Number:{phoneNo}", text_color="black", font=("times new roman", 16, "bold"), bg_color="white")
            p.place(x=180, y=160)

            ad = CTkLabel(ad_frame, text=f"address{Address}:", text_color="black", font=("times new roman", 16, "bold"), wraplength=400, bg_color="white")
            ad.place(x=180, y=190)
            num=rand_num()
            addhano1=" ".join(addhano)
            an=CTkLabel(ad_frame, text=addhano1, text_color="black", font=("times new roman", 25, "bold"), wraplength=400, bg_color="#FAF9F6")
            an.place(x=250, y=240)

                
            def save_as_pdf():
                    
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
                            c.drawString(200, 60, addhano1)
                            c.setEncrypt("bhai")
                            c.setFont("Helvetica-Bold", 70)

                            c.showPage()
                            c.save()


            save_button = CTkButton(ad_frame, text='Save as PDF', command=save_as_pdf, font=("times new roman", 20, "bold"), fg_color="orange", text_color="brown")
            save_button.place(x=30, y=70)
                    

            ad_frame.mainloop()

            
            # except:
            # tkmb.showwarning(title='Wrong input',message='please add your own number') 
        

    openb_=CTkButton(master=frame3,image=open_img,text='open file',command=fil_op,font=("times new roman",20, "bold"),fg_color="orange",text_color="brown")
    openb_.place(x=130,y=450)

    sign2=CTkButton(master=frame3,image=new_image,text='new',command=addharcomd,font=("times new roman",20, "bold"),fg_color="orange",text_color="brown")
    sign2.place(x=130,y=510)



    w4.mainloop()
