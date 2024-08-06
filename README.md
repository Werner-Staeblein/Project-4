 
# Table of contents

- [Table of contents](#table-of-contents)
- [Project Planning](#project-planning)
  - [Site Goal](#site-goal)
  - [Targeted Audience](#targeted-audience)
  - [Wireframes](#wireframes)
  - [Database Schema](#database-schema)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
- [Agile Development Process](#agile-development-process)
- [Features](#features)
- [Technologies](#technologies)
  - [Django-based technologies](#django-based-technologies)
- [Bugs and issues](#bugs-and-issues)
- [Testing](#testing)
- [Security Features](#security-features)
- [Content](#content)
- [Deployment](#deployment)
  - [Steps before deployment | Update code for deployment](#steps-before-deployment--update-code-for-deployment)
  - [Deployment on Heroku (step-by-step guide)](#deployment-on-heroku-step-by-step-guide)

# Project Planning
	
This is project milestone 4 for the Code Institute full-stack development program. The project is a full-stack website built using the Django framework.

The live site deployed on Heroku can be found here: **[Final_Project](https://dividend-blog-app-7524309b6f0c.herokuapp.com/)**
[NAME OF THE BLOG] is .....where users can look for. For logged-in users, a like/unlike functionality for a post is possible. Logged-in users likewise can comment on a post.

 
## Site Goal
	
## Targeted Audience
description of persona(s) needed
	
## Wireframes
	
## Database Schema

The database model (Entity Relationship Diagram | ERD) describes the connection among the different models used in the site
	
## Color Scheme

## Typography
 
	
# Agile Development Process

Details on the agile development process can be found here **[AGILE.md](agile.md)**

# Features


# Technologies

This is a full-stack (front-end/back-end) project with the primary use of HTML, CSS, and Python. The backend uses the Python framework Django.

The frontend primarily relies on the CSS framework Bootstrap for the efficient layout of mobile-first responsive design (MFRD).

## Django-based technologies

**[Django](https://www.djangoproject.com/)** Django is an open-source web framework for building robust and dynamic web applications

**[AllAuth](https://docs.allauth.org/en/latest/)** A Django package with views and templates for features such as authentication, registration, or account management

**[Cloudinary](https://cloudinary.com/)** Cloudinary is an image/video management solution for websites to easily upload images to the cloud with the delivery of media files through a fast content delivery network (CDN)

**[CrispyForms](https://pypi.org/project/django-crispy-forms/)** Crispy Forms is a third-party Django app to manage Django forms with Bootstrap styles		

**[Summernote](https://summernote.org/)** Summernote is a JavaScript library that allows to create a WYSIWYG (What You See Is What You Get) editor

**[Gunicorn](https://gunicorn.org/)** Gunicorn is a Python WSGI HTTP Server for UNIX. WSGI stands for Web Server Gateway Interface and is a specification for communication between web servers and Python web applications. Gunicorn is the equivalent of 'manage.py runserver' used in the development but with speed and security optimization

**[psycopg2](https://pypi.org/project/psycopg2/)** Pycopg2 is a PostgreSQL database adapter for the Python programming language

**[Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html)** Whitenoise is a Python package that allows the Heroku app to serve its own static files without relying on an external file hosting service such as a content delivery network (CDN)
															
**[CoideInstitutePostgreSQL](https://dbs.ci-dbs.net/)** PostgreSQL from Code Institute to create a database

**[Browserling](https://www.browserling.com/)** Browserling is a web-based cross-browser testing software that allows users to test the website across desktop and mobile browsers such as Chrome, Firefox, Edge, or Opera without downloading and installing the respective browser

**[CI Python Linter](https://pep8ci.herokuapp.com/)** The Code Institute Python Linter was used to validate Python code	

**[Favicon](https://favicon.io/favicon-generator/)** Favicon generates favicons						

**[GitHub](https://github.com/)** The code files, README files, and assets are stored on GitHub. The code on GitHub was pushed from Git				

**[Git](https://git-scm.com/)** The version control system Git was used to document the development of the application and to push code to the GitHub repository. The specific reasons for the commit are reflected in the respective commit message

**[Heroku](https://www.heroku.com/)** Heroku is a platform as a service (PaaS) to build, run, and operate cloud-based applications. It was used to deploy the website

**[Lucid Chart](https://www.lucidchart.com/pages/)** Lucid Chart is a web-based diagramming tool to create flowcharts, wireframes, and visualisation of concepts							

**[Python](https://www.python.org/)** Python is an interpreted, high-level general-purpose programming language	

**[Techsini](https://techsini.com/multi-mockup/)** Multi Device Website Mockup generator				

**[Visual Studio Code](https://code.visualstudio.com/)** Visual Studio Code (VS-Code) was used as an integrated development environment (IDE) for the entire project. The GitHub repository was cloned to VS-Code for this purpose			


# Bugs and issues
After the initial set-up of the Django project, I wanted to test the deployment in Heroku using the django project name 'testproject'. It was a fully erroneous assumption that a simple change of the Django project name with a change of the project folder to 'diviblog' will keep my django project running. I learned that hard way that I have to review and adjust the wsgi.py, asgi.py, manage.py and settings.py with the new app name that I assigned to the existing Django project originally named 'testproject'.


# Testing



# Security Features



# Content


# Deployment

The code for this project was written in visual studio code integrated development environment. Github was used for version control. The application is deployed to Heroku from the GitHub repository.	

The deployed app can be found here **[Final_Project](https://dividend-blog-app-7524309b6f0c.herokuapp.com/)**
    
## Steps before deployment | Update code for deployment
    
1. Install production-ready web server for Heroku
Use 'pip3 install gunicorn' in your development environment
Add gunicorn installed to the requirements.txt file with 'pip3 freeze --local > requirements.txt'
Gunicorn is a production equivalent of the manage.py runserver used in development
    
2. Configuration of python modules
With 'pip3 freeze --local > requirements.txt' the packages for deployment have already been installed
    
3. Create a file named Procfile at the root directory of the Django project
Ensure that the file named Procfile sits at same directory-level as requirements.txt
The Procfile ensures that Heroku is configred to be a gunicorn web application
Inside the Procfile add the following code: web: gunicorn PROJECT_NAME.wsgi
Ensure to have a space after the colon | Use the name of your Django project for the placeholder PROJECT_NAME (iny my case diviblog.wsgi)
The command gunicorn MY_PROJECT.wsgi is used by Heroku to start the server (for my project, Heroku is using diviblog.wsgi)
    
4. Ensure that environment variables are stored in env.py file
Unless created already, create a file named env.py at the root directory to store environment variables|sensitive and secret information
To ensure that secret information|sensitive information is not leaking, the env.py file must be included in .gitignore
Include the environment variables listed below in the Heroku deployment
    
5. Adjust the settings.py in your Django project
In the settings.py, the Heroku hostname must be appended to the ALLOWED_HOST list
Add Heroku to the ALLOWED_HOST list by adding '.herokuapp.com' to ALLOWED_HOSTS in settings.py
Remember to add a dot before herokuapp.com
Once name of Heroku app is known, the settings.py can be adjusted as follows:
    
6. Set the DEBUG to False
Before committing and pushing of changes to GitHub it is of utmost importance to adjust settings.py
Inside settings.py of the Django project, set DEBUG = False, i.e. replace DEBUG = True with DEBUG = False
    
## Deployment on Heroku (step-by-step guide)
    
1	Log in to Heroku under
2	In the Heroku dashboard click the button "Create new app"
3	Assign a unique name to your app. Names of apps existing already are not considered unique
4	Select the region (for this project, Europe was selected)
5	Click "Create app"
6	The deployment method must be selected. For this project, github was used as the deployment method
7	Search for the name of the github repository to be deployed
8	Click on "connect" to connect Heroku with the GitHub repository
9	Under the options of either manual or automatic deployment the "main branch" must be selected
10	In the tab named settings select the config vars
    Config Vars is Heroku's name for environment variables
    Inside the ConfigVars set the following
    
    SECRET_KEY and its value from the env.py file that was ignored with .gitignore
    DATABASE_URL and its value (the database URL) from the env.py file and that was ignored with .gitignore
    DISABLE_COLLECTSTATIC with a value of 1 initially. For final deployment and once static files are collected this must be removed
    
11	Final Step
    The last step is to click "Deploy Branch" in the section named Manual deploy
    This will start the build process in Heroku. Once the build process is completed successfully, a link is shown to view the deployed app