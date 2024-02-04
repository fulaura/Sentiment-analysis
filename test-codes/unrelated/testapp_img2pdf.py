import customtkinter
from pydantic import FilePath

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title('Ultimate toolkit - by fulaura')
logo_path="C:\\Users\\Niitro_musics\\Desktop\\Coding\\AI dev_stud\\my_code-stud-exp\\test-codes\\unrelated\\ultimate_toolkit_icon.png"
root.after(201, lambda :root.iconbitmap(logo_path))


#login functions
def login():
    print("analyzing inputs...")
    redirector()
    
def redirector():               #todo: then i have to connect it with database and control it from there
    if entry1.get()=="converter" and entry2.get()=="1234":
        print("successful!")
        frame.pack_forget()
        conv_open_filedir()
    else:
        print("unfortunately, you don't have access to application")


def conv_open_filedir():        #if 1 then redirect   conv_open   ------>   chose_file    /else*    choose_files:
    ui_conv_var_frame.pack(pady=120, padx=10)
    
def chose_file():
    ui_conv_var_frame.pack_forget()
    ui2_frame.pack(pady=120, padx=10)

#def choose_files():
    ###

output_dir = None

def openfile():
    global output_dir
    output_dir = filedialog.askopenfilename()
    if output_dir:
        filename = os.path.basename(output_dir)   #   v1      dir_len = len(output_dir.split('/')[-1])
        output_label.pack_forget()
        output_txt = customtkinter.CTkLabel(master=ui2_frame, text=f"file directory: .../{filename}")
        output_txt.pack()
        return output_dir
    else:
        return None

#Sys 2 PDF converter
def pdfconvert():
    global output_dir
    if output_dir:
        try:
            global pdf
            pdf.add_page()

            # Access and convert image
            with Image.open(output_dir) as image:
                width, height = image.size

                # Resize image if needed (optional)
                max_width = 400
                if width > max_width:
                    eight = int(height * (max_width / width))
                    width = max_width
                    image = image.resize((width, height))

                pdf.image(output_dir, x=0, y=0, w=width, h=height)

            output_pdf_path = os.path.join(os.path.dirname(output_dir), "output_file.pdf")
            pdf.output(output_pdf_path)

            success_label = customtkinter.CTkLabel(master=ui2_frame, text="Conversion successful!")
            success_label.pack()
        except Exception as e:
            print(f"Error during conversion: {e}")
            # Handle the error appropriately, e.g., display an error message
    else:
        print("Choose a file first")
        


#PDF confg
from fpdf import FPDF
import os
from PIL import Image

pdf = FPDF()
pdf.set_auto_page_break(0)


#Main FRAME
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System") #, text_font=("",24)
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry1.bind("<Return>", lambda event: login())

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)
entry2.bind("<Return>", lambda event: login())

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)


from customtkinter import *
from customtkinter import filedialog

#Converter FRAME
ui2_frame = customtkinter.CTkFrame(master=root)
button = customtkinter.CTkButton(master=ui2_frame, text="open", command=openfile)
button.pack()
button_sub = customtkinter.CTkButton(master=ui2_frame, text="Convert to PDF", command=pdfconvert)
button_sub.pack()

output_label = customtkinter.CTkLabel(master=ui2_frame, text="directory:")
output_label.pack()


#ModeChooser FRAME
ui_conv_var_frame = customtkinter.CTkFrame(master=root)
conv_type = customtkinter.CTkButton(master=ui_conv_var_frame, text="convert file", command=chose_file)
conv_type.pack()
conv_type_sub = customtkinter.CTkButton(master=ui_conv_var_frame, text="convert files", command=pdfconvert)
conv_type_sub.pack()


root.mainloop()


#lets continue tomorrow
#todo:
'''
1)+-add option to choose directory or life
2)add output directory
3)save converted file
4)+enter login and it will open converter/... corresponding to your input eg.  login: convert password:1234   (for later)
5)add better layout constructor for file picker/converter


'''