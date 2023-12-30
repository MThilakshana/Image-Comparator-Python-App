from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Image-Comparator")
root.resizable(False,False)
root.geometry("630x600")

firstFrame = Frame(root,
                   width=300,
                   height=400,
                   bg="red").place(x=10,y=50)

secondframe = Frame(root,
                   width=300,
                   height=400,
                   bg="green").place(x=320,y=50)


def openfirstImage():
    global file_path_one
    file_path_one = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path_one:
        original_image = Image.open(file_path_one)
        # Resize the image to a specific width and height (e.g., 300x300)
        resized_image = original_image.resize((300, 300))
        photo = ImageTk.PhotoImage(resized_image)
        showfirstimage.config(image=photo)
        showfirstimage.image = photo
        showfirstimage.place(x=10,y=50)
        
def opensecondImage():
    global file_path_two
    file_path_two = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path_two:
        original_image = Image.open(file_path_two)
        # Resize the image to a specific width and height (e.g., 300x300)
        resized_image = original_image.resize((300, 300))
        photo2 = ImageTk.PhotoImage(resized_image)
        showfirstimage.config(image=photo2)
        showfirstimage.image = photo2
        showfirstimage.place(x=320,y=50)
Label(root,
      text="Image Comparator",
      font=('Times 20 bold')).pack(fill=Y)

showfirstimage = Label(firstFrame)

Button(firstFrame,
       text="Upload Image",
       font=('Times 15'),
       width=10,
       height=1,
       cursor='hand2',
       command=openfirstImage).place(x=90,y=370)

Button(secondframe,
       text="Upload Image",
       font=('Times 15'),
       width=10,
       height=1,
       cursor='hand2',
       command=opensecondImage).place(x=400,y=370)

root.mainloop()