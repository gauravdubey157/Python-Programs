from tkinter import*
#from PIL import Image, ImageTk
root=Tk()
root.geometry("455x244")

photo = PhotoImage(file="pic.jpg")
label= Label(image = photo)
label.pack()

root.mainloop()