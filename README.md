# Artly

This is a README document for the back-end repository Artly_api that provides api functionality to the front-end repository Artly. 

You can access the Artly repository [here](https://github.com/laurakond/Artly). 

Live site can be found [here]().

(By Laura Kondrataite)

## Table of Contents

[Agile Methodology](#agile-methodology)

- [GitHub Project Management](#github-project-management)

[Features](#features)

- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

[Technologies used](#technologies-used)

- [Languages](#languages)
- [Frameworks and Libraries](#frameworks-and-libraries)
- [Databases](#databases)
- [Other Tools, technologies, packages](#other-tools-technologies-packages)

[Testing](#testing)

[Deployment](#deployment)

- [Github](#github)
  - [How to Fork](#how-to-fork)
  - [How to Clone](#how-to-clone)
- [Heroku](#heroku)

[Credits](#credits)

- [Content](#content)
- [Used code](#used-code)
- [General resources](#general-resources)
- [Acknowledgments](#acknowledgments)
- [Code inspiration](#code-inspiration)
- [References](#references)

[Return to Table of Contents](#table-of-contents)

## Design

### Target Audience

The primary target audience for the game is:

- persons of any gender aged 16+ who enjoy crafts,
- first time cross-stitchers,
- anyone looking for guidance on how to progress in their cross-stitch journey.

No background, geographical location or income has been specified for the target audience.

### User Stories

### Flowcharts

I used [Lucidchart](https://lucid.app/) for creating the ERD for the models and [Exslidraw](https://excalidraw.com/) for creating site navigation.

- ERD:

  ![Project Models](documentation/images/entity_relational_diagram/model-chart.png)

- MVP flowchart:

  ![flowchart-mvp](documentation/images/entity_relational_diagram/site-navigation.png)

### Wireframes

The following wireframes show the initial idea of how the website would look on different devices: mobiles, tablets/iPads and laptops/desktops.

[]()

### Color palette

The following palette was used to ensure the contrast is achieved between the main parts of the website:

<details>
    <summary>Color palette images</summary>

![Color palette]()
![Color palette2](documentation/design/color-palette2.jpeg)

</details>

<br>


### Font styles

I used [Google fonts](https://fonts.google.com/) to source the fonts for the website. These are:


![font screenshots]()

[Return to Table of Contents](#table-of-contents)

## Agile Methodology

### GitHub Project Management

![GitHub Project Management]()

- [GitHub Project board]() was used to manage the progress and development of this project.
- It allowed me to scope the project and keep track of progress, sometimes revising estimated dates and tasks that were needed to be done by a certain point.

![GitHub Project Management]()

- I chose the "trafic-light" color scheme for the MoSCoW method in order to indicate which tasks were a priority (green must-haves) and which ones were not(red won't-haves) for my project board.
  - This provided clarity and better understanding for myself as I was a sole project contributor.

[Return to Table of Contents](#table-of-contents)

## Features

### Existing Features

**The Header**

  ![header]()

  ![loggedin header]()

**The Footer**

  ![footer]()

**User authentication**

<details>
<summary></summary>

  </details>

**Restricted access**

**Error pages**

**Notification messages**

<details>
    <summary></summary>

</details>


### Features Left to Implement


[Return to Table of Contents](#table-of-contents)

## Technologies used

### Languages


### Frameworks and Libraries

### Databases

- PostgreSQL: the database used to store all the data.
- Sqlite3: the database used for automated testing.

### Other tools, technologies, packages

- [Django allauth](https://allauth.org/) authentication library was used for allowing users to register and login.
- [GitHub](https://github.com/) was used for creating and storing files and folders of the website.
- [Heroku](https://www.heroku.com) was used for accessing and storing my application game.
- **Git** was used for version control.
- **Pip** was used to install required dependencies.
- **Gitpod** cloud editor was used for writing the code.
- **Gunicorn** webserver used to run the website.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) was used for validating and checking my code for best code practices.
- [JS Hint](https://jshint.com/) was used for validating Javascript code.
- [W3C Markdown](https://validator.w3.org/) was used for validating html files.
- [W3C CSS](https://jigsaw.w3.org/css-validator/) was used for validating css files.
- [Lucidchart](https://lucid.app/) and [Exslidraw](https://excalidraw.com/) was used for creating ERDs.


Full list of dependencies used for the project can be found in the requirements.txt file.

[Return to Table of Contents](#table-of-contents)

## Testing

The website went through extensive testing during the development and deployment stages.

- See [TESTING.md](TESTING.md) file for full testing and validation information.

**Visible sqlite3 file**

- db.sqlite3 file is exposed within the file structure, which was done unintentionally. I have taken note of best practices going forward and will ensure that any future files are stored in the .gitignore file.


[Return to Table of Contents](#table-of-contents)

## Deployment

This website was deployed using GitHub pages and Heroku website. To deploy the project, follow the steps below:

### Github

1. Login to GitHub and navigate to the main repository page.
2. Click on the chosen repository,for example [Stitch Art Guides](https://github.com/laurakond/Stitch-Art-Guides-pp4).
3. Once inside the repository, click on the "Settings" tab above the repository title displayed around the middle of the page.
4. Select "Pages" tab on the left side navigation menu.
5. Select "main" or "master" branch under "Build and Deployment", then "root" folder and click "save" button.
6. The GitHub page site will be deployed.
   - It might take a few minutes to generate the "live" website link.

The live link to the website can be found [here](https://stitch-art-guides-pp4-5a679feed1e1.herokuapp.com/).

#### How to Fork

To fork the repository in Github:

1. Follow steps 1 & 2 as above.
2. Once inside the chosen repository, click the "fork" button in the top right corner above the "About section".

#### How to Clone

To clone the repository in Github:

1.  Follow steps 1 & 2 as in the deployment section above.
2.  Click on the "Code" button (often a bright color that stands out) at the top right corner just above the "commits" history.
    - Select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
3.  Open the terminal in your chosen code editor and change the current working directory to the location you want to use for the cloned directory.
    - Type 'git clone' into the terminal and then paste the copied link and press enter.
    - OR, if working with VSCode, select "Clone Git Repository" and save the file on your device as prompted.
4.  If you are working on a local IDE such as VS code, you need to create a virtual environment:
    - in the terminal write the command `python -m venv [directory-name]`
    - To activate the virtual environment write `[directory-name]/Scripts/Activate`
    - If you need to deactivate it, type `deactivate` in the terminal
    - remember to include this to the .gitignore file
5.  Next, create an env.py file where you will keep your key data and make sure it is included in the .gitignore file. Key data can include:
    - DATABASE_URL
    - SECRET_KEY
    - CLOUDINARY_URL
    - SITE_OWNER_EMAIL
    - SITE_OWNER_PASSWORD
6.  Import all the dependencies required for the project to run. You can do so by entering `pip install -r requirements.txt` for the VSCode or `pip3 install -r requirements.txt` for Gitpod IDE.
7.  Set up a database using postgreSQL.

### Heroku


[Return to Table of Contents](#table-of-contents)

## Credits

### Content

### Used code


### General resources:

<details>
<summary></summary>

</details>

### Acknowledgments

My thanks go to:

- My mentor, [Iuliia Konovalova](https://github.com/IuliiaKonovalova), for helping to organise and plan my project and for advising how to approach this project.

- My fellow student, [Vernell Clark](https://github.com/VCGithubCode), for moral support and advice on how to approach project planning.

- [Daisy McGirr](https://github.com/Dee-McG) for helping to cristalise my project idea, troubleshooting concepts I could not wrap my head around and moral support.

### Code Inspiration

### References
- I used Code Institute's DRF API [project](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106) as a base for my own.
- I referred to AsiaWi [Snap it up](https://github.com/AsiaWi/snap-it-up-backend/blob/main/offers/views.py) snippet of code to help me write the logic and functionality for my Bid Offer views.

[Return to Table of Contents](#table-of-contents)
