import tkinter as tk
import json
from tkinter import ttk

p = "Placeholder"

def add_tasks(sync_task, event=None):
    root_add_task = tk.Toplevel()
    root_add_task.geometry("450x160")
    root_add_task.config(bg="#2F2F2F")
    root_add_task.title("Add task")

    task_name = tk.Entry(root_add_task, bg="#292929", highlightbackground="#1a1a1a", highlightcolor="#1a1a1a", highlightthickness=2, fg="White", bd=0)
    task_name.place(x=10,y=10, width=430,height=40)
    placeholder = "Type the name of your task here!"
    task_name.insert(0,placeholder)
    def remove_placeholder(event):
        if task_name.get() == placeholder:
            task_name.delete(0,tk.END)
    task_name.bind("<FocusIn>",remove_placeholder)

    selection_one = tk.Label(root_add_task,bg="#292929",fg="White",text="When will this task start?", highlightbackground="#1a1a1a", highlightthickness=2)
    selection_one.place(x=10, y=60, height=40, width=170)

    at_hour = tk.Entry(root_add_task, bg="#292929", highlightbackground="#1a1a1a",highlightcolor="#1a1a1a", highlightthickness=2, fg="White", bd=0)
    at_hour.place(x=190,y=60,height=40,width=70)
    at_hour.insert(0, "Hour")

    at_minute = tk.Entry(root_add_task, bg="#292929", highlightbackground="#1a1a1a", highlightcolor="#1a1a1a", highlightthickness=2, fg="White", bd=0)
    at_minute.place(x=270,y=60,width=70,height=40)
    at_minute.insert(0,"Minute")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "Time_Day_Theme.TCombobox",
        fieldbackground="#292929",
        background="#292929",
        foreground="white",
        arrowcolor="white",
        bordercolor="#1a1a1a",
        darkcolor="#1a1a1a",
        lightcolor="#1a1a1a",
        borderwidth=2
    )
    style.map(
        "Time_Day_Theme.TCombobox",
        fieldbackground=[("readonly", "#292929"), ("active", "#292929")],
        background=[("active", "#292929"), ("active", "#292929")],
        foreground=[("readonly", "white"),("active", "white")],
        selectbackground=[("readonly", "#292929"), ("active", "#292929")],
        selectforeground=[("readonly", "white"),("active", "white")]
    )

    options = ["Am","Pm"]
    time_day = ttk.Combobox(root_add_task, values=options, state="readonly", style="Time_Day_Theme.TCombobox")
    time_day.set("Am or Pm")
    time_day.place(x=350, y=60, width=90, height=40)

    def remove_hour_place(event):
        if at_hour.get() == "Hour":
            at_hour.delete(0, tk.END)
    at_hour.bind("<FocusIn>", remove_hour_place)

    def remove_minute_place(event):
        if at_minute.get() == "Minute":
            at_minute.delete(0,tk.END)
    at_minute.bind("<FocusIn>",remove_minute_place)

    def submit_task_add(event=None):

        try:
            with open("Tasks.json", "r") as file:
                task_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            task_data = {}

        task_name_value = task_name.get()
        task_data[task_name_value] = {
            "Hours": at_hour.get(),
            "Minutes": at_minute.get(),
            "Time of day": time_day.get()
        }
        with open("Tasks.json", "w") as file:
            json.dump(task_data, file, indent=4)

        sync_task()

    submit = tk.Label(root_add_task,bg="#292929", text="Submit",fg="White", highlightbackground="#1a1a1a", highlightthickness=2)
    submit.place(x=10,y=110,width=430,height=40)
    submit.bind("<Button-1>", submit_task_add)



    root_add_task.mainloop()
