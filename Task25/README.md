# Task Manager 

A python Implementation for a Task Manager 

This is a part of a series of HyperionDev Capstone Projects, I will be creating a Task management program using the python language.
In this Capstone Project, I will be creating a program for a small business that can help it to manage tasks assigned to each member of the team.


# HyperionDev Capstone Projects Instrctions 

For this task, assume that you have been approached by a small business, you will be creating a program that can help the business manage tasks assigned to each member of the team. 


	Create a new Python file in this folder called task_manager.py.
	

	Write the code that will do the following:
	
		1.This program will work with two text files, user.txt and tasks.txt. 
		Open each of the files that accompany this project and take note of the following:
		
			■ tasks.txt: 
			
			tasks.txt stores a list of all the tasks that the team is working on. Open the tasks.txt file that accompanies this project. Note that this text file already contains data about two tasks.
			The data for each task is stored on a separate line in the text file. Each line includes the following data about a task in this order:
				
				● The username of the person to whom the task is assigned.
				● The title of the task. 
				● A description of the task. 
				● The date that the task was assigned to the user. 
				● The due date for the task. 
				● Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet. 
				
				
			■ user.txt
			
			user.txt stores the username and password for each user that has permission to use your program (task_manager.py). Open the user.txt file that accompanies this project. Note that this text
			file already contains one default user that has the username, ‘admin’ and the password, ‘adm1n’. The username and password for each user must be written to this file in the following format:
			
				● First, the username followed by a comma, a space and then the password.
				● One username and corresponding password per line.
		
		
		
		2. Modifying task_manager.py 
			
			■ Create a copy of your previous Capstone project (task_manager.py) and save it in the Dropbox folder for this project. Also, copy and paste the text files (user.txt and tasks.txt) that
			accompanied the previous Capstone project to this folder. Modify this program as follows: 
				
				● reg_user — that is called when the user selects ‘r’ to register a user. 
				● add_task — that is called when a user selects ‘a’ to add a new task. 
				● view_all — that is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’. 
				● view_mine — that is called when users type ‘vm’ to view all the tasks that have been assigned to them. 
				
		
				
			■ Modify the function called reg_user to make sure that you don’t duplicate usernames when you add a new user to user.txt. If a user tries to add a username that already exists in user.txt,
			provide a relevant error message and allow them to try to add a user with a different username. 
			
			■ Add the following functionality when the user selects ‘vm’ to view all the tasks assigned to them:
			
				● reg_user — that is called when the user selects ‘r’ to register a user.
				● Display all tasks in a manner that is easy to read. Make sure that each task is displayed with a corresponding number which can be used to identify the task. 
				● Allow the user to select either a specific task by entering a number or input ‘-1’ to return to the main menu. 
				● If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task. If the user chooses to mark a task as complete, the ‘Yes’/’No’
				value that describes whether the task has been completed or not should be changed to ‘Yes’. When the user chooses to edit a task, the username of the person to whom the task is assigned
				or the due date of the task can be edited. The task can only be edited if it has not yet been completed. 
				
			■ Add an option to generate reports to the main menu of the application. 

			
				
			
		3. When the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt, should be generated. Both these text files should output data in a user-friendly,
		easy to read manner.
		
			■ task_overview.txt should contain:
			 
				▪ The total number of tasks that have been generated and tracked using the task_manager.py. 
				▪ The total number of completed tasks. ▪ The total number of uncompleted tasks. 
				▪ The total number of tasks that haven’t been completed and that are overdue. 
				▪ The percentage of tasks that are incomplete. ▪ The percentage of tasks that are overdue.
				
			■ user_overview.txt should contain:
			
				▪ The total number of users registered with task_manager.py. 
				▪ The total number of tasks that have been generated and tracked using the task_manager.py. 
				▪ For each user also describe: ▪ The total number of tasks assigned to that user. 
				▪ What percentage of the total number of tasks have been assigned to that user? 
				▪ What percentage of the tasks assigned to that user have been completed? 
				▪ What percentage of the tasks assigned to that user must still be completed? 
				▪ What percentage of the tasks assigned to that user have not yet been completed and are overdue?
				
			■ Modify the menu option that allows the admin to display statistics so that the reports generated are read from task_overview.txt and user_overview.txt and displayed on the screen in a
			user-friendly manner.
		
		 
# Task Manager 
 
Built around the needs of a fictitious company, the Task Manager providesa a small team of workers a user friendly, and lightweight (hardware/software requirements) manner to keep track of tasks, responsibilities and dealines associated with their work on a day-to-day basis. 
     
## Features
The features of the task_manager.py is as follows:
* The user should be able to manage tasks assigned to each member of the team either by *registering new users* or *adding tasks* or *adding tasks* or *viewing all tasks* or *viewing user-specific tasks* and a host of other rich features.




