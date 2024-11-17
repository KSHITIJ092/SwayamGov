# from customtkinter import *
# import random
# import customtkinter as ctk
# from PIL import Image, ImageTk
# from tkinter.filedialog import asksaveasfilename
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

# ad_frame = CTkToplevel()
# ad_frame.title("signup")
# ad_frame.geometry("600x350")
# ad_frame.resizable(False, False)
# def fil_op():
    
#     fi_name=filedialog.askopenfilename()
#     return fi_name

# image2 = CTkImage(light_image=Image.open("srk-removebg-preview(1).jpg"), size=(150, 150))
# image1 = CTkImage(light_image=Image.open("addTemplate.jpg"), size=(600, 350))

# image3 =CTkImage(light_image=Image.open("icons8-export-pdf-60.png"), size=(20, 20))

# add_template = CTkLabel(ad_frame, image=image1, text='')
# add_template.pack(pady=0, padx=0, fill='both', expand=True)

# s = CTkLabel(ad_frame, image=image2, text='')
# s.place(x=10, y=70)

# n = CTkLabel(ad_frame, text="sharuk khan", text_color="black", font=("times new roman", 16, "bold"), bg_color="#FAF9F6")
# n.place(x=180, y=70)

# d = CTkLabel(ad_frame, text="date of birth:01/05/1951", text_color="black", font=("times new roman", 16, "bold"), bg_color="#FAF9F6")
# d.place(x=180, y=100)

# g = CTkLabel(ad_frame, text="Gender:male", text_color="black", font=("times new roman", 16, "bold"), bg_color="#FAF9F6")
# g.place(x=180, y=130)

# p = CTkLabel(ad_frame, text="Phone Number:7208757995", text_color="black", font=("times new roman", 16, "bold"), bg_color="#FAF9F6")
# p.place(x=180, y=160)

# ad = CTkLabel(ad_frame, text="address:rashid compound kausa mumbra thanekausa kabristan", text_color="black", font=("times new roman", 16, "bold"), wraplength=400, bg_color="#FAF9F6")
# ad.place(x=180, y=190)
# random_number =" ".join( random.choices('0123456789', k=10))
# an=CTkLabel(ad_frame, text=random_number, text_color="black", font=("times new roman", 25, "bold"), wraplength=400, bg_color="#FAF9F6")
# an.place(x=250, y=240)

# def save_as_pdf():
#     filename = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
#     if filename:
#         with open(filename, "wb") as f:
#             c = canvas.Canvas(f, pagesize=letter)
#             c.drawImage("addTemplate.jpg", 0, 0, width=600, height=300)  # Assuming image1 is a CTkImage object
#             c.drawImage("srk-removebg-preview(1).jpg", 10, 70, width=150, height=150)  # Assuming image2 is a CTkImage object
#             c.drawString(180, 70, name3)
#             c.drawString(180, 100, f"Date of Birth: {dob3}")
#             c.drawString(180, 130, f"Gender: {gender3}")
#             c.drawString(180, 160, f"Phone Number: {phoneNo3}")
#             c.drawString(180, 190, f"Address:{address3}")
#             c.drawString(180, 190, f"Address:{address3}")
#             c.showPage()
#             c.save()


# save_button = CTkButton(ad_frame, text='Save as PDF', command=save_as_pdf, font=("times new roman", 20, "bold"), fg_color="orange", text_color="brown")
# save_button.place(x=30, y=70)

# ad_frame.mainloop()
import random
def rand_num():
    random_number ="".join( random.choices('0123456789', k=10))
    return random_number

print(rand_num())