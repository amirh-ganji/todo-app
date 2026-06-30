# To-Do List App

A simple and efficient task management program that works through the command line (CLI).

## ✨ Features

- ✅ **View Tasks** - Display all tasks with status and priority
- ➕ **Add Tasks** - Create new tasks with title, description, and priority
- ❌ **Delete Tasks** - Remove tasks from the list
- 🔄 **Change Status** - Mark tasks as done or not done
- 💾 **Save and Load** - All tasks are saved in a CSV file
- 📊 **Priority Levels** - Three priority levels: low, medium, high

## 📁 Project Structure

```
todo-app/
├── main.py          # Entry point and CLI menu
├── task.py          # Task class for representing each task
├── todolist.py      # ToDoList class for managing tasks
├── README.md        # This file
└── tasks.csv        # Saved tasks file (created on first run)
```

## 🏗️ Architecture

### `task.py`
The `Task` class that represents each task:
- `title`: Task title
- `description`: Detailed description
- `priority`: Priority level (low, medium, high)
- `is_done`: Completion status

### `todolist.py`
The `ToDoList` class that manages all tasks:
- `add_task()`: Add a new task
- `remove_task()`: Delete a task by number
- `toggle_task_status()`: Change task status
- `show_tasks()`: Display all tasks
- `save_to_csv()`: Save tasks to CSV file
- `load_from_csv()`: Load tasks from CSV file

### `main.py`
Command-line interface (CLI) with interactive menu

## 🚀 How to Run

### Requirements
- Python 3.x

### Setup

```bash
# Clone the repository
git clone https://github.com/amirh-ganji/todo-app.git
cd todo-app

# Run the program
python main.py
```

## 📖 Usage Guide

After running, the following menu will be displayed:

```
--- To-Do List Menu ---
1. Show tasks           # Display all tasks
2. Add a task           # Add a new task
3. Delete Task          # Delete a task
4. Change task status   # Change status (done/not done)
5. Save to file         # Save all tasks
6. Exit                 # Exit the program
```

### Usage Examples

**1. Adding a task:**
```
Your choice: 2
Task title: Buy groceries
Description: Fresh fruits and vegetables from the market
Priority (low, medium, high): high
```

**2. Displaying tasks:**
```
Your choice: 1
0. [✗] Buy groceries (high)
1. [✓] Complete project (medium)
```

**3. Changing status:**
```
Your choice: 4
Task number to change status: 0
```

## 💾 Storage

All tasks are automatically saved to the `tasks.csv` file when menu options 5 or 6 are executed.

**CSV Format:**
```
title,description,priority,is_done
Task Title,Task Description,Priority Level,Done Status
```

## 🔧 Technical Notes

- Uses `csv` module for data storage
- Interactive command-line user interface
- Range checking to prevent index errors
- UTF-8 support for international text

## 📝 License

This project is for educational purposes.
