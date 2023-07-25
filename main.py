import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()

    if filename.endswith((".png", ".jpg", ".jpeg", ".svg")):
        print('Selected:', filename)
    else:
        print('Invalid file')
        del(filename)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()