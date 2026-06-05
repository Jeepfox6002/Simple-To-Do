import tkinter as tk
import json
from PIL import Image, ImageTk

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

def edit_tasks():
    print("Placeholder")

Task_height = 580
Task_width = 400

Time_until_height = 280
Time_until_width = 570

Time_left_height = 280
Time_left_width = 570

root = tk.Tk()
root.geometry("1000x600")
root.config(bg="#2F2F2F")
root.title("Simple To-Do")

tasks_canvas = tk.Canvas(root, bg="#292929", width=Task_width, height=Task_height)
tasks_canvas.propagate(False)
tasks_canvas.place(x=10, y=10, width=Task_width, height=Task_height)

task_title = tasks_canvas.create_text(40,20, text="Tasks:", fill="white", font=("Arial", 15, "normal"))

original_edit_image = Image.open("Simple To Do/EditIcon.png")
edit_image = ImageTk.PhotoImage(original_edit_image.resize((30, 30)))
edit_button = tk.Label(root, image=edit_image, bg="#292929")
edit_button.place(x=360, y=10)
edit_button.bind("<Button-1>", edit_tasks())

time_until_canvas = tk.Canvas(root, bg="#292929", width=Time_until_width, height=Time_until_height)
time_until_canvas.propagate(False)
time_until_canvas.place(x=420, y=10, width=Time_until_width, height=Time_until_height)

time_left_canvas = tk.Canvas(root, bg="#292929", width=Time_left_width, height=Time_left_height)
time_left_canvas.propagate(False)
time_left_canvas.place(x=420, y=310, width=Time_left_width, height=Time_left_height)

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
