import tkinter as tk
import json
from tkinter import Tk

p = "Placeholder"

def save_file():
    with open("data.json", "w") as file:
        json.dump(needed_data, file, indent=4, sort_keys=True)


def submit_task_add(event=None):
    print(p)

def add_tasks(event=None):
    root_add_task = tk.Tk()
    root_add_task.geometry("450x325")
    root_add_task.config(bg="#2F2F2F")
    root_add_task.title("Add task")

    task_name = tk.Entry(root_add_task, bg="#292929")
    task_name.place(x=10,y=10, width=430,height=40)
    placeholder = "Type the name of your task here!"
    task_name.insert(0,placeholder)
    name = task_name.get()
    def remove_placeholder(event):
        if name == placeholder:
            task_name.delete(0,tk.END)
    task_name.bind("<FocusIn>",remove_placeholder)

    selection_one = tk.Label(root_add_task,bg="#292929",fg="White",text="When will this task start?")
    selection_one.place(x=10, y=60, height=40, width=170)

    at_hour = tk.Entry(root_add_task, bg="#292929")
    at_hour.place(x=190,y=60,height=40,width=70)
    at_hour.insert(0, "Hour")

    at_minute = tk.Entry(root_add_task, bg="#292929")
    at_minute.place(x=270,y=60,width=70,height=40)
    at_minute.insert(0,"Minute")

    hour = at_hour.get()
    minute = at_minute.get()

    def remove_hour_place(event):
        if hour == "Hour":
            at_hour.delete(0, tk.END)
    at_hour.bind("<FocusIn>", remove_hour_place)

    def remove_minute_place(event):
        if minute == "Minute":
            at_minute.delete(0,tk.END)
    at_minute.bind("<FocusIn>",remove_minute_place)

    submit = tk.Label(root_add_task,bg="#292929", text="Submit",fg="White")
    submit.place(x=370,y=285,width=70,height=30)
    submit.bind("<Button-1>", submit_task_add)

    root_add_task.mainloop()
