from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Image-Comparator")
root.resizable(False,False)

firstFrame = Frame(root,
                   width=300,
                   height=300,
                   bg="#DCDADA").place(x=10,y=50)


def openfirstImage():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        original_image = Image.open(file_path)
        # Resize the image to a specific width and height (e.g., 300x300)
        resized_image = original_image.resize((300, 300))
        photo = ImageTk.PhotoImage(resized_image)
        showfirstimage.config(image=photo)
        showfirstimage.image = photo
        showfirstimage.pack()

Label(root,
      text="Image Comparator",
      font=('Times 20 bold')).pack(fill=Y)

showfirstimage = Label(root)

firstPicPath = Entry(root,
                     font=('Times 15')).pack(fill=X,padx=20)

Button(root,
       text="Upload Image",
       font=('Times 15'),
       width=10,
       height=1,
       cursor='hand2',
       command=openfirstImage).pack(fill=Y,pady=30,padx=40)

root.mainloop()