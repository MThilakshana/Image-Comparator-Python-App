import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        label.pack()

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Create a label to display the image
label = tk.Label(root)

# Create a button to open the image
button = tk.Button(root, text="Open Image", command=open_image)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()