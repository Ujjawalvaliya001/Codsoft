import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_list = tk.Listbox(root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(padx=10, pady=10)

        self.show_remaining_button = tk.Button(root, text="Show Remaining Tasks", command=self.show_remaining_tasks)
        self.show_remaining_button.pack(padx=10, pady=10)

        self.show_statistics_button = tk.Button(root, text="Show Statistics", command=self.show_statistics)
        self.show_statistics_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete.")

    def complete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            messagebox.showinfo("Task Complete", f"Task '{task}' is complete.")
            self.task_list.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showerror("Error", "Select a task to complete.")

    def show_remaining_tasks(self):
        messagebox.showinfo("Remaining Tasks", "\n".join(self.tasks))

    def show_statistics(self):
        total_tasks = len(self.tasks)
        messagebox.showinfo("Statistics", f"You have {total_tasks} tasks remaining.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List GUI Application")
    todo_gui = ToDoListGUI(root)
    root.mainloop()
