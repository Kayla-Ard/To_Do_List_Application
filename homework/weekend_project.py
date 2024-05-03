# Mini-project | To-Do list Application

# 1.) User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:

# Welcome to the To-Do List App!
#     Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit

# 2.) To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task with a title
# Viewing the list of tasks with from Incomplete and Complete tasks.
# Marking a task as complete.
# Deleting a task.
# Quitting the application.

# 3.) User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.

# 4.) Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.

# 5.) Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and docstrings for clarity.

# 6.) Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.

# 7.) Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.

# 8.) Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

# 9.) GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include a link to your GitHub repository in your project documentation.


# welcome = """Welcome to the To-Do List App!
# Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete (Moving from incomplete to complete)
#     4. Delete a task
#     5. Quit"""
# print(welcome)

completed_tasks = []
incomplete_tasks = []

def add_task(incomplete):
    task = input("What task would you like to add to your to-do list?: ")
    if task not in incomplete:
        incomplete.append(task)
        print(f"Your current incomplete to-do list now includes these tasks: {incomplete_tasks}")
    else:
        print("That task is already on your to-do list!")
        
def view_task(incomplete, complete):
    task = input('Which tasks would you like to view? Enter "1" for incomplete or enter "2" for complete: ')
    if task == "1":
        for task in incomplete:
            print(task)
    elif task == "2":
        for task in complete:
            print(task)
    else:
        print('Please enter a valid response of "1" or "2"!')
        
def mark_task(incomplete, complete):
    task = input('To mark a task on your incomplete to-do list as "complete" enter "1" or enter "2" to exit: ')
    if task == "1":
        print(f"Your current incomplete to-do list currently includes these tasks: {incomplete_tasks}")
        completed_task = input("What task would you like to mark as complete?: ")
        incomplete.remove(completed_task)
        complete.append(completed_task)
        print(f"Your updated incomplete to-do list now includes these tasks: {incomplete_tasks}")
    elif task == "2":
        print("No tasks will be altered")
    else:
        print('Please enter a valid response of "1" or "2"!')

def delete_task(incomplete, complete):
    task = input('To delete a task from incomplete to-do list enter "1", to delete a task from complete to-do list enter "2"!: ')
    if task == "1":
        print(f"Your current incomplete to-do list includes these tasks: {incomplete_tasks}")
        incomplete_task_to_delete = input("What task would you like to delete?: ")
        incomplete.remove(incomplete_task_to_delete)
        print(f"Your updated incomplete to-do list now includes these tasks: {incomplete_tasks}")
    elif task == "2":
        print(f"Your current complete to-do list includes these tasks: {completed_tasks}")
        complete_task_to_delete = input("What task would you like to delete?: ")
        complete.remove(complete_task_to_delete)
    else:
        print('Invalid response. Please enter a valid response of "1" or "2"!')

def app_run(incomplete, complete):
    while True:
        response = input("""Welcome to the To-Do List App! The menu is listed below. Please enter a number for your desired selection.

        Menu:
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit
            """)

        if response == "1":
            add_task(incomplete)
            print("Task added successfully!")
            
        elif response == "2":
            view_task(incomplete, complete)
            print("Displaying your tasks!")
            
        elif response == "3":
            mark_task(incomplete, complete)
            
        elif response == "4":
            delete_task(incomplete, complete)
            print("Task successfully deleted!")
            
        elif response == "5":
            print("Good-bye!")
            break
        
        else:
            print('Please enter a valid response. Must be "1", "2", "3", "4", or "5"!')
        
app_run(incomplete_tasks, completed_tasks)
