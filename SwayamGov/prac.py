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
ad_frame = CTk()
ad_frame.title("signup")
ad_frame.geometry("600x350")
ad_frame.resizable(False, False)

image1 = CTkImage(light_image=Image.open("pan-card.jpg"), size=(600, 350))
image2 = CTkImage(light_image=Image.open("srk-removebg-preview(1).jpg"), size=(115, 105))
image3 = CTkImage(light_image=Image.open("icons8-export-pdf-60.png"), size=(20, 20))

add_template = CTkLabel(ad_frame, image=image1, text='')
add_template.pack(pady=0, padx=0, fill='both', expand=True)

pimg=CTkLabel(ad_frame, image=image2, text='')
pimg.place(x=20,y=90)

pn=CTkLabel(ad_frame, text="1 a 3 v b  3 r 5 t 6", text_color="black",height=10,width=40, font=("times new roman", 22, "bold"), bg_color="light blue")
pn.place(x=200, y=140)


n = CTkLabel(ad_frame, text="abdul", text_color="black",height=10,width=40, font=("times new roman", 16, "bold"), bg_color="light blue")
n.place(x=30, y=210)


fn=CTkLabel(ad_frame, text="Shahnawaz aziz khan", text_color="black",height=10,width=40, font=("times new roman", 16, "bold"), bg_color="light blue")
fn.place(x=30, y=260)

dn=CTkLabel(ad_frame, text="2004-6-10", text_color="black",height=10,width=40, font=("times new roman", 16, "bold"), bg_color="light blue")
dn.place(x=30, y=320)


ad_frame.mainloop()