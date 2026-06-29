from task import Task
import csv

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority):
        task = Task(title, description, priority)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def toggle_task_status(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle_status()

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task.is_done else "✗"
            print(f"{i}. [{status}] {task.title} ({task.priority})")

    def save_to_csv(self, filename="tasks.csv"):
        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "description", "priority", "is_done"])
            for task in self.tasks:
                writer.writerow([task.title, task.description, task.priority, task.is_done])

    def load_from_csv(self, filename="tasks.csv"):
        self.tasks = []
        try:
            with open(filename, mode="r", newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["title"]
                    description = row["description"]
                    priority = row["priority"]
                    is_done = row["is_done"] == "True"
                    task = Task(title, description, priority, is_done)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass  # اگر فایل نبود، کاری نکن
