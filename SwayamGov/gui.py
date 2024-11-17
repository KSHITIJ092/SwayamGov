from customtkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.messagebox as tkmb
import mysql.connector
import addhar as ac
import pancard as pc
import download as dw
import feedback as fd



w = CTk()
w.title("Login")
w.geometry("480x500")
image1 = CTkImage(Image.open("addhar-removebg-preview.png"), size=(25, 25))

image2 = CTkImage(Image.open("pan-removebg-preview.png"), size=(45, 25))

image3 = CTkImage(Image.open("support-removebg-preview.png"), size=(25, 25))
image4 = CTkImage(Image.open("feedback-removebg-preview.png"), size=(25, 25))


frame = ctk.CTkFrame(master=w)
frame.pack(pady=20, padx=40, fill='both', expand=True)
ctk.set_appearance_mode("green")
ctk.set_default_color_theme("blue")

mainLabel = CTkLabel(frame, text="Login", text_color="darkorchid3", font=("times new roman", 40))
mainLabel.place(x=150, y=50)

def mainfram():
    w2 = CTkToplevel()
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
        command=ac.ADDHAR,
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
        command=pc.PANCARD,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=25,
    )
    pan.place(x=250, y=170)

    support = CTkButton(
        master=frame2,
        text="DOWNLOAD",
        image=image3,
        command=dw.DOWNLOAD,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=25,
    )
    support.place(x=390, y=170)

    feedback = CTkButton(
        master=frame2,
        text="FEEDBACK",
        image=image4,
        command=fd.FEEDBACK,
        font=("times new roman", 20, "bold"),
        fg_color="light blue",
        text_color="black",
        width=25,
    )
    feedback.place(x=570, y=170)
    w2.mainloop()
   




def lcmd():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="swapgov"
    )

    if conn.is_connected():
        print("Connected to MySQL database")

    cursor = conn.cursor()

    select_query = "SELECT UserName, Password FROM signup"

    cursor.execute(select_query)

    data = cursor.fetchall()

    username_password_pairs = [(item[0], item[1]) for item in data]

    entered_username = userInput.get()
    entered_password = passwordInput.get()

    if (entered_username, entered_password) in username_password_pairs:
        w.withdraw()
        mainfram()
    else:
        tkmb.showwarning(title='Wrong input', message='Your information is not in the database, please register first')

    conn.commit()
    cursor.close()
    conn.close()


userInput = CTkEntry(master=frame, placeholder_text="username", width=200, height=35, text_color='white',font=('arial', 18), corner_radius=20)
userInput.place(x=100, y=150)

passwordInput = CTkEntry(master=frame, placeholder_text="password", show="*", width=200, height=35,text_color='white', font=('arial', 18), corner_radius=20)
passwordInput.place(x=100, y=220)

login = CTkButton(master=frame, command=lcmd, text='Login', font=("times new roman", 18))
login.place(x=120, y=300)


def signupcommand():
    

    w1 = CTk()
    w1.title("signup")
    w1.geometry("400x600")

    frame1 = ctk.CTkFrame(master=w1, fg_color="lime green")
    frame1.pack(pady=0, padx=0, fill='both', expand=True)

    Slabel = CTkLabel(frame1, text="Signup", text_color="white", font=("times new roman", 40, "bold"))
    Slabel.place(x=140, y=50)

    name = CTkEntry(master=frame1, placeholder_text="Name", width=220, height=35, text_color="black",
                    font=('arial', 20), corner_radius=20, fg_color="white")
    name.place(x=100, y=130)

    dob = CTkEntry(master=frame1, placeholder_text="Date Of Birth", width=220, height=35, text_color="black",font=('arial', 20), corner_radius=20, fg_color="white")
    dob.place(x=100, y=190)

    gender = CTkEntry(master=frame1, placeholder_text="Gender", width=220, height=35, text_color="black",font=('arial', 20), corner_radius=20, fg_color="white")
    gender.place(x=100, y=250)

    phoneNo = CTkEntry(master=frame1, placeholder_text="Phone No", width=220, height=35, text_color="black",font=('arial', 20), corner_radius=20, fg_color="white")
    phoneNo.place(x=100, y=310)

    address = CTkEntry(master=frame1, placeholder_text="Address", width=220, height=35, text_color="black",font=('arial', 20), corner_radius=20, fg_color="white")
    address.place(x=100, y=370)

    Username = CTkEntry(master=frame1, placeholder_text="User Name", width=220, height=35, text_color="black",font=('arial', 20), corner_radius=20, fg_color="white")
    Username.place(x=100, y=430)

    password = CTkEntry(master=frame1, placeholder_text="Password", width=220, height=35, text_color="black",font=('arial', 20), corner_radius=20, fg_color="white")
    password.place(x=100, y=490)

    def scomd():
        name1 = name.get()
        dob1 = dob.get()
        gender1 = gender.get()
        phoneNo1 = phoneNo.get()
        address1 = address.get()
        Username1 = Username.get()
        password1 = password.get()
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

            values = (name1, dob1, gender1, phoneNo1, address1, Username1, password1)

            cursor.execute(insert_query, values)

            conn.commit()

            cursor.close()
            conn.close()
            w1.withdraw()




        except mysql.connector.Error as e:
            tkmb.showwarning(title='Wrong input', message='This username is already selected by someone else')

    sign = CTkButton(master=frame1, text='Sign Up', command=scomd, font=("times new roman", 20, "bold"),fg_color="orange", text_color="brown")
    sign.place(x=130, y=550)
    w1.mainloop()


signup = CTkButton(master=frame, command=signupcommand,image=image2, text='signup', font=("times new roman", 18))
signup.place(x=120, y=350)

w.mainloop()
