from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 
from tkinter import filedialog
import shutil, atexit, os

def upload_file():
    ### Prompts file upload and then checks if valid
    filename = filedialog.askopenfilename()

    if filename.endswith((".png", ".jpg", ".jpeg")):
        print("Selected:", filename)
        # Create copy of file for use until program termination
        shutil.copyfile(filename, "./Temporary/original.png")
        original = Image.open(filename)
        resized = original.resize((500, 500))
        resized.save("./Temporary/resized.png")

        scale_1 = original.resize((250, 250))
        scale_1.save("./Temporary/scale_1.png")
        scale_2 = original.resize((100, 100))
        scale_2.save("./Temporary/scale_2.png")
        scale_3 = original.resize((40, 40))
        scale_3.save("./Temporary/scale_3.png")

        balance()
    else:
        print("Invalid file")
        del(filename)

def balance():
    file = Image.open("./Temporary/resized.png")
    overlay = Image.open("./Assets/balance_overlay.png")
    file.paste(overlay, (0, 0), overlay)
    file.save("./Temporary/balanced.png")

def colourblind():
    pass

def pixelate():
    pass

def blur():
    pass

def on_exit():
    shutil.rmtree("Temporary/")
    os.mkdir("Temporary/")

def main_loop():
    ## MAIN PROGRAM LOOP

    path = "./Temporary/resized.png"
    balance_path = "./Temporary/balanced.png"
    scale_1_path = "./Temporary/scale_1.png"
    scale_2_path = "./Temporary/scale_2.png"
    scale_3_path = "./Temporary/scale_3.png"

    loaded_img = Image.open(path) if os.path.exists(path) else None
    img = ImageTk.PhotoImage(loaded_img) if os.path.exists(path) else open
    file_image.image = img
    file_image.configure(image=img)

    balance_loaded_img = Image.open(balance_path) if os.path.exists(balance_path) else None
    balance_img = ImageTk.PhotoImage(balance_loaded_img) if os.path.exists(balance_path) else default
    balance_image.image = balance_img
    balance_image.configure(image=balance_img)

    scale_1_loaded_img = Image.open(scale_1_path) if os.path.exists(scale_1_path) else None
    scale_1_img = ImageTk.PhotoImage(scale_1_loaded_img) if os.path.exists(scale_1_path) else default
    scale_1_image.image = scale_1_img
    scale_1_image.configure(image=scale_1_img)

    scale_2_loaded_img = Image.open(scale_2_path) if os.path.exists(scale_2_path) else None
    scale_2_img = ImageTk.PhotoImage(scale_2_loaded_img) if os.path.exists(scale_2_path) else default
    scale_2_image.image = scale_2_img
    scale_2_image.configure(image=scale_2_img)

    scale_3_loaded_img = Image.open(scale_3_path) if os.path.exists(scale_3_path) else None
    scale_3_img = ImageTk.PhotoImage(scale_3_loaded_img) if os.path.exists(scale_3_path) else default
    scale_3_image.image = scale_3_img
    scale_3_image.configure(image=scale_3_img)

    root.after(1, main_loop)

# INITIALISATION
root = Tk()
icon = ImageTk.PhotoImage(Image.open("./Assets/icon.png"))
open = ImageTk.PhotoImage(Image.open("./Assets/open_file.png"))
default = ImageTk.PhotoImage(Image.open("./Assets/default_image.png"))
root.title("Intellogo")
root.iconphoto(False, icon)
root.geometry("500x600")

# TABS SETUP
tabs = ttk.Notebook(root)
tabs.pack(pady=15)

original_tab = Frame(tabs, width=500, height=500)
balance_tab = Frame(tabs, width=500, height=500)
scale_tab = Frame(tabs, width=500, height=500)
colourblind_tab = Frame(tabs, width=500, height=500)
blur_tab = Frame(tabs, width=500, height=500)
pixel_tab = Frame(tabs, width=500, height=500)
bw_tab = Frame(tabs, width=500, height=500)

original_tab.pack(fill="both", expand=1)
balance_tab.pack(fill="both", expand=1)
scale_tab.pack(fill="both", expand=1)
colourblind_tab.pack(fill="both", expand=1)
blur_tab.pack(fill="both", expand=1)
pixel_tab.pack(fill="both", expand=1)
bw_tab.pack(fill="both", expand=1)

tabs.add(original_tab, text="Original")
tabs.add(balance_tab, text="Balance")
tabs.add(scale_tab, text="Scaled")
tabs.add(colourblind_tab, text="Colourblind")
tabs.add(blur_tab, text="Blurred")
tabs.add(pixel_tab, text="Pixelated")
tabs.add(bw_tab, text="Black/White")

# DISPLAY
button = Button(root, text="Choose File", command=upload_file)
button.pack() 

file_image = Label(original_tab, width=500, height=500)
file_image.pack()

balance_image = Label(balance_tab, width=500, height=500)
balance_image.pack()

scale_1_image = Label(scale_tab, width=250, height=250)
scale_1_image.pack()
scale_2_image = Label(scale_tab, width=100, height=100)
scale_2_image.pack()
scale_3_image = Label(scale_tab, width=40, height=40)
scale_3_image.pack()

root.after(1, main_loop)
root.mainloop()

# EXIT MANAGER
atexit.register(on_exit)