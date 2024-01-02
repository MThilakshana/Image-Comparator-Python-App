import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageUploaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")
        self.master.geometry("700x400")

        self.image1_label = tk.Label(self.master, text="Image 1:")
        self.image1_label.grid(row=0, column=0, padx=10, pady=10)

        self.image2_label = tk.Label(self.master, text="Image 2:")
        self.image2_label.grid(row=0, column=1, padx=10, pady=10)

        self.image1_display = tk.Label(self.master)
        self.image1_display.grid(row=1, column=0, padx=10, pady=10)

        self.image2_display = tk.Label(self.master)
        self.image2_display.grid(row=1, column=1, padx=10, pady=10)

        self.upload_button = tk.Button(self.master, text="Upload Images", command=self.upload_images)
        self.upload_button.grid(row=2, column=0, columnspan=2, pady=10)

    def upload_images(self):
        image1_path = filedialog.askopenfilename(title="Select Image 1", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        image2_path = filedialog.askopenfilename(title="Select Image 2", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if image1_path and image2_path:
            self.display_image(image1_path, self.image1_display)
            self.display_image(image2_path, self.image2_display)

    def display_image(self, path, label):
        original_image = Image.open(path)
        resized_image = original_image.resize((200, 200))
        photo = ImageTk.PhotoImage(resized_image)
        label.config(image=photo)
        label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploaderApp(root)
    root.mainloop()
