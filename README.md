# Sparkling-Astro: Zodiac Sign & numerology value

<div align="center">
  <img width="1064" alt="responsive page" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/85330f2c-48dd-4867-b906-dff758328000">
  </div>

# Table of Contents

- [Repository](#repository)
- [Introduction](#introduction)
- [Project Goals](#project-goals)
- [User Experience](#user-experience)
- [Design](#design)
    - [Color](#color)
- [Feature](#feature)
    - [Main Page](#main-page)
        - [Option 1](#option-1)
        - [Option 2](#option-2)
        - [Option 3](#option-3)
        - [Option 4](#option-4)
- [Testing](#testing)
    - [Python Linter Testing](#python-linter-testing)
    - [Bugs](#bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Technologies used](#technologies-used)
- [Credits](#credits)
    - [Acknowledgments](#acknowledgments)

<hr>

# Repository

[GitHub Repository](https://github.com/Dayasuvagiya/SparkLing)

Live: [https://.herokuapp.com/](https://sparkling-asro-2f4fa7a9d813.herokuapp.com/)

<hr>

# Introduction
Welcome to our comprehensive program where you can explore your zodiac sign, discover the numerology value of your name, and gain insights into general personality traits associated with each zodiac sign. Unveil the mysteries of the stars and numbers as you embark on a transformative journey of self-discovery.

<hr>

## Project Goals
The objective of this project was to demonstrate the use of Python for backend technology. To enhance user engagement and usability, I decided to create an interactive and enjoyable experience.

<div align="center">
  <img width="1170" alt="Screenshot 2023-06-24 at 22 03 30" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/cec820e8-5a7b-4ec7-a32d-9964f6e24991">
  </div>
  
<hr>

## User Experience 

The user experience of this app is designed to be intuitive and informative, catering to users who are curious about numerology and astrology. Here's how the user journey unfolds:

1. User-Friendly Interface: The app features a user-friendly interface, allowing users to easily navigate through the different options and input their information.

2. Zodiac Sign Retrieval: Users can start by inserting the first letter of their name, and the app instantly reveals their corresponding zodiac sign. 

3. Personality Insights: By clicking on the third option, users can access detailed information about their zodiac sign's personality traits. 

4. Numerology Calculation: For users interested in numerology, the app provides the option to input their full name. The system then performs the calculations and reveals the final number associated with the user according to numerology. This feature eliminates the need for manual calculations, making it convenient for users to discover their numerological value.

<hr>

## Design

### Color
The color scheme of the font utilized in this project, implemented through the installation of the Python Colorama module, enhances user experience and visual clarity. The deliberate use of green color to highlight correct answers, red color to signify error messages, and cyan color for the initial part of the page create a visually pleasing and intuitive interface, ensuring that users can easily identify and differentiate relevant information. By employing these color choices strategically, the project achieves a professional and aesthetically appealing presentation. 

1. The initial page of the program utilizes a visually pleasing cyan color scheme to create an appealing and attractive appearance for users.

2. Correct outputs are displayed in a green color font, offering users a clear indication of successful outcomes and reinforcing a positive user experience.

3. In contrast, error messages are presented in a red color font, ensuring high visibility and alerting users to incorrect input, thereby facilitating quick identification and resolution of any issues.

<hr>

# Feature

## Main Page

<div align="center">
  <img width="784" alt="main 1" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/c5f0450e-0cb5-45ae-bf74-e6c13f5f3ac4">
  </div>
  
  
The main page of the screen serves as a concise introduction to the program, providing users with key information about its purpose and functionality. The page presents four distinct options for users to choose from, enabling them to navigate through different sections or access specific features according to their preferences and needs. 

 1. Discover your Zodiac identity through your name.
 2. Discover numerology value of your name.
 3. Read personality traits based on your Zodiac sign.
 4. Exit program.

### Option 1:

<div align="center">
  <img width="784" alt="option 1" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/7f8770d2-c3d7-4d8b-ade4-04ed136352df">
  </div>


- Upon selecting option one from the main menu, users are presented with a straightforward input option where they can enter the first letter of their name to check their corresponding zodiac sign.

<div align="center">
  <img width="784" alt="option 1-2" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/7973c7f9-efde-40eb-bb76-cae0e933fb68">
  </div>
  

- If the user enters more than one letter or number in the first option, an error message will be displayed, providing instructions to enter only the first letter of their name. An example will be given to illustrate the expected input format.

### Option 2:

<div align="center">
  <img width="784" alt="option 2" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/8aadecbf-628f-4201-8dc5-9ea7231e2a9e">
  </div>
  
  
- When choosing option two from the menu, users can obtain the numerology value of their name by simply entering their first name.

<div align="center">
  <img width="784" alt="option 2-2" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/d2ac62dd-b41a-411b-a927-2f3beeeb62ac">
  </div>
  
  
- After choosing the second option, users have the opportunity to retrieve their numerology value. Nevertheless, in the event that users input numbers or symbols instead of letters, an error message will be promptly displayed, guiding them to input letters exclusively. This ensures that users are aware of the required input format and helps them avoid any potential confusion or incorrect results.

### Option 3:

<div align="center">
  <img width="784" alt="option 3" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/8f6fd711-bfab-4dea-a7d9-e83f66020e09">
  </div>
  
  
- Opting for option three from the menu allows users to explore general personality traits associated with their zodiac sign. This feature caters to users' curiosity, providing insights into the personality characteristics commonly observed in individuals based on their zodiac sign.

### Option 4:

<div align="center">
  <img width="784" alt="exit" src="https://github.com/Dayasuvagiya/SparkLing/assets/130157117/b4c9600f-8a1f-4ab7-869d-3c7b87ecc759">
  </div>
  

- Upon selecting option three from the main menu, users have the option to exit the program. This choice allows users to gracefully exit the application when they have completed their desired tasks or no longer wish to continue using the program. 

<hr>

# Future Features 

1. An interactive daily horoscope feature providing personalized predictions and insights based on the user's zodiac sign, enabling users to navigate their day and make informed decisions.

2. A comprehensive astrology and numerology glossary, providing definitions, explanations, and examples of key terms and concepts, allowing users to deepen their understanding of these subjects.

<hr>

# Testing 

## Python Linter Testing

Upon running my code through Code Institutes Python linter, it successfully returned a result with Whiteline error and 501 error(3 lines are too long) detected errors. 

### 1. Run
### **Results:**
#### 3 occasions of "expected 2 blank lines, found 1"
#### 5 occasions of "trailing whitespace"
#### 3 occasions of "line too long"

### 2. Run
### **Results:**
3 occasions of "line too long" is not solved. Rest I have successfully solved.

<hr>

## Bugs
Through testing, I discovered some potential issues in the code and made some changes to prevent errors caused by incorrect user input:
1. An issue arose when users selected an invalid option, resulting in the display of multiple error messages. However, this issue has been successfully addressed and resolved. 

2. When a user is requested to enter a letter in Uppercase or Capitalize, I modified the code to accept the letters in capital and convert them into small letters. 

<hr>

## Deployment

### Heroku

- Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't.
- Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
- In the "App name" field enter the name of your app. This name has to be unique.
    - Heroku displays a green tick if your app name is available.
- In the "Choose a region" field choose either the United States or Europe based on your location.
- Click the "Create app" button.
- Next page, top center of the screen, select the "Settings" tab.
- Just below in the "Buildpacks" section click on the "Add build back" button. Buildpacks have to be installed in this order.
    1. Click on the "Python" button to select it and then the "Save changes" button.
    2. Click again on the "Add build back" button.
    3. Click on the "nodejs" button to select it and then the "Save changes" button.
- Go back to the top of the screen and select the "Deploy" tab.
- In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Enable Automatic Deploys" button to update the deploy also when you push a new commit to GitHub.
    3. At the very bottom of the page click on the "Deploy Branch" button.
- You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.

<hr>

# Technologies used 

- Python3: The main code used.
- Colorama library: To give content color
- Visual Studio: Used to host and edit all code and the website.
- Github: Used to deploy the website.
- ChatGPT: I utilized the tool as a means to effectively structure and organize my wording across the entirety of the readme file.

<hr>

# Credits 

## Acknowledgments
The site was completed as a Portfolio Project 3 piece for the Full Stack Software Developer, Diploma at the Code Institute. As such I would like to thank my mentor, the Slack community, and all at the Code Institute for their help and support.

Thanks to the Love Sandwiches module. This was incredibly engaging and helpful.

Online references about industrial standards and Youtube and google with guides.

