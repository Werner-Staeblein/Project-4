# Table of contents

- [Table of contents](#table-of-contents)
- [Project Planning](#project-planning)
  - [Site Goal](#site-goal)
  - [Targeted Audience](#targeted-audience)
  - [Wireframes](#wireframes)
    - [Wireframe landing | home page](#wireframe-landing--home-page)
    - [Wireframe blog page](#wireframe-blog-page)
    - [Wireframe about page](#wireframe-about-page)
    - [Wireframe contact page](#wireframe-contact-page)
    - [Wireframe registration page](#wireframe-registration-page)
    - [Wireframe login page](#wireframe-login-page)
    - [Wireframe individual blogpost](#wireframe-individual-blogpost)
    - [Wireframe 404 page](#wireframe-404-page)
    - [Wireframe landing | home mobile](#wireframe-landing--home-mobile)
  - [Database Schema](#database-schema)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
- [Agile Development Process](#agile-development-process)
- [Features](#features)
  - [Hompage | Landing Page](#hompage--landing-page)
  - [Navigation | Logo | Favicon](#navigation--logo--favicon)
    - [Logo Details | Favicon](#logo-details--favicon)
    - [Navigation](#navigation)
      - [Navigation Components](#navigation-components)
      - [Design and Functionality](#design-and-functionality)
      - [Navigation Items for User Status](#navigation-items-for-user-status)
  - [Blog Page | Blog App](#blog-page--blog-app)
      - [Blog Page](#blog-page)
      - [User access to blog content | ability to make comments](#user-access-to-blog-content--ability-to-make-comments)
      - [Individual Blogpost](#individual-blogpost)
  - [About Page | About App](#about-page--about-app)
  - [Contact Page | Contact App](#contact-page--contact-app)
  - [Newsletter Signup Page | Newsletter App](#newsletter-signup-page--newsletter-app)
    - [Call-to-Action Button in Footer](#call-to-action-button-in-footer)
  - [Altert and feedback messages](#altert-and-feedback-messages)
  - [Registration Page](#registration-page)
  - [Login Page](#login-page)
  - [Logout | sign-out confirmation page](#logout--sign-out-confirmation-page)
  - [Customized 404 Error Page](#customized-404-error-page)
    - [Key Features of the Customized 404 Page:](#key-features-of-the-customized-404-page)
  - [Possible future features](#possible-future-features)
- [Technologies](#technologies)
  - [Django-based technologies](#django-based-technologies)
- [Bugs and issues](#bugs-and-issues)
- [Testing](#testing)
  - [Automated Testing](#automated-testing)
      - [Lighthouse results Desktop](#lighthouse-results-desktop)
      - [Lighthouse results Mobile](#lighthouse-results-mobile)
  - [Manual Testing](#manual-testing)
    - [Manual Testing Page 1](#manual-testing-page-1)
    - [Manual Testing Page 2](#manual-testing-page-2)
    - [Manual Testing Page 3](#manual-testing-page-3)
    - [Manual Testing Page 4](#manual-testing-page-4)
    - [Manual Testing Page 5](#manual-testing-page-5)
    - [Manual Testing Page 6](#manual-testing-page-6)
    - [Manual Testing Page 7](#manual-testing-page-7)
    - [Manual Testing Page 8](#manual-testing-page-8)
    - [Manual Testing Page 9](#manual-testing-page-9)
- [Security Features](#security-features)
- [Credits](#credits)
  - [Code](#code)
  - [Content Data Sources](#content-data-sources)
- [Deployment](#deployment)
  - [Steps before deployment | Update code for deployment](#steps-before-deployment--update-code-for-deployment)
  - [Deployment on Heroku (step-by-step guide)](#deployment-on-heroku-step-by-step-guide)
  - [Local Development](#local-development)
    - [How to Fork the project](#how-to-fork-the-project)
    - [How to Clone the Project](#how-to-clone-the-project)
- [Acknowledgements](#acknowledgements)

# Project Planning
	
This is project milestone 4 for the Code Institute full-stack development program. The project is a full-stack website built using the Django framework.

![Color Scheme](docs/readme/mockup_image_generated_with_techsini.png)

The live site deployed on Heroku can be found here: **[Dividend Dynamics](https://dividend-blog-app-7524309b6f0c.herokuapp.com/)**
 
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

My wireframes served as a rough guideline for the development, the user interface, and the overall appearance of the application. Bootstrap was used during development. Bootstrap has built-in breakpoints for different screen widths. Therefore, my influence on the appearance of the app in Bootstrap was naturally limited, and the user interface of the application is based on the breakpoints as well as how my application is displayed in Bootstrap on different devices.

### Wireframe landing | home page

![Wireframe_landing](docs/readme/wireframes/wireframe_landing.png)

### Wireframe blog page

![Wireframe_blog](docs/readme/wireframes/wireframe_blog.png)

### Wireframe about page

![Wireframe_about](docs/readme/wireframes/wireframe_about.png)

### Wireframe contact page

![Wireframe_contact](docs/readme/wireframes/wireframe_contact.png)

### Wireframe registration page

![Wireframe_registration](docs/readme/wireframes/wireframe_register.png)

### Wireframe login page

![Wireframe_login](docs/readme/wireframes/wireframe_login.png)

### Wireframe individual blogpost

![Wireframe_blogpost](docs/readme/wireframes/wireframe_individual_blogpost.png)

### Wireframe 404 page

![Wireframe_404_page](docs/readme/wireframes/wireframe_404_page.png)

### Wireframe landing | home mobile

![Wireframe_blogpost](docs/readme/wireframes/wireframe_landing_mobile.png)

## Database Schema

The database model (Entity Relationship Diagram | ERD) describes the connection among the different models used in the site.

The user model was created with Django-Allauth. ForeignKey relationships exists to Django's built-in User model for the DividendPosts and Discussion entities.

The UserContact, AboutPage, and NewsLetterSubscriber models/entities are independent entities with no explicit relationships to other models or entities in the Django project.

![Entity_Relationship_Diagram](docs/readme/entity_relationship_diagram.png)
	
## Color Scheme

The dividend blog app uses a color scheme to convey professionalism and trustworthiness. Both are key characteristics of finance-related content.
The blue color is associated with trust, stability, and professionalism and is widely used in the financial sector. The credibility of the content is supported by the use of this key color for headlines, titles, and important text elements. Gray is used as a contrast color. The gray color is neutral and symbolizes maturity, calmness, and sophistication. The gray colors are used for standard text to ensure readability and to complement and contrast the headline and title color. Gray is also used for background elements to support the main content.

While developing the app a lighthouse test resulted in a bad score for the initial color scheme. Therefore, the final color scheme as shown below was chosen to ensure sufficient contrast and the est possible accessibility.

![Color Scheme](docs/readme/coolors_color_palette.png)

## Typography

For my application, I selected Roboto and Times New Roman to enhance both visual appeal and readability. Times New Roman is chosen for body text due to its serif style, which conveys tradition, reliability, and professionalism—key attributes for a finance-related blog.

On the other hand, Roboto is used for headlines and titles. As a modern sans-serif font, Roboto provides a clean and contemporary look, ensuring excellent legibility on screens. Its straightforward design makes it ideal for drawing attention to important information while maintaining a sleek appearance.

The pairing of Times New Roman's traditional reliability with Roboto's modern clarityenhances readability and user engagement, offering a visually appealing and functional design for the financial content.

	
# Agile Development Process

Details on the agile development process can be found here **[agile.md](agile.md)**

# Features

Semantic HTML tags were used throughout the process. This allows search engines, screen readers, or other accessbility devices to access the content.

Use of Bootstrap allows to that styles are consistent and that site is visually appealing. The use of Bootstrap ensures that site is responsive across all devices with MFRD used in Bootstrap thus supporting progressive enhancement in the development process

## Hompage | Landing Page

The homepage | landing page includes navbar, footer, and information about the applications purpose.

Screen is different for registered and logged in users and users not logged in.

![Homepage_user_not_logged_in](docs/readme/features/feature_homepage_user_not_logged_in.png)


## Navigation | Logo | Favicon

The project features a user-friendly navigation system designed to enhance the overall experience. A key component of this navigation is the **logo**, which is seamlessly integrated into the layout.

### Logo Details | Favicon

- **Design Consistency**: The logo's style is intentionally aligned with the navigation icon (navicon), ensuring a cohesive visual identity across the entire application
  
- **Functionality**: The logo, when clicked, will reroute users back to the **landing page**. This feature provides a convenient way for users to return to the starting point of their journey within the application.

![Clickable_Logo_and_Favicon](docs/readme/features/feature_logo_and_favicon.png)

### Navigation

The application features an intuitive navigation system designed to enhance user experience. Below is a detailed description of the navigation components and their functionalities

#### Navigation Components

- **Navigation Items**: The navigation bar includes items that provide links to key sections of the application. Each item is labeled to help users find what they need quickly

- **Login Status**: The navigation also displays the user's login status. This feature allows users to easily see whether they are logged in and provides relevant options based on their authentication status

#### Design and Functionality

- **Consistent Styling**: The background color of navigation items is dynamically updated to match the main background color used throughout the application

#### Navigation Items for User Status

The navigation items differ based on the user's login status

- **Not Logged-In Users**: For users who are not logged in, the navigation includes items that direct the user to the blog page, login page, registration, about and contact

![Clickable_Logo_and_Favicon](docs/readme/features/features_navigation_including_login_status.png)

- **Logged-In Users**: For users who are logged in, the navigation displays additional 

![Clickable_Logo_and_Favicon](docs/readme/features/features_navigation_including_login_status_logedin_user.png)


## Blog Page | Blog App

The Blog Page is designed to enable users to view and interact with the blog post content. 

#### Blog Page

- **Display of All Blog Posts**: A dedicated blog page where all published blog posts are displayed. Users can easily scroll and paginate through the available content

![Blog_Page_with_pagination](docs/readme/features/blog_page_with_pagination.png)

#### User access to blog content | ability to make comments

- **Unregistered Users**: Both unregistered and registered users can view blog posts individually. This allows anyone to access the content

- **Registered Users**: While registered users can view all blog posts, only registered users have the ability to comment on posts. Comments on blog posts need approval by admin before the comment is made public to all other users on the blogpost page. The registered user is displayed the comments already made and still subject to approval by admin with message of either "approved" or "pending approval"

#### Individual Blogpost

Logged-in users have the ability to make comments on blog posts. Access to restricted content of functionality is therefore linked to role-based login.

The features on commenting are:

- **Comment Submission**: Registered users can submit comments on individual blog posts. However, comments submitted are not visible to other users until they are approved by an admin.

- **Pending Approval Notification**: Once a user submits a comment, the user receives a notification indicating that the comment is pending approval. This ensures transparency to the contributing user regarding the status of their submission

- **Approval Status Labels**: Comments awaiting approval are displayed with the label **"pending approval."** Once a comment has been approved by the admin, it is updated with the label **"approved."** This distinction helps users to understand the status of their comments

- **Edit and Delete Options**: Registered users also have the ability to edit or delete comments that have been previously approved by the admin. This feature provides users with control over their contributions

- **Returning to the Blog Page**: For convenience, users can easily navigate back to the main blog page that displays all blog posts. Each individual blog post includes a button that, when clicked, takes the user back to the blog listing page

![Blogpost_CRUD_features](docs/readme/features/individual_blogpost_crud_features.png)


## About Page | About App

The blog application includes a dedicated About page that provides information about the blog, its purpose, and its creators. This page can be managed and populated by an admin through a model interface. The admin panel for admin users can access the About model.

- **Admin Interface**: Admin users have access to a dedicated interface where they can create, edit, and delete content for the About page. Changes made by the admin are immediately reflected on the About page
  
- **Rich Text Support**: The About page can include formatted text or an image to enhance the information presented

- **Frontend**: The About page is designed to be visually consistent with the remainder of the application and includes a link to all blogposts to guide the user to the important content of the application

- **Access Control**: Only authenticated admin users (superusers) have the permission to access or modify the content of the About page.

![About_Page_Feature](docs/readme/features/feature_about_page.png)


## Contact Page | Contact App

The **Contact** feature allows users to submit messages via a contact form on the website. It includes the following functionality:

- **Contact Form Submission**: Users can fill out and submit the contact form with their details and message.
- **Form Handling**: The form is processed when a user submits it (via a POST request). If the form is valid, the data is saved, and a success message is displayed to the user.
- **Error Handling**: If the form contains invalid data, an error message is shown, and the form is re-rendered with the user's input preserved.
- **Form Rendering**: For GET requests, an empty form is rendered for the user to fill out.

![Contact_Page_Feature](docs/readme/features/feature_contact_page.png)

## Newsletter Signup Page | Newsletter App

The **Newsletter Subscription** feature allows users to sign up for a newsletter. 

- **Newsletter Subscription Form**: 
  The form is built on the `NewsLetterSubscriber` modeland includes fields for:
    - `email`: The user's email address
    - `name`: The user's name
  
  The form is designed to be user-friendly and uses Bootstrap classes for consistent styling across the website.

![Newsletter_AppFeature](docs/readme/features/feature_newsletter_signup_form.png)

### Call-to-Action Button in Footer

A "Sign Up for Our Newsletter" button is strategically placed in the footer of the website. This button remains visible across all pages, encouraging users to subscribe to the newsletter no matter where they are on the site. 

![Newsletter_AppFeature](docs/readme/features/feature_newsletter_button.png)

## Altert and feedback messages

User feedback was implemented with altert-messages. Changes in data such as login-status are alerted to user to confirm back to user successful completion of intended step.

![Alert_and_feedback_messages](docs/readme/features/features_altert_and_feedback_messages_part1.png)

When comment is posted, changed or deleted, the user is inform about successful completion. Alter-messages were implemented with Django altert messaging. The altert and feedback messaging was likewise used for the contact app and newsletter app providing immediate feedback to the user once changes in data are completed successfully.

![Alert_and_feedback_messages](docs/readme/features/features_altert_and_feedback_messages_part2.png)

## Registration Page

Users can register an account. The username and password are required fields while email is an optional field.

The sign-up form was styled to be consistent with the remaining colors of the site. Crispyforms was used for the layout of the form.

The username and password are clearly conveyed to the user to be required fields while providing the email adress is optional for the user.

User input data into the registration form is validated before submission can be executed successfully by the user. Input errors in the form are displayed to the user with messaging system. Successful completion and submission of the registration form is displayed to user with success message.

![User_registration_page](docs/readme/features/features_user_registration_page.png)

## Login Page

User can login once an account was created. Users logged-in can create, view, edit and delete comments on blogposts while users not registered and not logged-in can not use CRUD functionality for comments in blogposts.

The log-in/sign-in form was styled to be consistent with the remaining colors of the site. Crispyforms was used for the layout of the form.

User input data into the log-in/sign-in form is validated before submission can be executed successfully by the user. Input errors (such as wrong password or wrong username) in the form are displayed to the user with messaging system. Successful completion and submission of the registration form is displayed to user with success message.

![User_login_page](docs/readme/features/features_user_login_page.png)

## Logout | sign-out confirmation page

Users can securely log out of the application. Once the user clicks the logout button on any of the pages of the application, the user is redirected to the logout confirmation page.

The logout confirmation page form was styled to be consistent with the remaining colors of the site. 

Successful completion of the logout process is displayed to user with success message and redirect to the homepage/landing page.

![User_logout_confirmation_page](docs/readme/features/features_logout_confirmation_page.png)

## Customized 404 Error Page

To enhance user engagement and experience, a customized 404 error page has been implemented. This approach prevents the display of generic error messages and ensures that users encountering errors are provided with a more informative and user-friendly response.

### Key Features of the Customized 404 Page:

- **User Engagement and Experience**:
  - The customized 404 page is designed to support user engagement by providing a more tailored response to errors, avoiding the display of a generic error message.
  - It helps maintain user satisfaction by offering clear and helpful feedback when an error occurs.

- **Design Integration**:
  - The 404 page design is fully integrated with the overall design of the website, ensuring a consistent look and feel. 
  - It allows users to easily navigate back to the page where the error was encountered, minimizing disruption to their experience.

- **User-Centric Approach**:
  - This user-centric design reinforces the website’s commitment to providing a good user experience.

![404_page](docs/readme/features/screenshot_404_page.png)

## Possible future features

Future features may include the following

- Confirmation email once users register to the page or user sign-up/registration made dependent on user to confirm the sign-up process
- Options for user to reset password. I a user forgot the password, user can access a page with password reset email notification
- Sign-in via social accounts
- Creation of a user profile page
- Ability for user to assign likes or unlike a certain comment or blogpost

# Technologies

This is a full-stack (front-end/back-end) project with the primary use of HTML, CSS, and Python. The backend uses the Python framework Django.

The frontend primarily relies on the CSS framework Bootstrap for the efficient layout of mobile-first responsive design (MFRD).

## Django-based technologies

**[Django](https://www.djangoproject.com/)** Django is an open-source web framework for building robust and dynamic web applications

**[AllAuth](https://docs.allauth.org/en/latest/)** A Django package with views and templates for features such as authentication, registration, or account management

**[Cloudinary](https://cloudinary.com/)** Cloudinary is an image/video management solution for websites to easily upload images to the cloud with the delivery of media files through a fast content delivery network (CDN)

**[CrispyForms](https://pypi.org/project/django-crispy-forms/)** Crispy Forms is a third-party Django app to manage Django forms with Bootstrap styles

**[Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/)** Crispy Bootstrap5 is a Bootstrap template pack for Django Crispy Forms

**[Summernote](https://summernote.org/)** Summernote is a JavaScript library that allows to create a WYSIWYG (What You See Is What You Get) editor

**[Gunicorn](https://gunicorn.org/)** Gunicorn is a Python WSGI HTTP Server for UNIX. WSGI stands for Web Server Gateway Interface and is a specification for communication between web servers and Python web applications. Gunicorn is the equivalent of 'manage.py runserver' used in the development but with speed and security optimization

**[psycopg2](https://pypi.org/project/psycopg2/)** Pycopg2 is a PostgreSQL database adapter for the Python programming language

**[Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html)** Whitenoise is a Python package that allows the Heroku app to serve its own static files without relying on an external file hosting service such as a content delivery network (CDN)
															
**[CoideInstitutePostgreSQL](https://dbs.ci-dbs.net/)** PostgreSQL from Code Institute to create a database

**[Browserling](https://www.browserling.com/)** Browserling is a web-based cross-browser testing software that allows users to test the website across desktop and mobile browsers such as Chrome, Firefox, Edge, or Opera without downloading and installing the respective browser

**[CI Python Linter](https://pep8ci.herokuapp.com/)** The Code Institute Python Linter was used to validate Python code

**[Favicon](https://favicon.io/favicon-generator/)** Favicon generates favicons

**[Fontawesome](https://fontawesome.com/)** fontawesome was used for icons

**[GitHub](https://github.com/)** The code files, README files, and assets are stored on GitHub. The code on GitHub was pushed from Git

**[Git](https://git-scm.com/)** The version control system Git was used to document the development of the application and to push code to the GitHub repository. The specific reasons for the commit are reflected in the respective commit message

**[Google fonts](https://fonts.google.com/)** googlefonts were used for customized use of font-types

**[Grammarly](https://app.grammarly.com/)** Grammarly is an online grammar-check tool to check English grammar and eliminate writing mistakes

**[Heroku](https://www.heroku.com/)** Heroku is a platform as a service (PaaS) to build, run, and operate cloud-based applications. It was used to deploy the website

**[Lucid Chart](https://www.lucidchart.com/pages/)** Lucid Chart is a web-based diagramming tool to create flowcharts, wireframes, and visualisation of concepts			

**[Python](https://www.python.org/)** Python is an interpreted, high-level general-purpose programming language

**[Random Key Generator](https://acte.ltd/utils/randomkeygen)** Random key generator to create a SECRET_KEY for the Django app that is different from the secret key created initially and generated once the env.py and .gitignore already existed to ensure that no secret information is shared in the commits

**[Techsini](https://techsini.com/multi-mockup/)** Multi Device Website Mockup generator

**[Tinypng](https://tinypng.com/)** To reduce the size of the images used and improve lighthouse score on performance	

**[Visual Studio Code](https://code.visualstudio.com/)** Visual Studio Code (VS-Code) was used as an integrated development environment (IDE) for the entire project. The GitHub repository was cloned to VS-Code for this purpose

# Bugs and issues

**Erroneously Renaming Django Project Folder**

After the initial set-up of the Django project, I wanted to test the deployment in Heroku using the django project name 'testproject'. It was a fully erroneous assumption that a simple change of the Django project name with a change of the project folder to 'diviblog' will keep my django project running. I learned that hard way that I have to review and adjust the wsgi.py, asgi.py, manage.py and settings.py with the new app name that I assigned to the existing Django project originally named 'testproject'.

**HTML tag rendering in single_post.html for individual posts clicked**

My 'bold' HTML -tag included in the posts.json in fixtures for the blog body (content) did initially not render on the single_post.html page. I reviewed the |safe filter to ensure that Django is not escaping the HTML-tag for XSS reasons

**static/css/style.css only partly working on classes defined in 404.html**
For my 404.html I defined classes in the markup of the 404.html. I did load static and connect the stylesheet correctly from static/css/style.css. Nevertheless, the styles in
my style.css were only PARTLY applied to the 404.html. Some styles affected the 404.html, some did not. I change class names in 404.html to be as distinctly different from bootstrap classes as possible to avoid that bootstrap is over-riding my custom CSS for the 404.html page but this did likewise not work. I decided to make the the styles of the 404.html with an internal stylesheet inside the 404.html and everything worked out well. Adds some more complexity maintaining the code as I have defined custom properties in
my CSS stylesheet and when one of these custom properties such as colors changes, the internal stylesheet of the 404.html would need additional attention to synchronise colors with potentially changed colors of my custom CSS defined in the :root of my CSS stylesheet

- **Update and correction of bug 404.html**: After a project call with my mentor, David Bowers, I learned the correct approach of connecting the style.css with the 404.html page and this issue of separating CSS styling for the 404.html with inline styles in the 404.html from the rest of the CSS styling in the style.css was resolved. Resolution was achieved by adding not only {% static %} but likewise load the base.html and "simply" insert the 404 text & button as {% blockcontent %} 

**Debug on False and change of styles in style.css**
After running a deployment test on heroku I did not reset the debug to True. I tried to change some of my custom styles in my style.css but none of the new styles in the stylesheet was applied. I increased specificity of CSS styles and even emptied the entire style.css for testing purposes only to learn that my "old" styles from the style.css are still applied. Puzzled by the fact that styles are applied even if a stylesheet is entirely empty but correctly connected, I stopped development for the day. Rethinking the issue while the code editor was turned off, I speculated that django was using the stylesheet inside the staticfiles as my debug of FALSE was in "production mode". Quite logically, I can change my style.css as much as I want to with no effect as long as Django is using the style.css from staticfiles with debug on FALSE. I changed debug back to TRUE and all my issues with style.css were resolved. Do not really know whether my theory is correct but all simple changes in styles were done once I changed the DEBUG back to true.

# Testing

## Automated Testing

1. **[W3C Markup Validation Service](https://validator.w3.org/) - HTML Validation**
The W3 HTML validator was used throughout the developmeht phase to ensure consistency with HTML standards. All site pages were tested with official W3C validator for both users logged in and those not logged in. HTML validation was done with the renedered pages. The reason for this is that W3C validation does not recognize Django template language (DTL).

| URL Path                                | Screenshot                                    |
|-----------------------------------------|-----------------------------------------------|
| home                                    | ![Default_Value](docs/readme/testing/w3c_validation_check_homepage.png) |
| home/blog                               | ![Default_Value](docs/readme/testing/w3c_validation_check_home_blog.png) |
| home/about                              | ![Default_Value](docs/readme/testing/w3c_validation_home_about.png) |
| home/contact                            | ![Default_Value](docs/readme/testing/w3c_validation_home_contact.png) |
| home/accounts/logout/                   | ![Default_Value](docs/readme/testing/w3c_validation_home_accounts_logout.png) |
| home/accounts/signup/                   | ![Default_Value](docs/readme/testing/w3c_validation_home_accounts_signup.png) |
| home/accounts/login/                    | ![Default_Value](docs/readme/testing/w3c_validation_home_accounts_login.png) |
| home/newsletter/subscribe/              | ![Default_Value](docs/readme/testing/w3c_validation_home_newsletter_subscribe.png) |
| home/blog/post/A-SINGLE-BLOGPOST/       | ![Default_Value](docs/readme/testing/w3c_validation_home_blog_post_singlepost.png) |
| home/404_page/                          | ![Default_Value](docs/readme/testing/w3c_validation_home_404_page.png) |

2. **[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) - CSS Validation**

The CSS stylesheet was tested with the W3C CSS validator. No error messages or syntactical errors.

![Jigsaw CSS valiation](docs/readme/css_jigsaw_w3c_validation_outcome.png)

3. **[CI Python Linter](https://pep8ci.herokuapp.com/)** The Code Institute Python Linter was used to validate Python code

![Python Validation](docs/readme/testing/table_summary_for_automated_py_testing_with_pep8_linter.png)

4. **[Google Lighthouse](https://developers.google.com/web/tools/lighthouse)**

Performance of pages, best practices and SEO was tested for every page with Lighthouse. Instead of inserting many different screenshots of all lighthouse results, the lighthouse results are summarised as per tables below.

#### Lighthouse results Desktop

| **Page**                           | **Performance** | **Accessibility** | **Best Practices** | **SEO** |
|------------------------------------|----------------|-------------------|--------------------|---------|
| home                               | 99             | 100               | 100                | 100     |
| home/blog                          | 100            | 100               | 100                | 100     |
| home/about                         | 100            | 100               | 100                | 100     |
| home/contact                       | 100            | 100               | 100                | 100     |
| home/accounts/logout/              | 100            | 100               | 100                | 100     |
| home/accounts/signup/              | 100            | 100               | 100                | 100     |
| home/accounts/login/               | 100            | 100               | 100                | 100     |
| home/newsletter/subscribe/         | 100            | 100               | 100                | 100     |
| home/blog/post/A-SINGLE-BLOGPOST/ | 100            | 98                | 100                | 100     |
| home/404_page/ | 100            | 100                | 96                | 91     |

#### Lighthouse results Mobile

| **Page**                           | **Performance** | **Accessibility** | **Best Practices** | **SEO** |
|------------------------------------|----------------|-------------------|--------------------|---------|
| home                               | 90             | 100               | 96                 | 100     |
| home/blog                          | 90             | 100               | 96                 | 100     |
| home/about                         | 94             | 100               | 96                 | 100     |
| home/contact                       | 95             | 100               | 96                 | 100     |
| home/accounts/logout/              | 98             | 100               | 96                 | 100     |
| home/accounts/signup/              | 99             | 100               | 96                 | 100     |
| home/accounts/login/               | 96             | 100               | 96                 | 100     |
| home/newsletter/subscribe/         | 96             | 100               | 96                 | 100     |
| home/blog/post/A-SINGLE-BLOGPOST/ | 92             | 98                | 96                 | 100     |
| home/404_page/ | 99             | 100                | 93                 | 91     |

5. **[JS_hint](https://jshint.com/)**
I have configured JSHint to support ES6 features, and the code is functioning correctly; however, I was unable to resolve the warning regarding the undefined variable bootstrap, as the Bootstrap modal is working as intended.

![JavaScirpt Validation](docs/readme/testing/js_hint_testing_of_js_code.png)

6. **Accessibility testing**

Accessbility testing with color scheme was built into the development process. A sufficient contrast in the color palette was used to ensure accessibility. This is verified by the lighthouse results on accessibility.

Good accessibility was likewise achieved with the use of semantic HTML tags to facilitate access to the application with screenreaders.

## Manual Testing

Manual testing was carried out repeatedly throughout the entire development. During the development phase, an Excel table was created during the manual testing in which the results of the manual testing were documented. At the end of the development and after iteration 6 was closed, all features were manually tested again, and the result of the manual test was finally documented.

### Manual Testing Page 1

![Manual_Testing_Page_1](docs/readme/testing/manual_testing/manual_testing_page_1.png)

### Manual Testing Page 2

![Manual_Testing_Page_2](docs/readme/testing/manual_testing/manual_testing_page_2.png)

### Manual Testing Page 3

![Manual_Testing_Page_3](docs/readme/testing/manual_testing/manual_testing_page_3.png)

### Manual Testing Page 4

![Manual_Testing_Page_4](docs/readme/testing/manual_testing/manual_testing_page_4.png)

### Manual Testing Page 5

![Manual_Testing_Page_5](docs/readme/testing/manual_testing/manual_testing_page_5.png)

### Manual Testing Page 6

![Manual_Testing_Page_6](docs/readme/testing/manual_testing/manual_testing_page_6.png)

### Manual Testing Page 7

![Manual_Testing_Page_7](docs/readme/testing/manual_testing/manual_testing_page_7.png)

### Manual Testing Page 8

![Manual_Testing_Page_8](docs/readme/testing/manual_testing/manual_testing_page_8.png)

![Manual_Testing_Page_8](docs/readme/testing/manual_testing/manual_testing_page_8_continued.png)

### Manual Testing Page 9

![Manual_Testing_Page_9](docs/readme/testing/manual_testing/manual_testing_page_9.png)


# Security Features

- **User Authentication**:
  - Only superusers can access the admin panel; normal users do not have access.

- **Secret Keys Management**:
  - All `SECRET_KEY` values are stored separately in an `env.py` file and in config vars on Heroku.
  - The `env.py` file is excluded from version control using `.gitignore`, ensuring that sensitive information is not exposed on GitHub.
  - A new `SECRET_KEY` was generated using a `secret_key` generator after the initial setup of the `.gitignore` and `env.py` file for enhanced security.

- **Environment Variables**:
  - Critical environment variables such as `DATABASE_URL` and `CLOUDINARY_URL` are stored in the `env.py` file and as config vars on Heroku for secure access.

# Credits
The project follows the walkthrough project of Matt Rudge from Code Institute named "I Think Therefore I Blog". Using the walkthrough project as a guide improved my understanding of the project goals. I changed the models, including modifications to class names and field names. Additionally, I customized the views and rendering of data in the templates to better suit the specific requirements of my application. I benchmarked and compared the code from the walkthrough project to ensure that my implementation is unique and distinct. Through modifications, I have made the best effort possible to create original work.

For my contact app, I used **[Contact_App_Reference_Material](https://pythonguides.com/contact-form-with-django-and-sqlite/).** I made significant modifications and customizations to this code including adjustment of the model (class names, field names) so that the contact app is distinctly different from the reference material. The adapted code and rendered page was styled with custom CSS stylesheet.

The custom `404.html` page was created using the guidance from **[Create_Custom_404_error_page](https://www.makeuseof.com/create-custom-404-error-page-django/).**

For the newsletter signup feature, I referred to this source: **[NewsLetter_with_Django](https://dev.to/shubhamkshatriya25/how-to-build-a-email-newsletter-subscriber-in-django-j2p)**.
The code mentioned in this source was modified and adjusted to ensure that the model, view, and template used are as different as possible from the code used in this source.

## Code

The Readme.md file follows the structure of Readme.md provided by Code Institute **[Code Institute readme template](https://github.com/Code-Institute-Solutions/readme-template)**. 

The video titled **[README.md - Manual Testing Write Up Overview](https://www.youtube.com/watch?v=Q66HZgkDSOo)** by Kasia Bogucka made it easy to structure the README section on testing.

The video titled **[README.md - How, What and When?](https://www.youtube.com/watch?v=l1DE7L-4eKQ)** by Kasia Bogucka.

The video titled **[Guide to Github Aigle Tool](https://www.youtube.com/watch?v=U_dMihBgUNY&list=PL_7334VduOHsrWzhu5Ta2lrkp016kcBWY&index=20)** by Kasia Bogucka helped to understand the organisation of the agile development process. 

The video titled **[Community Q&A: Validating Your Code Before Project Submission]((https://www.youtube.com/watch?v=wiqAvRCheKo&list=PL_7334VduOHsrWzhu5Ta2lrkp016kcBWY&index=17))** by Code Institute provided good instructions on code validation/linter. Validation of HTML, CSS, Python, and Javascript was done throughout the project development and not just at the end of the project.

The video titled **[Guide to MVP](https://www.youtube.com/watch?v=vIv1c6RLBac)** by Kasia Bogucka provided additional insights and understanding to the PP-4 specifications and project requirements.

The video titled **[Community Q&A: PP4 Project FAQ's](https://www.youtube.com/watch?v=Q5cdZXomzVg)** was used to have some more clarity about the project requirements.

Notes from the call **"Community Q&A: Mastering Full Stack Applications: Your Way to PP4 Success"** webinar held on July 30, 2024.

## Content Data Sources

The dividend history and stability information presented in this blog app are sourced from **[Aktien Guide](https://aktien.guide/dividendenadel)**, a comprehensive resource for dividend data. Company descriptions are derived from official company websites and reputable public sources to ensure accuracy and reliability. This approach ensures that the content provided is both informative and up-to-date.

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
    
1. Log in to Heroku under **[Heroku](https://id.heroku.com/login)**
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

## Local Development

### How to Fork the project

1. Log in or Sign Up on GitHub
2. The repository of this project can be found at **[Project Repository](https://github.com/Werner-Staeblein/Project-4)**
3. The "Fork" button is a the top right of the page. The "Fork" button is located immdiately left to the button ***Star***. Click on the button named "Fork"
4. A new page titled "Create a new fork" will be shown
5. At the bottom of the new page click on "Create fork"
6. With steps 1. to 5. completed, a copy of the project exists in your list of repositories

### How to Clone the Project

1. Log in or Sign Up on GitHub
2. The repository of this project can be found at **[Project Repository](https://github.com/Werner-Staeblein/Project-4)**
3. Click on button named "Code" button. Here, you can choose a clone method (HTTPS, SSH, Github CLI). The link provided must be copied
4. In your code editor navigate to the directory where you would want to clone the repository
5. In the terminal of your code editor, type 'git clone'. Here, the copied link must be pasted. Finish the step by pressing Enter

# Acknowledgements

A heartfelt thanks goes to my mentor, David Bowers, for the unwavering support and guidance throughout this project. His encouragement and insights have been invaluable in keeping me motivated and on track.

I also want to acknowledge the Slack community for their diverse ideas and discussions, as well as the forum members whose questions and answers helped me navigate potential pitfalls and refine my approach.

*****************

[Back to top](#table-of-contents)