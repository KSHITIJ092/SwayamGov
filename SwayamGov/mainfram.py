from customtkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk

image1 = CTkImage(Image.open("addhar-removebg-preview.png"), size=(25, 25))

image2 = CTkImage(Image.open("pan-removebg-preview.png"), size=(45, 25))

image3 = CTkImage(Image.open("support-removebg-preview.png"), size=(25, 25))

image4 = CTkImage(Image.open("feedback-removebg-preview.png"), size=(25, 25))

def myfram():
    w2 = CTk()
    w2.title("signup")
    w2.geometry("700x450")

    frame2 = ctk.CTkFrame(master=w2, fg_color="black", corner_radius=0)
    frame2.pack(pady=0, padx=0, fill="both", expand=True)

    
    s = CTkLabel(
        frame2, text="SWAYAM", text_color="yellow", font=("times new roman", 40, "bold")
    )
    s.place(x=250, y=50)

    s1 = CTkLabel(
        frame2, text="GOVERNMENT", text_color="white", font=("times new roman", 40, "bold")
    )
    s1.place(x=200, y=90)

    addhar = CTkButton(
        master=frame2,
        text="ADDHAR",
        image=image1,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=20,
    )
    addhar.place(x=80, y=170)

    pan = CTkButton(
        master=frame2,
        text="PAN",
        image=image2,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=25,
    )
    pan.place(x=250, y=170)

    support=CTkButton(
        master=frame2,
        text="SUPPORT",
        image=image3,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=25,
    )
    support.place(x=390,y=170)

    feedback=CTkButton(
        master=frame2,
        text="FEEDBACK",
        image=image4,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=25,
    )

    feedback.place(x=540,y=170)
    w2.mainloop()
myfram()