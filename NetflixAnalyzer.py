import tkinter as tk
from tkinter.filedialog import askopenfilename


#Define window properties
window = tk.Tk()
window.title('Netflix Analyzer')
window.resizable('false', 'false')
window.geometry('800x600')

fileButton = tk.Button(window, text="File")

fileButton.pack()

# file = fd.askopenfilename()

window.mainloop()