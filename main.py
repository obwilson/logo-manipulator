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

        balance()
    else:
        print("Invalid file")
        del(filename)

def balance():
    file = Image.open("./Temporary/resized.png")
    overlay = Image.open("./Assets/balance_overlay.png")
    file.paste(overlay, (0, 0), overlay)
    file.save("./Temporary/balanced.png")

    # balance = Label(balance_tab, width=500, height=500)
    # balance.image = file
    # balance.pack()

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

    loaded_img = Image.open(path) if os.path.exists(path) else None
    img = ImageTk.PhotoImage(loaded_img) if os.path.exists(path) else default
    file_image.image = img

    file_image.configure(image=img)

    root.after(1, main_loop)

# INITIALISATION
root = Tk()
icon = ImageTk.PhotoImage(Image.open("./Assets/icon.png"))
default = ImageTk.PhotoImage(Image.open("./Assets/open_file.png"))
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

root.after(1, main_loop)
root.mainloop()

# EXIT MANAGER
atexit.register(on_exit)