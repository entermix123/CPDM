# CPDM
Company Planning and Development Manager

Project Defense 14.04 2024 - SoftUni Course Django Advanced February 2024 - https://softuni.bg/trainings/4392/django-advanced-february-2024

The project is developed with focus on Company planning, process development and management purposes. Server side rendering, CRUD operations for intermidiate database models structure. Basic visualization. Basic REST APIs implemented. 

1. Download the project on your computer
2. Below You will find options to run the App with VsCode or PyCharm Professional.

-------------------------------------------------------
RUN APPLICATION IN DEVELOPMENT ENVIRONMENT WITH VSCODE:
-------------------------------------------------------

1. Register and Install Docker --> https://www.docker.com/

2. Install PostgreSQL:
	terminal --> docker run -p 5432:5432 -e POSTGRES_USER=postgres-user -e POSTGRES_PASSWORD=password -d -v my-postgres-data:/var/lib/postgresql/data --name custom-name postgres:latest

3. Install PgAdmin:
	terminal --> docker run -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=some@email.com -e PGADMIN_DEFAULT_PASSWORD=password -v my-data:/var/lib/pgadmin -d dpage/pgadmin4

4. Open PgAdmin: Browser --> http://localhost:5050/
	Follow the instruction, connect to PostgreSQL and create DB with name 'cpdm_db_latest' instead of 'postgres'

	Connection instruction:
	When you first log in to pgAdmin, you will not have any connections to the database, and you will need to create one.
	Click on the icon "Add New Server".
	Open the Connection Tab and write down the host name (always "host.docker.internal"), port of the container (in this example is "5432"), the maintenance database is "postgres", your username and password which you chose when running  the PostgreSQL container 	(in this example "postgres-user" and "password"). Click "Save" to save the server:

5. Open The project in VsCode.

6. Navigate to the folder that contains 'manage.py' file:
	terminal --> cd CPDM\CPDM

7. Create virtual environment directory:
	terminal --> python -m venv .venv

8. Activate virtual environment:
	terminal --> .venv/Scripts/activate

9. Install dependancies:
	terminal --> pip install -r requirements.txt

10. Apply migrations:
	terminal --> python manage.py migrate

11. Start hte application:
 	terminal --> python manage.py runserver

12. Open the Application in Browser:
	Browser --> http://127.0.0.1:8000/


---------------------------------------------------------------------
RUN APPLICATION IN DEVELOPMENT ENVIRONMENT WITH PYCHARM PROFESSIONAL:
---------------------------------------------------------------------

1. Set up PostgreSQL DataBase
	- Go to Docker.com, register an account and login
	- Download, install Docker Desktop or else for specific OS and login
	- Start PostgreSQL container:
		- terminal --> docker run -p 5432:5432 -e POSTGRES_USER=postgres-user -e POSTGRES_PASSWORD=password -d -v my-postgres-data:/var/lib/postgresql/data --name my_postgresql postgres:latest 

2. Open PyCharm Proffesional or else.
	- File / Project from Version Control...
	- URL: https://github.com/entermix123/CPDM.git
	- Directory: D:/repos/test_from_VCS

3. Set Virtual Environment and install packages:
	- add local interpreter
		- click on interpreter/add local interpreter
	- install required packages
		- open terminal
		- go to the directory the contains requirements.txt
		- termianl --> pip install -r requirements.txt

4. Set Django Support Configuration and Django Server Configuration
	- go to settings/Languages and Frameworks/Django
		- Check Enable Django Support Check Box
		- Set Django project root: D:\repos\test_from_VCS\CPDM\CPDM
		- set Settings: settings.py
		- set Manage script: D:\repos\test_from_VCS\CPDM\manage.py
		- set Folder pattern to track files: migrations
		- click Apply and OK
	- on right side of Run/Debug buttons click on drop down menu and choose Edit Configurations...
		- Click on '+' on top left of the window
		- Choose Django Server
		- Set Name field: start_django_app
		- Set Run to the correct Project Interpreter
		- Set host field: localhost
		- Set Post field: 8000
		- Set Environment Variables: PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=CPDM.settings
		- click Apply and OK

5. Connect database, migrate models and visualize tables
	- Click on database button on right on the PyCharm window
		- Click on '+' / PostgreSQL
		- Set Name: project_db
		- Set User: postgres-user
		- Set Paswword: password
		- Install drivers if needed
		- Click Test Connection / OK
	- Right click on project_db / new / Database
		- Set Name: cpdm_db_latest
		- Click OK
		- termianl --> python manage.py migrate
	- On database tab click refresh button
		- Click on the number on the right of the Database name / expand cpdm_db_latest and check Default Schema checkbox

6. Start Django server and play with the application
	- option 1: Click on Run button
 		-  go to http://localhost:8000/
	- option 2: terminal --> pyrhon manage.py runserver
		- go to http://localhost:8000/



