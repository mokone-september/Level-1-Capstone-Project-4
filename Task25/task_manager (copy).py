# https://docs.python.org/3/library/datetime.html, Topic: Examples of Usage: date under the subheading,  "More examples of working with date"
# import of datetime module
 
from datetime import datetime

# Although this code is not a replica or verbatim copy of the code originally authored/coded by Nada Bonaso
# The code in mention can be found on https://github.com/nadabonaso/company_task_manager_v2
# I will be adding her as a resource used to avoid any form of plagiarism because I did originally see and understood the task better after seeing her code.   


# variable from the datetime module function for the current local date

current_date = datetime.today().strftime('%d-%m-%Y')

# variable for completed, uncompleted and overdue tasks counter, intialized at 0 

tasks_completed = 0
tasks_uncompleted = 0
tasks_overdue = 0

#  return to the main menu, intialized to False

return_to_menu = False

def  view_mine():
        with open("tasks.txt", "r") as task_manager_file:

            # code section for viewing user logged specific tasks
            
            for line in task_manager_file.readlines():
                data_split = line.split(", ")
                if data_split[0] == end_user: #Ensuring that data retrieved are for the specific user, logged in

                # Through the use of split() at specific indices[x] of our list we specify, the data to be retrived and print in a user friendly manner
                
                    existing_username = data_split[0].strip()
                    add_title_of_task = data_split[1].strip()
                    add_description = data_split[2].strip()
                    add_current_date = data_split[3].strip()
                    add_due_date = data_split[4].strip()
                    add_completion_status = data_split[5].strip()
                    unique_reference_number = id(data_split[5])
            
                    print('\nTASK MANAGER VIEW MINE')
                    print(f'                                                                     {unique_reference_number}')
                    print('____________________________________________________')
                    print(f'Task is assigned to:         {existing_username}')
                    print(f'Title of task:                       {add_title_of_task}')
                    print(f'Description of task:        {add_description}')
                    print(f'Current date:                     {add_current_date}')
                    print(f'Due date:                             {add_due_date}')
                    print(f'Completion Status:         {add_completion_status}')
                

            
# Function to register a new user

def reg_user(new_username, new_user_password, confirm_password):
    print('\nTASK MANAGER NEW-REG')
    print('____________________________________________________')
    while True:
        reg_user_out = open("user.txt", "r")
        reg_user_out_read = reg_user_out.readlines()

        # Checks if the username exists in the user text file
        
        for line in reg_user_out_read:
            if new_username in line:
                print("\nUsername exists, try again.\n")
                new_username = input('Enter new username: ')
                new_user_password = input(f'Enter a new password for {new_username.upper()}: ')
                confirm_password = input(f'Please confirm password for {new_username.upper()}: ')

        # Checks if the passwords do not match
        
        if new_user_password != confirm_password:
            print("\nPasswords do not match, please try again.\n")
            new_username = input('Enter new username: ')
            new_user_password = input(f'Enter a new password for {new_username.upper()}: ')
            confirm_password = input(f'Please confirm password for {new_username.upper()}: ')

        # Checks if the passwords match
        
        elif new_user_password == confirm_password:
        
            # Calls the function to write new user and password to file
            
            write_user_to_file(new_username, confirm_password)
            print("\nYou have successfully added a new user.\n")
            break

        user_file.close()

def add_task():
    print('\nTASK MANAGER TASK ADD')
    print('____________________________________________________')
    existing_username = input('Username of the person the task is assigned to:  ')
    add_title_of_task = input('Enter task title:  ')
    add_description = input('Please provide task description: ')
    add_current_date = current_date
    add_due_date = input('Enter the due date for the task (DD-MM-YYYY): ')
    add_completion_status = "NO"

    print('\nTASK MANAGER TASK ADDED')
    print('____________________________________________________')
    print(f'Task is assigned to:       {existing_username}')
    print(f'Title of task:                     {add_title_of_task}')
    print(f'Description of task:      {add_description}')
    print(f'Current date:                   {add_current_date}')
    print(f'Due date:                           {add_due_date}')
    print(f'Completion Status:       {add_completion_status}')

    with open('tasks.txt', 'a+') as data_user_out:
        task_data_details = f'{existing_username}, {add_title_of_task}, {add_description}, {add_due_date}, {add_completion_status}'
        data_user_out.write(task_data_details + '\n')



def view_all():

    with open("tasks.txt", "r") as task_manager_file:
        for line in task_manager_file.readlines():
            data_split = line.split(", ")
            
            # Through the use of split() at specific indices[x] of our list we specify, the data to be retrived and print in a user friendly manner 

            existing_username = data_split[0].strip()
            add_title_of_task = data_split[1].strip()
            add_description = data_split[2].strip()
            add_current_date = data_split[3].strip()
            add_due_date = data_split[4].strip()
            add_completion_status = data_split[5].strip()

            print('\nTASK MANAGER VIEW ALL')
            print('____________________________________________________')
            print(f'Task is assigned to:         {existing_username}')
            print(f'Title of task:                       {add_title_of_task}')
            print(f'Description of task:        {add_description}')
            print(f'Current date:                     {add_current_date}')
            print(f'Due date:                             {add_due_date}')
            print(f'Completion Status:         {add_completion_status}')


    

# code section for end_user login validation, by means of a while loop.

accepted_login = False #Initializing accepted login as false until correct validation is passed

while not accepted_login:
    print('\nTASK MANAGER LOGIN')
    print('____________________________________________________')
    end_user = input("Please enter your username: ")
    end_user = end_user.strip()
    password = input("Please enter your password: ")
    password = password.strip()
    credential_admin = "admin, adm1n"

    # code section for the for loop that (1) opens and reads the file, user.txt in read mode
    #(2) strip() which removes any spaces in our file line and split() which splits a string into a list
    #(3) and finally through the variables access_credential_username and access_credential_password we access our list 
    #through indices to identify the username: admin and password: adm1n 
    
    for line in open("user.txt", "r").readlines():
        access_credential = line.strip()
        access_credential = access_credential.split(", ")

        access_credential_username = access_credential[0]
        access_credential_password = access_credential[1]
        

        if end_user == access_credential_username and password == access_credential_password:
        
            accepted_login = True #correct user validation has passed and we change are initial false boolean 
            
            
            end_user_logged = access_credential_username + ", " + access_credential_password

    if not accepted_login:
        print("\nPlease try again, that was an invalid entry.\n")

# variable for capturing user input in and returning all values in lowercase
 
end_user_choice = "".lower     

    # A distinguishing feature of this code section is that the end_user is
    # provided two different menu options based on their verified credential status
    # End_user is either an administrator with authorization to register new users or a user only account
    
while end_user_choice != "e":
    if end_user_logged == credential_admin:
        
        print('\nTASK MANAGER ADMIN-MENU')
        print('____________________________________________________')
        end_user_choice =input('''\n
Please select on the following options:
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit\n\nSelect your option: ''')

    else:
            if end_user_logged != credential_admin:
                
                print('\nTASK MANAGER USER-MENU')
                print('____________________________________________________')
                end_user_choice =input('''\n
Please select on the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit\n\nSelect your option: ''')
                
    
    # code section for registering a new user, only available to the administrator
    
    if end_user_choice == 'r' and end_user_logged == credential_admin:
        print('\nTASK MANAGER NEW-REG')
        print('____________________________________________________')
        new_username = input('Enter new username: ')
        new_user_password = input(f'Enter a new password for {new_username.upper()}: ')
        confirm_password = input(f'Please confirm password for {new_username.upper()}: ')
        reg_user(new_username, new_user_password, confirm_password)

    # code section for adding new tasks
     
    elif end_user_choice == 'a':
        add_task()


    elif end_user_choice == 'va':
        view_all()

    elif end_user_choice == 'ds' and end_user_logged == credential_admin:
    
    # code section for opening tasks.txt and user.txt in reading mode to calculate the total amount of data captured in each file to output to user, admin only
       
        with open("tasks.txt", "r") as task_manager_file:
            number_of_tasks = 0
            content_from_file = task_manager_file.read()
            task_list = content_from_file.split("\n")
            for i in task_list:
                if i:
                    number_of_tasks += 1

        with open("user.txt", "r") as user_manager_file:
            number_of_users = 0
            content_from_file = user_manager_file.read()
            user_list = content_from_file.split("\n")
            for i in user_list:
                if i:
                    number_of_users += 1
        
        print('\nTASK MANAGER STATS')
        print('____________________________________________________')
        print(f'\nTotal number of users:      {number_of_users}') 
        print(f'Total number of tasks:      {number_of_tasks}\n')

        print('\nTASK MANAGER STATS')
        print('____________________________________________________')
        with open("task_overview.txt", "r") as task_manager_file:
            task_manager_contents = task_manager_file.read()
            for line in task_manager_contents:
                print (task_manager_contents)

        
        
    elif end_user_choice == 'gr' and end_user_logged == credential_admin:
        print('\nTASK MANAGER GEN-REPORT')
        print('____________________________________________________')
        

        with open("tasks.txt", "r") as task_manager_file:
            for line in task_manager_file.readlines():
                data_split = line.split(", ")

                existing_username = data_split[0].strip()
                add_title_of_task = data_split[1].strip()
                add_description = data_split[2].strip()
                add_current_date = data_split[3].strip()
                add_due_date = data_split[4].strip()
                add_completion_status = data_split[5].strip()

                task_data_details = f'{existing_username}, {add_title_of_task}, {add_description}, {add_due_date}, {add_completion_status}'

                with open('task_overview.txt', 'w') as task_overview:
                    for item in task_data_details:
                        task = task_data_details
                        if 'Yes' == add_completion_status:
                            tasks_completed += 1
                        elif 'No' == add_completion_status:
                            tasks_uncompleted += 1
            
                        # Comparing the dates to check if the task is overdue.
                        #https://stackoverflow.com/questions/60294481/checking-if-date-is-overdue-from-text-file, is where this example code is sourced
                        
                        if """datetime.strptime(add_due_date, '%d-%m-%Y') < current_date and""" 'No' == add_completion_status:
                            tasks_overdue += 1

                        # Calculations for percentage_incomplete_tasks, percentage_overdue_tasks and Percentage_completed
                        
                        percentage_incomplete_tasks = (tasks_uncompleted * 100)/(len(task_data_details))
                        percentage_overdue_tasks = (tasks_overdue * 100)/(len(task_data_details))
                        Percentage_completed =  (tasks_completed * 100)/(len(task_data_details))

                    # writing mode, for task_overview.txt
                    
                    task_overview.write(f"Total number of tasks generated using task_manager.py : {len(task_data_details)}\n")
                    task_overview.write(f"Total number of completed tasks: {tasks_completed}\n")
                    task_overview.write(f"Total number of uncompleted tasks: {tasks_uncompleted}\n")
                    task_overview.write(f"Total number of tasks that haven’t been completed and that are overdue: {tasks_overdue}\n")
                    task_overview.write(f"Percentage of tasks that are incomplete: {percentage_incomplete_tasks}%\n")
                    task_overview.write(f"Percentage of tasks that are overdue tasks: {percentage_overdue_tasks}%\n")
    
        print("task_overview.txt file is ready for viewing.")
       
        # oopening user.txt in read mode
        
        with open("user.txt", "r") as task_manager_file:
                for line in task_manager_file.readlines():
                    data_split = line.split(", ")
                    if data_split[0] == end_user:

                        existing_username = data_split[0].strip()
                        confirm_password = data_split[1].strip()

                        user_data_details = f'{existing_username}, {add_title_of_task}'

                        # writing mode, for user_overview.txt
                        
                        with open('user_overview.txt', 'w') as user_overview:

                            user_overview.write(f"Total number of users registered with task_manager.py: {len(user_data_details)}\n")
                            user_overview.write(f"Total number number of tasks that have been generated and tracked using the task_manager.py: {len(task_data_details)}\n")
                            user_overview.write(f"Total number of tasks assigned to you: {len(task_data_details)}\n")
                            user_overview.write(f"Percentage of total number of tasks assigned to user: {Percentage_completed}%\n")
                            user_overview.write(f"Percentage of the tasks assigned to that user have been completed: {tasks_uncompleted}%\n")
                            user_overview.write(f"Percentage of the tasks assigned to that user must still be completed: {percentage_incomplete_tasks}%\n")
                            user_overview.write(f"Percentage of tasks assigned to that user have not yet been completed and are overdue: {percentage_overdue_tasks}%\n")
                        
                print("user_overview.txt file is ready for viewing.")
                        
        
    elif end_user_choice == 'vm':
        view_mine()
        
        # Back to menu option
                
        while return_to_menu == False:
            menu_option = input("\nReturn to main menu type (-1) to EDIT tasks and ENTER: ")
            if menu_option == "-1":
                return_to_menu = True
            if menu_option != "-1":
                print("\nInvalid input, please try again.\n")
                        
        continue
            
    elif end_user_choice == 'e':
    
        #code section for exiting and printing farwell message to user
    	 
        print('\n\t\t\t\tTASK MANAGER')
        print('\t\t____________________________________________________')
        print('\n\t\t\t     THANK YOU AND GOODBYE')
        

        
        exit(0)
 
        

    else:
        print('invalid entry') 

