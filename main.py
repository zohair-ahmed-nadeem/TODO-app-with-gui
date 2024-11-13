import tkinter as tk
from tkinter import *

status ="n/a"

def add_task():
    task = task_entry.get()
    time = time_entry.get()
    if task and time:
        list1.insert(END, task)
        list2.insert(END, time)
        task_entry.delete(0, END)
        time_entry.delete(0, END)

def delete_task():
    try:
        selected_task_index = list1.curselection()[0]
        list1.delete(selected_task_index)
        list2.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("TODO by ZOHAIR AHMED")
root.geometry("410x590")
root.resizable(False,False)


# Create and place the headings
head1 = tk.Label(root, text="Tasks", font=("Arial", 16))
head1.grid(row=0, column=0, sticky="w", padx=50, pady=(10, 0))

head2 = tk.Label(root, text="Time", font=("Arial", 16))
head2.grid(row=0, column=1, sticky="e", padx=100, pady=(10, 0))

# Create and place the listboxes and scrollbar
scrollbar = Scrollbar(root)
list1 = Listbox(root, height=25, width=30, font=("Arial", 10), activestyle='dotbox', yscrollcommand=scrollbar.set)
list2 = Listbox(root, height=25, width=10, font=("Arial", 10), activestyle='dotbox', yscrollcommand=scrollbar.set)
scrollbar.config(command=lambda *args: [list1.yview(*args), list2.yview(*args)])
scrollbar.grid(row=1, column=2, sticky='ns', pady=(0, 10))

list1.grid(row=1, column=0, padx=10, pady=(0, 10))
list2.grid(row=1, column=1, pady=(0, 10))

# Example task
list1.insert(1, "Example Task")
list2.insert(1, "12:00 PM")

# Task and time entry fields
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=2, column=0, padx=10, pady=(10, 0))

time_entry = tk.Entry(root, width=10)
time_entry.grid(row=2, column=1, pady=(10, 0))

# Add and delete buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, padx=10, pady=(10, 10))

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=3, column=1, pady=(10, 10))


root.mainloop()
