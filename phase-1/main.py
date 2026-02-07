from typing import List, Dict, Optional


class Task:
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed


# In-memory storage for tasks
tasks: List[Task] = []
next_task_id = 1


def add_task():
    """Add a new task to the list"""
    global next_task_id
    
    title = input("Enter task title (required): ").strip()
    if not title:
        print("Title is required!")
        return
    
    description = input("Enter task description (optional): ").strip()
    
    new_task = Task(task_id=next_task_id, title=title, description=description, completed=False)
    tasks.append(new_task)
    print(f"Task '{title}' added successfully with ID {next_task_id}")
    next_task_id += 1


def view_tasks():
    """Display all tasks with their ID, title, description, and status"""
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nCurrent Tasks:")
    print("-" * 60)
    print(f"{'ID':<4} {'Status':<8} {'Title':<20} {'Description'}")
    print("-" * 60)
    
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"{task.id:<4} {status:<8} {task.title:<20} {task.description}")


def update_task():
    """Update task title and/or description by ID"""
    if not tasks:
        print("No tasks found to update.")
        return
    
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    # Find the task with the given ID
    task = None
    for t in tasks:
        if t.id == task_id:
            task = t
            break
    
    if task is None:
        print(f"No task found with ID {task_id}.")
        return
    
    # Get new values (keep existing if empty input)
    new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
    new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
    
    # Update the task if new values were provided
    if new_title:
        task.title = new_title
    if new_description:
        task.description = new_description
    
    print(f"Task ID {task_id} updated successfully.")


def delete_task():
    """Delete a task by ID"""
    if not tasks:
        print("No tasks found to delete.")
        return
    
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    # Find and remove the task with the given ID
    for i, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(i)
            print(f"Task '{deleted_task.title}' (ID: {task_id}) deleted successfully.")
            return
    
    print(f"No task found with ID {task_id}.")


def mark_task_complete_incomplete():
    """Toggle task completion status by ID"""
    if not tasks:
        print("No tasks found to mark.")
        return
    
    try:
        task_id = int(input("Enter task ID to mark complete/incomplete: "))
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    # Find the task with the given ID
    task = None
    for t in tasks:
        if t.id == task_id:
            task = t
            break
    
    if task is None:
        print(f"No task found with ID {task_id}.")
        return
    
    # Toggle the completion status
    task.completed = not task.completed
    status = "completed" if task.completed else "incomplete"
    print(f"Task '{task.title}' (ID: {task_id}) marked as {status}.")


def main():
    """Main application loop"""
    print("Welcome to the Todo Console Application!")
    
    while True:
        print("\nPlease select an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                update_task()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                mark_task_complete_incomplete()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
