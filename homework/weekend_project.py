
# 4.) Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.

# 6.) Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.

# 7.) Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.

# 8.) Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.




# Mini-project | To-Do list Application

completed_tasks = []                                                                                # Create an empty lists to append completed tasks to
incomplete_tasks = []                                                                               # Create an empty lists to append incomplete tasks to

def add_task(incomplete):                                                                           # defined a function for adding tasks that accepts user input
    task = input("What task would you like to add to your to-do list? ")                            # taking input from the user to see what task they would like to add to incomplete_tasks list
    if task not in incomplete:                                                                      # making sure the task user enters is not already on the incomplete_tasks list
        incomplete.append(task)                                                                     # adding the task the user entered to the incomplete_tasks list
        print(f"Your current incomplete to-do list now includes these tasks: {incomplete_tasks}")   # incomplete_tasks lists is printed for the user so they can see all tasks in the list
    else:
        print("That task is already on your to-do list!")                                           # prints message to user letting them know the task they tried to add was already on the incomplete_tasks list 
        
def view_task(incomplete, complete):                                                                            # defined a function for viewing tasks that accepts user input
    task = input('Which tasks would you like to view? Enter "1" for incomplete or enter "2" for complete: ')    # taking input from the user to see what type of tasks they would like to view
    if task == "1":                                                                                             # created an if statement to see if user input is equal to 1
        for task in incomplete:                                                                                 # created a for loop to loop through incomplete_tasks list
            print(task)                                                                                         # prints out each task included in incomplete_tasks list for the user
    elif task == "2":                                                                                           # created an elif statement to see if user input is equal to 2
        for task in complete:                                                                                   # created a for loop to loop through completed_tasks list
            print(task)                                                                                         # prints out each task included in completed_tasks list for the user
    else:
        print('Please enter a valid response of "1" or "2"!')                                                   # prints message to user letting them know they need to enter a valid response
        
def mark_task(incomplete, complete):                                                                                # defined a function for marking tasks complete that accepts user input
    task = input('To mark a task on your incomplete to-do list as "complete" enter "1" or enter "2" to exit: ')     # taking input from the user to ensure they want to mark a task from incomplete_tasks list as completed 
    if task == "1":                                                                                                 # create an if statement to see if user input is equal to 1
        print(f"Your current incomplete to-do list currently includes these tasks: {incomplete_tasks}")             # prints out the tasks currently in incomplete_tasks for user
        completed_task = input("What task would you like to mark as complete?: ")                                   # taking input from the user to see what task they want to mark as complete in a new variable 
        incomplete.remove(completed_task)                                                                           # removing the task that the user specified from the incomplete_tasks list
        complete.append(completed_task)                                                                             # adding the task we removed from the incomplete_tasks list to the completed_tasks list 
        print(f"Your updated incomplete to-do list now includes these tasks: {incomplete_tasks}")                   # prints out an updated incomplete_tasks list for the user so they can see the changes 
    elif task == "2":                                                                                               # created an elif statement to see if the user input is equal to 2
        print("No tasks will be altered")                                                                           # prints out a message for user letting them know nothing was changed 
    else:
        print('Please enter a valid response of "1" or "2"!')                                                       # prints out a message to user letting them know they need to enter a valid response 

def delete_task(incomplete, complete):                                                                                              # defined a function for deleting tasks that accepts user input
    task = input('To delete a task from incomplete to-do list enter "1", to delete a task from complete to-do list enter "2"!: ')   # taking input from the user to see what list they would like to delete a task from 
    if task == "1":                                                                                                                 # create an if statement to see if user input is equal to 1
        print(f"Your current incomplete to-do list includes these tasks: {incomplete_tasks}")                                       # prints out the tasks currently in incomplete_tasks list for user
        incomplete_task_to_delete = input("What task would you like to delete?: ")                                                  # taking input from the user to see what task they want to delete in a new variable 
        incomplete.remove(incomplete_task_to_delete)                                                                                # removing the task that the user specified from the incomplete_tasks list
        print(f"Your updated incomplete to-do list now includes these tasks: {incomplete_tasks}")                                   # prints out an updated incomplete_tasks list for the user so they can see the changes 
    elif task == "2":                                                                                                               # created an elif statement to see if the user input is equal to 2
        print(f"Your current complete to-do list includes these tasks: {completed_tasks}")                                          # prints out the tasks currently in completed_tasks list for user
        complete_task_to_delete = input("What task would you like to delete?: ")                                                    # taking input from the user to see what task they want to delete in a new variable 
        complete.remove(complete_task_to_delete)                                                                                    # removing the task that the user specified from the completed_tasks list
    else:
        print('Invalid response. Please enter a valid response of "1" or "2"!')                                                     # prints out a message to user letting them know they need to enter a valid response

# Defining a function with a while loop that displays a welcoming message and a menu with options for the user to choose from

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
