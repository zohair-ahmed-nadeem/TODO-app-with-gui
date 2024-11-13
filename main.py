import tkinter as tk
from datetime import datetime
import threading
import time
import nortify

# List to store reminders
reminders = []

def add_task():
    task = task_entry.get()
    time_str = time_entry.get()
    try:
        if task and time_str:
            # Check if time format is correct
            reminder_time = datetime.strptime(time_str, "%H:%M").time()
            reminders.append((task, reminder_time))
            list1.insert(tk.END, task)
            list2.insert(tk.END, time_str)
            task_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
            sta.set("Task added successfully!")
        else:
            sta.set("Please enter both task and time.")
    except ValueError:
        sta.set("Invalid time format. Please use HH:MM.")

def delete_task():
    try:
        selected_task_index = list1.curselection()[0]
        list1.delete(selected_task_index)
        list2.delete(selected_task_index)
        del reminders[selected_task_index]
        sta.set("Task deleted successfully!")
    except IndexError:
        sta.set("No task selected.")

def update_time():
    current_time = datetime.now().strftime("Current time is: %H:%M")
    times.config(text=current_time)
    root.after(1000, update_time)  # Update time every second

def check_reminders():
    while True:
        current_time = datetime.now().time()
        for reminder, reminder_time in reminders[:]:
            if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
                nortify.send_notification("Reminder", reminder, wait_time=2)
                reminders.remove((reminder, reminder_time))
        time.sleep(30)

# Start the reminder checking thread
reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

root = tk.Tk()
root.title("TODO by ZOHAIR AHMED")
root.geometry("410x590")
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Create and place the headings
head1 = tk.Label(root, text="Tasks", font=("Arial", 16))
head1.grid(row=0, column=0, sticky="w", padx=50, pady=(10, 0))

head2 = tk.Label(root, text="Time", font=("Arial", 16))
head2.grid(row=0, column=1, sticky="e", padx=100, pady=(10, 0))

# Create and place the listboxes and scrollbar
scrollbar = tk.Scrollbar(root)
list1 = tk.Listbox(root, height=25, width=30, font=("Arial", 10), activestyle='dotbox', yscrollcommand=scrollbar.set)
list2 = tk.Listbox(root, height=25, width=10, font=("Arial", 10), activestyle='dotbox', yscrollcommand=scrollbar.set)
scrollbar.config(command=lambda *args: [list1.yview(*args), list2.yview(*args)])
scrollbar.grid(row=1, column=2, sticky='ns', pady=(0, 10))

list1.grid(row=1, column=0, padx=10, pady=(0, 10))
list2.grid(row=1, column=1, pady=(0, 10))

# Example task
list1.insert(1, "Example Task")
list2.insert(1, "12:00")

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

# Current time label
times = tk.Label(root, text="")
times.grid(row=4, column=0, pady=(10, 10))

# Status label
sta = tk.StringVar()
status = tk.Label(root, textvariable=sta)
status.grid(row=4, column=1, pady=(10, 10))

update_time()  # Start the clock
root.mainloop()
