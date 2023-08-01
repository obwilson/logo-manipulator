from tkinter import *
from tkinter import ttk
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
root.geometry("500x600")

# Tabs
tabs = ttk.Notebook(root)
tabs.pack(pady=15)

scale_tab = Frame(tabs, width=500, height=500, bg="Blue")
colourblind_tab = Frame(tabs, width=500, height=500, bg="Red")
blur_tab = Frame(tabs, width=500, height=500, bg="Blue")
pixel_tab = Frame(tabs, width=500, height=500, bg="Red")
bw_tab = Frame(tabs, width=500, height=500, bg="Blue")

scale_tab.pack(fill="both", expand=1)
colourblind_tab.pack(fill="both", expand=1)
blur_tab.pack(fill="both", expand=1)
pixel_tab.pack(fill="both", expand=1)
bw_tab.pack(fill="both", expand=1)

tabs.add(scale_tab, text="Scaled")
tabs.add(colourblind_tab, text="Colourblind")
tabs.add(blur_tab, text="Blurred")
tabs.add(pixel_tab, text="Pixelated")
tabs.add(bw_tab, text="Black/White")


# DISPLAY
button = Button(root, text='Choose File', command=upload_file)
button.pack() 

image = Label(scale_tab, width = 500, height = 500)
image.pack()

root.after(1, main_loop)
root.mainloop()

# EXIT MANAGER
atexit.register(on_exit)