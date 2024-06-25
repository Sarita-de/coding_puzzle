import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle



class TodoApp:
    def __init__(my, box):
        my.box = box
        root.title(" to-do-list")
        root.geometry=("500 X 250")
        root.config(background="")


   

        my.frame = ttk.Frame(box)
        my.frame.pack()

        my.task_entry = ttk.Entry(my.frame)
        my.task_entry.pack(pady=15)

        my.add_button = ttk.Button(my.frame, text="ADD TASK", command=my.add_task)
        my.add_button.pack(pady=15)
        print("successfully the new task added")

        my.task_listbox = tk.Listbox(my.frame, width=40)
        my.task_listbox.pack(pady=15)

        my.delete_button = ttk.Button(my.frame, text="DELETE", command=my.delete_task)
        my.delete_button.pack(pady=15)
        print("Task has been deleted")

        my.complete_button = ttk.Button(my.frame, text="MARK AS COMPLETE", command=my.complete_task)
        my.complete_button.pack(pady=15)
        print("marked")

        my.save_button = ttk.Button(my.frame, text= "SAVE TASK" , command=my.save_task)
        my.save_button.pack(pady=15)
        print("SAVED")

        my.tasks = []

    def add_task(my):
        task = my.task_entry.get().strip()
        if task:
            my.tasks.append(task)
            my.task_listbox.insert(tk.END, task)
            my.task_entry.delete(0, tk.END)

    def delete_task(my):
        selected = my.task_listbox.curselection()
        if selected:
            my.tasks.pop(selected[0])
            my.task_listbox.delete(selected[0])

    def complete_task(my):
        selected = my.task_listbox.curselection()
        if selected:
            task = my.tasks[selected[0]]
            my.tasks.pop(selected[0])
            my.task_listbox.delete(selected[0])
            my.task_listbox.insert(tk.END, f"[COMPLETED] {task}")

    def save_task(my):
        selected = my.task_listbox.curselection()
        if selected:
            my.tasks.pop(selected[0])
            my.task_listbox.delete(selected[0])  

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
