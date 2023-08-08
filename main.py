from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 
from tkinter import filedialog
from daltonlens import convert, simulate, generate
import numpy as np
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
        colourblind()
    else:
        print("Invalid file")
        del(filename)

def balance():
    file = Image.open("./Temporary/resized.png")
    overlay = Image.open("./Assets/balance_overlay.png")
    file.paste(overlay, (0, 0), overlay)
    file.save("./Temporary/balanced.png")

def colourblind():
    file = np.asarray(Image.open("./Temporary/resized.png").resize((250, 250)).convert("RGB"))
    simulator = simulate.Simulator_Brettel1997()
    protan_img = simulator.simulate_cvd (file, simulate.Deficiency.PROTAN, severity=1)
    deutan_img = simulator.simulate_cvd (file, simulate.Deficiency.DEUTAN, severity=1)
    tritan_img = simulator.simulate_cvd (file, simulate.Deficiency.TRITAN, severity=1)
    
    protan = Image.fromarray(protan_img)
    deutan = Image.fromarray(deutan_img)
    tritan = Image.fromarray(tritan_img)

    protan.save("./Temporary/protan.png")
    deutan.save("./Temporary/deutan.png")
    tritan.save("./Temporary/tritan.png")


def pixelate():
    pass

def blur():
    pass

def on_exit():
    shutil.rmtree("Temporary/")
    os.mkdir("Temporary/")

def main_loop():
    ### MAIN PROGRAM LOOP

    PATH = "./Temporary/resized.png"
    BALANCE_PATH = "./Temporary/balanced.png"
    SCALE_1_PATH = "./Temporary/scale_1.png"
    SCALE_2_PATH = "./Temporary/scale_2.png"
    SCALE_3_PATH = "./Temporary/scale_3.png"
    PROTAN_PATH = "./Temporary/protan.png"
    DEUTAN_PATH = "./Temporary/deutan.png"
    TRITAN_PATH = "./Temporary/tritan.png"

    # ORIGINAL TAB
    loaded_img = Image.open(PATH) if os.path.exists(PATH) else None
    img = ImageTk.PhotoImage(loaded_img) if os.path.exists(PATH) else OPEN
    file_image.image = img
    file_image.configure(image=img)

    # BALANCE TAB
    balance_loaded_img = Image.open(BALANCE_PATH) if os.path.exists(BALANCE_PATH) else None
    balance_img = ImageTk.PhotoImage(balance_loaded_img) if os.path.exists(BALANCE_PATH) else DEFAULT
    balance_image.image = balance_img
    balance_image.configure(image=balance_img)

    # SCALE TAB
    scale_1_loaded_img = Image.open(SCALE_1_PATH) if os.path.exists(SCALE_1_PATH) else None
    scale_1_img = ImageTk.PhotoImage(scale_1_loaded_img) if os.path.exists(SCALE_1_PATH) else SCALE_1_DEFAULT
    scale_1_image.image = scale_1_img
    scale_1_image.configure(image=scale_1_img)

    scale_2_loaded_img = Image.open(SCALE_2_PATH) if os.path.exists(SCALE_2_PATH) else None
    scale_2_img = ImageTk.PhotoImage(scale_2_loaded_img) if os.path.exists(SCALE_2_PATH) else SCALE_2_DEFAULT
    scale_2_image.image = scale_2_img
    scale_2_image.configure(image=scale_2_img)

    scale_3_loaded_img = Image.open(SCALE_3_PATH) if os.path.exists(SCALE_3_PATH) else None
    scale_3_img = ImageTk.PhotoImage(scale_3_loaded_img) if os.path.exists(SCALE_3_PATH) else SCALE_3_DEFAULT
    scale_3_image.image = scale_3_img
    scale_3_image.configure(image=scale_3_img)

    # COLOURBLIND TAB
    loaded_original = Image.open(PATH).resize((250, 250)) if os.path.exists(PATH) else None
    original = ImageTk.PhotoImage(loaded_original) if os.path.exists(PATH) else DEFAULT
    original_image.image = original
    original_image.configure(image=original)

    protan_img = Image.open(PROTAN_PATH) if os.path.exists(PROTAN_PATH) else None
    protan_img = ImageTk.PhotoImage(protan_img) if os.path.exists(PROTAN_PATH) else DEFAULT
    protan_image.image = protan_img
    protan_image.configure(image=protan_img)

    deutan_img = Image.open(DEUTAN_PATH) if os.path.exists(DEUTAN_PATH) else None
    deutan_img = ImageTk.PhotoImage(deutan_img) if os.path.exists(DEUTAN_PATH) else DEFAULT
    deutan_image.image = deutan_img
    deutan_image.configure(image=deutan_img)

    tritan_img = Image.open(TRITAN_PATH) if os.path.exists(TRITAN_PATH) else None
    tritan_img = ImageTk.PhotoImage(tritan_img) if os.path.exists(TRITAN_PATH) else DEFAULT
    tritan_image.image = tritan_img
    tritan_image.configure(image=tritan_img)

    root.after(1, main_loop)

# INITIALISATION
root = Tk()

ICON = ImageTk.PhotoImage(Image.open("./Assets/icon.png"))
OPEN = ImageTk.PhotoImage(Image.open("./Assets/open_file.png"))
DEFAULT = ImageTk.PhotoImage(Image.open("./Assets/default_image.png"))
SCALE_1_DEFAULT = ImageTk.PhotoImage(Image.open("./Assets/scale_1_default.png"))
SCALE_2_DEFAULT = ImageTk.PhotoImage(Image.open("./Assets/scale_2_default.png"))
SCALE_3_DEFAULT = ImageTk.PhotoImage(Image.open("./Assets/scale_3_default.png"))

root.title("Intellogo")
root.iconphoto(False, ICON)
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

original_frame = Frame(colourblind_tab, width=250, height=250)
original_frame.place(x=0,y=0)
protan_frame = Frame(colourblind_tab, width=250, height=250)
protan_frame.place(x=250,y=0)
deutan_frame = Frame(colourblind_tab, width=250, height=250)
deutan_frame.place(x=0,y=250)
tritan_frame = Frame(colourblind_tab, width=250, height=250)
tritan_frame.place(x=250,y=250)

original_image = Label(original_frame, width=250, height=250)
original_image.pack()
protan_image = Label(protan_frame, width=250, height=250)
protan_image.pack()
deutan_image = Label(deutan_frame, width=250, height=250)
deutan_image.pack()
tritan_image = Label(tritan_frame, width=250, height=250)
tritan_image.pack()

root.after(1, main_loop)
root.mainloop()

# EXIT MANAGER
atexit.register(on_exit)