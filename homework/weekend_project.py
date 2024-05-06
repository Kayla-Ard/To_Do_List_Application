# Mini-project | To-Do list Application

completed_tasks = []                                                                                # Create an empty lists to append completed tasks to
incomplete_tasks = []                                                                               # Create an empty lists to append incomplete tasks to

def add_task(incomplete):                                                                           # defined a function for adding tasks that accepts user input
    task = input("What task would you like to add to your to-do list? ").lower()                    # taking input from the user to see what task they would like to add to incomplete_tasks list
    if task not in incomplete:                                                                      # making sure the task user enters is not already on the incomplete_tasks list
        incomplete.append(task)                                                                     # adding the task the user entered to the incomplete_tasks list
        print(f"Your incomplete to-do list now includes these tasks: {incomplete_tasks}")           # incomplete_tasks lists is printed for the user so they can see all tasks in the list
    else:                                                                                           # created an else statement to flag that the user's task request is already in the list
        print(f"That task is already on your to-do list!")                                          # prints message to user letting them know the task they tried to add was already on the incomplete_tasks list
        print(f"Your incomplete to-do list currently includes these tasks: {incomplete_tasks}.")              # prints messages to user showing them their current tasks on their list
        
def view_task(incomplete, complete):                                                                                        # defined a function for viewing tasks that accepts user input
    task = input('Which to-do list would you like to view? Enter "1" for incomplete or enter "2" for complete: ').lower()   # taking input from the user to see what type of tasks they would like to view
    if task == "1":                                                                                                         # created an if statement to see if user input is equal to 1
        print("Here are your tasks in your incomplete to-do list: ")
        for task in incomplete:                                                                                             # created a for loop to loop through incomplete_tasks list
            print(task)                                             # prints message to use letting them know the tasks being shown are in their incomplete to-do list                                                                                                    # prints out each task included in incomplete_tasks list for the user
    elif task == "2":                                                                                                       # created an elif statement to see if user input is equal to 2
        print("Here are your tasks in your completed to-do list: ")
        for task in complete:                                                                                               # created a for loop to loop through completed_tasks list
            print(task)                                              # prints message to use letting them know the tasks being shown are in their completed to-do list
    else:                                                                                                                   # created an else statement to flag invalid user input
        print('A valid response of "1" or "2" must be added!')                                                              # prints message to user letting them know they need to enter a valid response
        
def mark_task(incomplete, complete):                                                                                                            # defined a function for marking tasks complete that accepts user input
    task = input('To mark a task on your incomplete to-do list as "complete" enter "1" or enter "2" to return to Menu: ').lower()               # taking input from the user to ensure they want to mark a task from incomplete_tasks list as completed 
    if task == "1":                                                                                                                             # create an if statement to see if user input is equal to 1
        print(f"Your incomplete to-do list currently includes these tasks: {incomplete_tasks}")                                                 # prints out the tasks currently in incomplete_tasks for user
        try:
            completed_task = input("What task would you like to mark as complete?: ").lower()                                                   # taking input from the user to see what task they want to mark as complete in a new variable 
            incomplete.remove(completed_task)                                                                                                   # removing the task that the user specified from the incomplete_tasks list
            complete.append(completed_task)                                                                                                     # adding the task we removed from the incomplete_tasks list to the completed_tasks list 
            print(f"Your updated incomplete to-do list now includes these tasks: {incomplete_tasks}")                                           # prints out message to user showing them their updated incomplete to-do list 
            print(f"Your updated completed to-do list now includes these tasks: {completed_tasks}")                                             # prints out an updated incomplete_tasks list for the user so they can see the changes 
        except ValueError:
            print("Your to-do list does not contain that task!")                                                                                # prints out message to user letting them know their list doesn't contain the task they entered 
            option_to_add = input('Would you like to add it to your completed to-do list? Enter "yes" or "no" please: ').lower()                # giving the user an option to add the task or not
            if option_to_add == "yes":                                                                                                          # if statement checking to see if user entered "yes"
                complete.append(completed_task)                                                                                                 # adding the task to the completed to-do list
                print(f"Ok, your task was added successfully! Your updated completed to-do list now includes these tasks: {completed_tasks}")   # prints out message to the user letting them know their task was added to their to-do list & showing them the current list 
            elif option_to_add == "no":                                                                                                         # elif statement checking to see if user entered "no"
                print("Ok! Nothing on your to-do list was altered!")                                                                            # prints a message to the user letting them know nothing was altered on their to-do list
    elif task == "2":                                                                                                                           # created an elif statement to see if the user input is equal to 2
        print("Ok! Nothing on your to-do list was altered!")                                                                                    # prints out a message for user letting them know nothing was changed 
    else:                                                                                                                                       # created an else statement to flag invalid user input
        print('Please enter a valid response of "1" or "2"!')                                                                                   # prints out a message to user letting them know they need to enter a valid response 

def delete_task(incomplete, complete):                                                                                                      # defined a function for deleting tasks that accepts user input
    task = input('To delete a task from incomplete to-do list enter "1", to delete a task from complete to-do list enter "2": ').lower()    # taking input from the user to see what list they would like to delete a task from 
    if task == "1":                                                                                                                         # create an if statement to see if user input is equal to 1
        print(f"Your current incomplete to-do list includes these tasks: {incomplete_tasks}")                                               # prints out the tasks currently in incomplete_tasks list for user
        try:
            incomplete_task_to_delete = input("What task would you like to delete?: ").lower()                                              # taking input from the user to see what task they want to delete in a new variable 
            incomplete.remove(incomplete_task_to_delete)                                                                                    # removing the task that the user specified from the incomplete_tasks list
            print(f"Item deleted successfully! Your updated incomplete to-do list now includes these tasks: {incomplete_tasks}")            # prints out an updated incomplete_tasks list for the user so they can see the changes 
        except ValueError:
            print("Your incomplete to-do list does not contain that task!")                                                                 # prints message to user letting them know the task they enter is not on their current to-do list
    elif task == "2":                                                                                                                       # created an elif statement to see if the user input is equal to 2
        print(f"Your current complete to-do list includes these tasks: {completed_tasks}")                                                  # prints out the tasks currently in completed_tasks list for user
        complete_task_to_delete = input("What task would you like to delete?: ").lower()                                                    # taking input from the user to see what task they want to delete in a new variable 
        try:
            complete.remove(complete_task_to_delete)                                                                                        # removing the task the user entered from the completed to do list 
            print(f"Item deleted successfully! Your updated completed to-do list now includes these tasks: {completed_tasks}")              # removing the task that the user specified from the completed_tasks list
        except ValueError:
            print("Your completed to-do list does not contain that task!")                                                                  # prints message to user letting them know the task they enter is not on their current to-do list 
    else:                                                                                                                                   # created an else statement to flag invalid user input
        print('Invalid response. Please enter a valid response of "1" or "2"!')                                                             # prints out a message to user letting them know they need to enter a valid response

def app_run(incomplete, complete):                                                             # Defining a function with two parameters that displaying a menu with options for the user to choose from                                                                                                                   
    print("Welcome to the To-Do List App!")                                                    # Displaying a welcome statement to the user
    while True:                                                                                # Created a while loop in order to be able to run through the program multiple times until user instructs to end the program 
        response = input("""Please enter a number from the menu before for your desired selection.  

        Menu:
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit
            """)

        if response == "1":                                                                     # created an elif statement to see if the user input is equal to 1
            add_task(incomplete)                                                                # Calling the function
            
        elif response == "2":                                                                   # created an elif statement to see if the user input is equal to 2
            view_task(incomplete, complete)                                                     # Calling the function
            
        elif response == "3":                                                                   # created an elif statement to see if the user input is equal to 3
            mark_task(incomplete, complete)                                                     # Calling the function
                                                                                                
        elif response == "4":                                                                   # created an elif statement to see if the user input is equal to 4
            delete_task(incomplete, complete)                                                   # Calling the function
            
        elif response == "5":                                                                   # created an elif statement to see if the user input is equal to 5
            print("Thanks for using the to-do list app! Good-bye!")                             # prints out a message to the user saying good-bye since the program is ending 
            break                                                                               # breaking out of the while loop to end the program 
        
        else:                                                                                   # created an else statement to flag invalid user input
            print('Please enter a valid response. Must be "1", "2", "3", "4", or "5"!')         # prints out a message to user letting them know they need to enter a valid response
        
app_run(incomplete_tasks, completed_tasks)                                                      # Calling the function & assigning arguments to the parameters 
