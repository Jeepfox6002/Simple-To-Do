import tkinter as tk
from PIL import Image, ImageTk
from add_task import add_tasks
from datetime import datetime
import json

Task_height = 50
Task_width = 380

Time_until_height = 280
Time_until_width = 570

Time_left_height = 280
Time_left_width = 570

Task_panel_height = 150

panel_number = 0

p = "Placeholder"

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%p")
    clock_until.config(text=current_time)
    root.after(1000, get_time)

def add_task_panel(hours,minutes,time_of_day,task_name):
    global panel_number
    new_panel = tk.Canvas(tasks_Frame, bg="#292929", width=Task_width, height=Task_height, highlightbackground="#1a1a1a", highlightthickness=2)
    #y = 35 + panel_number * Task_height + 10
    y = 35 + panel_number * (Task_height + 10)
    new_panel.place(x=10, y=y, width=Task_width, height=Task_height, anchor="nw")

    if hours == "Hour" or minutes == "Minute":
        return

    try:
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        return

    formated_time = f"{hours}:{str(minutes).zfill(2)} {time_of_day}"

    new_panel.create_text(5,5,text=task_name,font=("Arial", 11), anchor="nw", fill="white")
    new_panel.create_text(5,20,text="This task happens at: " + formated_time,font=("Arial", 11), anchor="nw", fill="white")

    panel_number += 1

def sync_task():
    with open("Tasks.json", "r") as file:
        task_data = json.load(file)

    for widget in tasks_Frame.winfo_children():
        widget.destroy()

    global panel_number
    panel_number = 0

    for task_id, info in task_data.items():
        add_task_panel(info["Hours"],info["Minutes"],info["Time of day"],info["Task_Name"])

def settings():
    root_settings = tk.Toplevel(root)
    root_settings.geometry("300x200")
    root_settings.config(bg="#2F2F2F")
    root_settings.title("Settings")

def edit_tasks(event=None):
    print(p)

root = tk.Tk()
root.geometry("1000x600")
root.config(bg="#2F2F2F")
root.title("Simple To-Do")
root.resizable(False, False)

tasks_Frame = tk.Frame(root, bg="#292929", width=400, height=580, highlightbackground="#1a1a1a", highlightcolor="#1a1a1a",highlightthickness=2)
tasks_Frame.propagate(False)
tasks_Frame.place(x=10, y=10, width=400, height=580)

task_title = tk.Label(root, bg="#292929",fg="White",text="Tasks:", highlightbackground="#1a1a1a", highlightthickness=2, font=("Arial", 15))
task_title.place(x=10, y=10, width=75, height=30)

original_edit_image = Image.open("EditIcon.png")
original_add_image = Image.open("AddIcon.png")
add_image = ImageTk.PhotoImage(original_add_image.resize((30, 30)))
edit_image = ImageTk.PhotoImage(original_edit_image.resize((30, 30)))
edit_button = tk.Label(root, image=edit_image, bg="#292929")
edit_button.place(x=360, y=15)
edit_button.bind("<Button-1>", edit_tasks)
add_button = tk.Label(root, image=add_image, bg="#292929")
add_button.place(x=320, y=15)
add_button.bind("<Button-1>", lambda event: add_tasks(sync_task, event))

time_until_canvas = tk.Canvas(root, bg="#292929", width=Time_until_width, height=Time_until_height, highlightbackground="#1a1a1a", highlightthickness=2)
time_until_canvas.propagate(False)
time_until_canvas.place(x=420, y=10, width=Time_until_width, height=Time_until_height)

clock_label = tk.Label(root, text="Current Time: ", bg="#292929", fg="white", font=("Arial", 20))
clock_label.place(x=560, y=15, width=300, height=100)
clock_until = tk.Label(root, text="", bg="#292929", fg="white", font=("Arial", 30), highlightbackground="#1a1a1a", highlightthickness=2)
clock_until.place(x=420, y=10, width=Time_until_width, height=Time_until_height)
clock_label.lift(clock_until)

time_left_canvas = tk.Canvas(root, bg="#292929", width=Time_left_width, height=Time_left_height, highlightbackground="#1a1a1a", highlightthickness=2)
time_left_canvas.propagate(False)
time_left_canvas.place(x=420, y=310, width=Time_left_width, height=Time_left_height)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

sync_task()
get_time()

root.mainloop()
