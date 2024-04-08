# CPDM
Company Planning and Development Manager


RUN APPLICATION IN DEVELOPMENT ENVIRONMENT:

1. Set up PostgreSQL DataBase
	- Go to Docker.com and register an account and login
	- Download Docker Desktop or else for specific OS and login
	- Start PostgreSQL container:
		- terminal --> docker run -p 5432:5432 -e POSTGRES_USER=postgres-user -e POSTGRES_PASSWORD=password -d -v my-postgres-data:/var/lib/postgresql/data --name my_postgresql postgres:latest


2. Open Pycharm Proffesional or else.
	- File / Project from Version Control...
	- URL: https://github.com/entermix123/CPDM.git
	- Directory: D:/repos/test_from_VCS

3. Set Virtual Environment and install packages:

	- add local interpreter
		- click on interpreter/add local interpreter

	- install required packages
		- open terminal
		- go to requirements.txt dir
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


5.Connect database and migrate models:
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
	- On database tab click refresh button
	- Click on the number on the right of the Database name / expand cpdm_db_latest and check Default Schema checkbox
	- termianl --> python manage.py migrate

6. Start Django server and play with the application
	option 1: Click on Run button and go to http://localhost:8000/
	option 2: terminal --> pyrhon manage.py runserver
		       - go to http://localhost:8000/



