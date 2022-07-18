import tkinter as tk
from tkinter import filedialog as fd


def selectFile():
    file = fd.askopenfilename()
    print(file)
    
    return file

#Define window properties
window = tk.Tk()
window.title('Netflix Analyzer')
window.resizable('false', 'false')
window.geometry('800x600')


fileButton = tk.Button(window, text="File", command=selectFile)

fileButton.pack()

fileField = tk.Entry(window)
fileField.pack()

window.mainloop()

