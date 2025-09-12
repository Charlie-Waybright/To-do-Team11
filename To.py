# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
Done = []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Step 4: Delete a task
def delete_task(index):
    tasks.pop(index)
    print(f"Deleted: {tasks}")


# Step 5: Mark task complete

def mark_complete():
    tasks.remove(index)
    Done.append(index)
    print(f"Finished: {tasks}")
    print(Done)




# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    delete_task(0)
    view_tasks()
    mark_complete()
    #view_tasks()
    