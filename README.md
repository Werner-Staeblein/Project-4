 
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
The goal of the Dividend Shares Blog App is to provide comprehensive, reliable, and insightful information about companies that have a strong track record of paying dividends. The blog content aims to serve as a resource for investors looking to build or manage a dividend-focused investment portfolio. By delivering short summaries of analysis on dividend-paying companies, the blog content helps users with ideas of potential investments to be investigated further.

## Targeted Audience
The targeted personas of the blog app are broad and include personas such as long-term investors familiar with the dividend shares investment style, personas seeking information about stocks with higher dividend growth prospects than already owned, or personal investors new to the investment style of dividend shares.

All personas have some or all of the following interests:
-	Stable income streams through dividend-paying stocks
-	Accumulation of wealth for retirement
-	Information about long-term track record of dividend-paying stocks with dividend histories and analyses
-	Reinvestment of dividend income to achieve compounded returns on investments
-	Identification of stocks with a track record of increasing dividend payments over prolonged periods
-	Information about the basics of dividend investing and building financial literacy

The dividend blog app caters to the information needs of users as follows:
-	Educational content on dividend investing fundamentals
-	Explains beginner-friendly dividend-paying stocks with low risk
-	Offers the opportunity to share thoughts on specific dividend investment ideas via a comment function and get engaged in a discussion with other users

## Wireframes
	
## Database Schema

The database model (Entity Relationship Diagram | ERD) describes the connection among the different models used in the site
	
## Color Scheme

The dividend blog app uses a color scheme to convey professionalism and trustworthiness. Both are key characteristics of finance-related content.
The blue color is associated with trust, stability, and professionalism and is widely used in the financial sector. The credibility of the content is supported by the use of this key color for headlines, titles, and important text elements.Gray is used as a contrast color. The gray color is neutral and symbolizes maturity, calmness, and sophistication. The gray colors are used for standard text to ensure readability and to complement and contrast the headline and title color. Gray is also used for background elements to support the main content.

![Color Scheme](docs/readme/coolors_color_palette.png)


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
    
1. Log in to Heroku under.
2. In the Heroku dashboard, click the button **"Create new app"**.
3. Assign a unique name to your app. Names of apps existing already are not considered unique.
4. Select the region (for this project, Europe was selected).
5. Click **"Create app"**.
6. The deployment method must be selected. For this project, GitHub was used as the deployment method.
7. Search for the name of the GitHub repository to be deployed.
8. Click on **"Connect"** to connect Heroku with the GitHub repository.
9. Under the options of either manual or automatic deployment, the **"main branch"** must be selected.
10. In the tab named **"Settings"**, select the **Config Vars**. Config Vars is Heroku's name for environment variables.
    - Inside the Config Vars, set the following:
      - **SECRET_KEY** and its value from the `env.py` file that was ignored with `.gitignore`.
      - **DATABASE_URL** and its value (the database URL) from the `env.py` file that was ignored with `.gitignore`.
      - **DISABLE_COLLECTSTATIC** with a value of `1` initially. For final deployment and once static files are collected, this must be removed.
11. Final Step:
    - The last step is to click **"Deploy Branch"** in the section named **"Manual deploy"**.
    - This will start the build process in Heroku. Once the build process is completed successfully, a link is shown to view the deployed app.
