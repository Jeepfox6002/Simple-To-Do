import tkinter as tk
import json
from PIL import Image, ImageTk
import time

Task_height = 580
Task_width = 400

Time_until_height = 280
Time_until_width = 570

Time_left_height = 280
Time_left_width = 570

Task_panel_height = 150

p = "Placeholder"

needed_data = {
    "Tasks": []
}

def new_file():
    with open("data.json", "w") as f:
        json.dump(needed_data, f, indent=4)

def save_file():
    with open("data.json", "w") as file:
        json.dump(needed_data, file, indent=4, sort_keys=True)

def settings():
    root_settings = tk.Toplevel(root)
    root_settings.geometry("300x200")
    root_settings.config(bg="#2F2F2F")
    root_settings.title("Settings")

def edit_tasks(event=None):
    print(p)

def add_tasks(event=None):
    root__add_task = tk.Toplevel(root)
    root__add_task.geometry("450x325")
    root__add_task.config(bg="#2F2F2F")
    root__add_task.title("Add task")

    task_name = tk.Entry(root__add_task, bg="#292929")
    task_name.place(x=10,y=10, width=430)
    task_name.insert(0,"Type the name of your task here!")
    placeholder = "Type the name of your task here!"
    name = task_name.get()
    def remove_placeholder(event):
        if name == placeholder:
            task_name.delete(0,tk.END)
    task_name.bind("<FocusIn>",remove_placeholder)

    submit = tk.Button(root__add_task,background="#292929", text="Submit",fg="White")
    submit.place(x=370,y=285,width=70,height=30)

root = tk.Tk()
root.geometry("1000x600")
root.config(bg="#2F2F2F")
root.title("Simple To-Do")
root.resizable(False, False)

tasks_canvas = tk.Canvas(root, bg="#292929", width=Task_width, height=Task_height)
tasks_canvas.propagate(False)
tasks_canvas.place(x=10, y=10, width=Task_width, height=Task_height)

task_title = tasks_canvas.create_text(40,20, text="Tasks:", fill="white", font=("Arial", 15, "normal"))

original_edit_image = Image.open("Simple To Do/EditIcon.png")
original_add_image = Image.open("Simple To Do/AddIcon.png")
add_image = ImageTk.PhotoImage(original_add_image.resize((30, 30)))
edit_image = ImageTk.PhotoImage(original_edit_image.resize((30, 30)))
edit_button = tk.Label(root, image=edit_image, bg="#292929")
edit_button.place(x=360, y=15)
edit_button.bind("<Button-1>", edit_tasks)
add_button = tk.Label(root, image=add_image, bg="#292929")
add_button.place(x=320, y=15)
add_button.bind("<Button-1>", add_tasks)

time_until_canvas = tk.Canvas(root, bg="#292929", width=Time_until_width, height=Time_until_height)
time_until_canvas.propagate(False)
time_until_canvas.place(x=420, y=10, width=Time_until_width, height=Time_until_height)

time_left_canvas = tk.Canvas(root, bg="#292929", width=Time_left_width, height=Time_left_height)
time_left_canvas.propagate(False)
time_left_canvas.place(x=420, y=310, width=Time_left_width, height=Time_left_height)

#menubar = tk.Menu(root)

#file_menu = tk.Menu(menubar, tearoff=0)
#file_menu.add_command(label="New", command=new_file)
#file_menu.add_command(label="Open", command=open_file)
#file_menu.add_command(label="Save", command=save_file)
#file_menu.add_command(label="Settings", command=settings)

#menubar.add_cascade(label="File", menu=file_menu)

#root.config(menu=menubar)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()
