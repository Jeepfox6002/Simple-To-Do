import tkinter as tk

def new_file():
    print("Placeholder")

def open_file():
    print("placeholder")

def save_file():
    print("placeholder")

def save_file_as():
    print("placeholder")

root = tk.Tk()
root.geometry("600x400")

text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)

menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()