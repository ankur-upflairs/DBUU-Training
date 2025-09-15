import tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()
root.geometry('600x400')
root.title('Images App')
image=Image.open('check.png')
image=image.resize((20,20))
img=ImageTk.PhotoImage(image)
# label=tk.Label(root,text='check',image=img,compound="left")
# label.pack()
# root.iconbitmap()#only .ico images are allowed
root.iconphoto(True,img)
root.mainloop()
