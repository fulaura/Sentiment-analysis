from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename()
    file = open(filepath,'r')
    
    print(file.read())
    file.close()
    
window = Tk()
button = Button(text="open", command=openfile)
button.pack()
window.mainloop()



