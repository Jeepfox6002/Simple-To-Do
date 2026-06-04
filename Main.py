import tkinter as tk
import json

needed_data = {
    "Tasks": ["Example 1", "Example 2"]
}

def new_file():
    with open("data.json", "w") as f:
        json.dump(needed_data, f, indent=4)

def open_file():
    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data)

def save_file():
    with open("data.json", "w") as file:
        json.dump(needed_data, file, indent=4, sort_keys=True)

def settings():
    root_settings = tk.Toplevel(root)
    root_settings.geometry("300x200")
    root_settings.config(bg="#2F2F2F")
    root_settings.title("Settings")

root = tk.Tk()
root.geometry("580x355")
root.config(bg="#2F2F2F")

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Settings", command=settings)

menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()
