from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image,ImageFilter
from tkinter import filedialog
from daltonlens import simulate
import numpy as np
import shutil, atexit, os

def upload_file():
    ### Prompts file upload and then checks if valid
    filename = filedialog.askopenfilename()

    make_files(filename)
    
def make_files(filename):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        
        print("Selected:", filename)
        # Create copy of file for use until program termination
        shutil.copyfile(filename, "./Temporary/original.png")
        original = Image.open(filename)
        if original.mode == 'CMYK':
            original = original.convert('RGB')
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
        blur()
        pixelate()
        black_white()
    else:
        messagebox.showerror("Intellogo",
        "Error: Invalid filetype, please use .png or .jpg files only.")
        print("Invalid file")
        del(filename)


def balance():
    file = Image.open("./Temporary/resized.png")
    overlay = Image.open("./Assets/balance_overlay.png")
    file.paste(overlay, (0, 0), overlay)
    file.save("./Temporary/balanced.png")

def colourblind():
    file = np.asarray(
    Image.open("./Temporary/resized.png").resize((250, 250)).convert("RGB")
    )
    # file.convert("RGB")
    sim = simulate.Simulator_Brettel1997()
    protan_img = sim.simulate_cvd (file, simulate.Deficiency.PROTAN, severity=1)
    deutan_img = sim.simulate_cvd (file, simulate.Deficiency.DEUTAN, severity=1)
    tritan_img = sim.simulate_cvd (file, simulate.Deficiency.TRITAN, severity=1)

    protan = Image.fromarray(protan_img)
    deutan = Image.fromarray(deutan_img)
    tritan = Image.fromarray(tritan_img)

    protan.save("./Temporary/protan.png")
    deutan.save("./Temporary/deutan.png")
    tritan.save("./Temporary/tritan.png")


def blur():
    file = Image.open("./Temporary/resized.png")
    blurred = file.filter(ImageFilter. GaussianBlur(radius=20))
    blurred.save("./Temporary/blurred.png")

def pixelate():
    file = Image.open("./Temporary/resized.png")
    downsized = file.resize((32, 32), resample=Image.Resampling.BILINEAR)
    pixelated = downsized.resize(file.size, Image.Resampling.NEAREST)
    pixelated.save("./Temporary/pixelated.png")

def black_white():
    file = Image.open("./Temporary/resized.png")
    grayscale = file.convert("L")

    grayscale.save("./Temporary/grayscale.png")

def on_exit():
    shutil.rmtree("Temporary/")
    os.mkdir("Temporary/")

def main_loop():
    ### MAIN PROGRAM LOOP

    # ORIGINAL TAB
    img = Image.open(PATH)
    img = ImageTk.PhotoImage(img)
    file_image.image = img
    file_image.configure(image=img)

    # BALANCE TAB
    balance_img = Image.open(BALANCE_PATH)
    balance_img = ImageTk.PhotoImage(balance_img)
    balance_image.image = balance_img
    balance_image.configure(image=balance_img)

    # SCALE TAB
    scale_1_img = Image.open(SCALE_1_PATH)
    scale_1_img = ImageTk.PhotoImage(scale_1_img)
    scale_1_image.image = scale_1_img
    scale_1_image.configure(image=scale_1_img)

    scale_2_img = Image.open(SCALE_2_PATH)
    scale_2_img = ImageTk.PhotoImage(scale_2_img)
    scale_2_image.image = scale_2_img
    scale_2_image.configure(image=scale_2_img)

    scale_3_img = Image.open(SCALE_3_PATH)
    scale_3_img = ImageTk.PhotoImage(scale_3_img)
    scale_3_image.image = scale_3_img
    scale_3_image.configure(image=scale_3_img)

    # COLOURBLIND TAB
    loaded_original = Image.open(PATH).resize((250, 250))
    original = ImageTk.PhotoImage(loaded_original)
    original_image.image = original
    original_image.configure(image=original)

    protan_img = Image.open(PROTAN_PATH)
    protan_img = ImageTk.PhotoImage(protan_img)
    protan_image.image = protan_img
    protan_image.configure(image=protan_img)

    deutan_img = Image.open(DEUTAN_PATH)
    deutan_img = ImageTk.PhotoImage(deutan_img)
    deutan_image.image = deutan_img
    deutan_image.configure(image=deutan_img)

    tritan_img = Image.open(TRITAN_PATH)
    tritan_img = ImageTk.PhotoImage(tritan_img)
    tritan_image.image = tritan_img
    tritan_image.configure(image=tritan_img)

    # BLUR TAB
    blur_img = Image.open(BLUR_PATH)
    blur_img = ImageTk.PhotoImage(blur_img)
    blur_image.image = blur_img
    blur_image.configure(image=blur_img)

    # PIXELATE TAB
    pixel_img = Image.open(PIXEL_PATH)
    pixel_img = ImageTk.PhotoImage(pixel_img)
    pixel_image.image = pixel_img
    pixel_image.configure(image=pixel_img)

    # BLACK AND WHITE TAB
    grayscale_img = Image.open(GRAYSCALE_PATH)
    grayscale_img = ImageTk.PhotoImage(grayscale_img)
    grayscale_image.image = grayscale_img
    grayscale_image.configure(image=grayscale_img)

    root.after(1, main_loop)

# INITIALISATION
root = Tk()

ICON = ImageTk.PhotoImage(Image.open("./Assets/icon.png"))
OPEN = ImageTk.PhotoImage(Image.open("./Assets/open_file.png"))
PATH = "./Temporary/resized.png"
BALANCE_PATH = "./Temporary/balanced.png"
SCALE_1_PATH = "./Temporary/scale_1.png"
SCALE_2_PATH = "./Temporary/scale_2.png"
SCALE_3_PATH = "./Temporary/scale_3.png"
PROTAN_PATH = "./Temporary/protan.png"
DEUTAN_PATH = "./Temporary/deutan.png"
TRITAN_PATH = "./Temporary/tritan.png"
BLUR_PATH = "./Temporary/blurred.png"
PIXEL_PATH = "./Temporary/pixelated.png"
SILHOUETTE_PATH = "./Temporary/silhouette.png"
GRAYSCALE_PATH = "./Temporary/grayscale.png"

make_files("./Assets/icon.png")

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

blur_image = Label(blur_tab, width=500, height=500)
blur_image.pack()

pixel_image = Label(pixel_tab, width=500, height=500)
pixel_image.pack()

grayscale_image = Label(bw_tab, width=500, height=500)
grayscale_image.pack()

root.after(1, main_loop)
root.mainloop()

# EXIT MANAGER
atexit.register(on_exit)