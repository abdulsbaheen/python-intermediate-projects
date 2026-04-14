# Title: To-Do List App
# Description: A simple to-do list application built with Python's Tkinter library.
# It allows users to add, view, and delete tasks, with the ability to save tasks to a file for persistence.
import tkinter as tk
import os
# File path for storing tasks
path_file = "example.txt"

# create a Window
root = tk.Tk()
root.title("To-Do App")
root.geometry("420x550")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="📝 My To-Do List",
                 font=("Helvetica", 20, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=15)

# Input Frame
input_frame = tk.Frame(root, bg="#1e1e2f")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame,
                 width=25,
                 font=("Helvetica", 12),
                 bg="#2e2e3e",
                 fg="white",
                 insertbackground="white",
                 relief="flat")
entry.grid(row=0, column=0, padx=5, ipady=6)

# function to add task to the listbox and save to file
def add_task():
    task = entry.get()
    
    if task != "":
        count = listbox.size() + 1   # get next number
        formatted_task = f"{count}. {task}"
        
        listbox.insert(tk.END, formatted_task)
        
        with open(path_file, "a") as f:
            f.write(task + "\n")
        entry.delete(0, tk.END)

# Save all tasks to file after deletion or clearing
def save_all_tasks():
    with open(path_file, "w") as f:
        for i in range(listbox.size()):
            task = listbox.get(i)

            # remove numbering (1. Task → Task)
            task = task.split(". ", 1)[1]

            f.write(task + "\n")       

# Add button
add_btn = tk.Button(input_frame,
                    text="Add",
                    bg="#4CAF50",
                    fg="white",
                    font=("Helvetica", 10, "bold"),
                    relief="flat",
                    padx=10,
                    command=add_task)
add_btn.grid(row=0, column=1, padx=5)

# Listbox Frame
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Listbox
listbox = tk.Listbox(list_frame,
                     width=35,
                     height=15,
                     font=("Helvetica", 12),
                     bg="#2e2e3e",
                     fg="white",
                     selectbackground="#4e9cff",
                     relief="flat",
                     yscrollcommand=scrollbar.set)

listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

# Button Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=15)
# refresh numbers after deletion
# This function is used to refresh the numbering of tasks in the listbox after a task is deleted. 
# It retrieves all tasks from the listbox, removes the numbering, and then re-inserts them with updated numbers.
def refresh_numbers():
    tasks = []
    for i in range(listbox.size()):
        task = listbox.get(i)
        task = task.split(". ", 1)[1]
        tasks.append(task)

    listbox.delete(0, tk.END)

    for i, task in enumerate(tasks, start=1):
      listbox.insert(tk.END, f"{i}. {task}")

# delete task function
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
        refresh_numbers()
        save_all_tasks()  # save changes to file after deletion
        
# delete button
delete_btn = tk.Button(btn_frame,
                       text="Delete",
                       bg="#f44336",
                       fg="white",
                       font=("Helvetica", 10, "bold"),
                       relief="flat",
                       padx=15,
                       command=delete_task)
delete_btn.grid(row=0, column=0, padx=10)
# clear button
clear_btn = tk.Button(btn_frame,
                      text="Clear All",
                      bg="#ff9800",
                      fg="white",
                      font=("Helvetica", 10, "bold"),
                      relief="flat",
                      padx=10,
                      command=lambda: [listbox.delete(0, tk.END), save_all_tasks()])
clear_btn.grid(row=0, column=1, padx=10)
# load tasks from file to listbox

def load_tasks():
    if os.path.exists(path_file):
        with open(path_file, "r") as f:
            tasks = f.readlines()

        for i, task in enumerate(tasks, start=1):
            listbox.insert(tk.END, f"{i}. {task.strip()}")
# calling for the function to load tasks when the application starts            
load_tasks()
# about developer
footer = tk.Label(root,
                  text="🚀 Developed by Abdul-Rehman Azam",
                  font=("Helvetica", 10, "italic"),
                  bg="#1e1e2f",
                  fg="#888")

footer.pack(side=tk.BOTTOM, pady=10)
# Run
root.mainloop()
