from tkinter import *
from PIL import ImageTk,Image 
from tkinter import filedialog
import shutil, atexit, os

def upload_file():
    ### Prompts file upload and then checks if valid
    filename = filedialog.askopenfilename()

    if filename.endswith((".png", ".jpg", ".jpeg")):
        print('Selected:', filename)
        # Create copy of file for use until program termination
        shutil.copyfile(filename, "./Temporary/original.png")
    else:
        print('Invalid file')
        del(filename)

def on_exit():
    shutil.rmtree("Temporary/")
    os.mkdir("Temporary/")

def main_loop():
    ## MAIN PROGRAM LOOP

    path = "./Temporary/original.png"

    loaded_img = Image.open(path) if os.path.exists(path) else None
    img = ImageTk.PhotoImage(loaded_img) if os.path.exists(path) else icon
    image.image = img

    image.configure(image=img)

    root.after(1, main_loop)

# INITIALISATION
root = Tk()
icon = ImageTk.PhotoImage(Image.open("./Assets/icon.png"))
root.title("Intellogo")
root.iconphoto(False, icon)
root.geometry("500x500")

# DISPLAY
button = Button(root, text='Choose File', command=upload_file)
button.pack()

# canvas = Canvas(root, width = 500, height = 500)  
# canvas.pack() 

image = Label(root, width = 500, height = 500)
image.pack()

root.after(10, main_loop)
root.mainloop()

# EXIT MANAGER
atexit.register(on_exit)