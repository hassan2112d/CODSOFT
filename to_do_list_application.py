import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = task_list.curselection()[0]
        selected_task = task_list.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def save_updated_task():
    try:
        selected_task_index = task_list.curselection()[0]
        updated_task = task_entry.get()
        if updated_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

root = tk.Tk()
root.title("To-Do List")

task_list = tk.Listbox(root, selectmode=tk.SINGLE)
task_list.pack(pady=10)

task_entry = tk.Entry(root)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
save_button = tk.Button(root, text="Save Updated Task", command=save_updated_task)

add_button.pack()
delete_button.pack()
update_button.pack()
save_button.pack()

root.mainloop()
