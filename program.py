import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import face_recognition

class ImageUploaderApp:
        
    def __init__(self, master):
        self.master = master

        self.main_label = tk.Label(self.master, text="Image Comparator", font=('Times', 20, 'bold'))
        self.main_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        self.image1_label = tk.Label(self.master, text="Image 1:")
        self.image1_label.grid(row=1, column=0, padx=10, pady=10)

        self.image2_label = tk.Label(self.master, text="Image 2:")
        self.image2_label.grid(row=1, column=1, padx=10, pady=10)

        self.image1_display = tk.Label(self.master)
        self.image1_display.grid(row=2, column=0, padx=10, pady=10)

        self.image2_display = tk.Label(self.master)
        self.image2_display.grid(row=2, column=1, padx=10, pady=10)

        self.upload_button = tk.Button(self.master, text="Upload Images", command=self.upload_images)
        self.upload_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.compare_button = tk.Button(self.master, text="Compare Images",command=self.imageComparator)
        self.compare_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.result_label = tk.Label(self.master)
        self.result_label.grid(row=5, column=0,columnspan=2, padx=10, pady=10)
        
        self.acc_label = tk.Label(self.master)
        self.acc_label.grid(row=6, column=0,columnspan=2, padx=10, pady=10)
        
    def find_face(self, img_path):
        image = cv2.imread(img_path)
        face_enc = face_recognition.face_encodings(image)
        return face_enc[0]
        
    def imageComparator(self):
        image1 = self.find_face(image1_path)
        image2 = self.find_face(image2_path)
        
        is_same = face_recognition.compare_faces([image1],image2)[0]
        
        result = ""
        acc = ""
        
        if is_same:
            distance = face_recognition.face_distance([image1],image2)
            distance = round(distance[0]*100)
            accuracy = 100 - round(distance)
            result = "The fases are same"
            acc = f"Accuracy Level - {accuracy}%"
        else:
            result = "The faces are not same."
        
        self.result_label.config(text=result)
        self.acc_label.config(text=acc)


    def upload_images(self):
        global image1_path
        global image2_path
        
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

root = tk.Tk()
app = ImageUploaderApp(root)
root.title('Image-Comparator')
root.geometry('450x500')
root.resizable(False,False)
root.mainloop()
