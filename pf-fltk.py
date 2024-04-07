from PIL import Image, ImageTk, ImageEnhance
from tkinter import Tk, Label, Frame
import time
import os
import sys

def calculate_total_size(pics):
    total_size = 0
    for pic in pics:
        total_size += sys.getsizeof(pic)
    return total_size / (1024 * 1024)

def get_pics():
    pics = []
    pic_path = "/home/pi/Pictures/MasterPicsResize_SPLIT/"
    # Walk the directory at pic_path and add the complete path of each image file to pics
    for root, dirs, files in os.walk(pic_path):
        for file in files:
            if file.endswith(".jpg"):
                print(file)
                pics.append(os.path.join(root, file))
    total_size = calculate_total_size(pics)
    print(f"Total size of image strings: {total_size:.2f} MB")
    return pics





def main(pics):
    root = Tk()
    root.title("Image Viewer")

    # root.geometry("1000x563")
    
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.overrideredirect(True)
    def end_fullscreen(event=None):
        root.overrideredirect(False)

    root.bind("<Escape>", end_fullscreen)


    # Create a frame to hold the image
    image_frame = Frame(root, bg='black')
    image_frame.pack(fill="both", expand=True)

    # Image label
    image_label = Label(image_frame, bg='black')
    image_label.place(relx=0.5, rely=0.5, anchor='center')

    

    # Function to display an image
    def display_image(path):
        # Load the image using PIL
        imz = Image.open(path)
        # Get the image size
        width, height = imz.size
        print((width, height))
        aspratio = width / height
        img = None
        if width > height:
            newheight = 1000 // aspratio
            img = imz.resize((1000, int(newheight)))  # Resize image to fit the window
        elif width < height:
            newwidth = 825 * aspratio
            img = imz.resize((int(newwidth), 825))
        else:
            img = imz.resize((1000, 1000))


        # Fade in
        for i in range(10):
            enhancer = ImageEnhance.Brightness(img)
            img_enhanced = enhancer.enhance(i / 20)
            photo = ImageTk.PhotoImage(img_enhanced)
            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            root.update()
            root.after(100)

        # Display for a duration
        root.after(3000)

        # Fade out
        for i in range(10, -1, -1):
            enhancer = ImageEnhance.Brightness(img)
            img_enhanced = enhancer.enhance(i / 20)
            photo = ImageTk.PhotoImage(img_enhanced)
            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            root.update()
            root.after(100)

    # Loop through the image list
    while True:
        for pic in pics:
            display_image(pic)

    root.mainloop()

if __name__ == "__main__":
    pics = get_pics()
    main(pics)