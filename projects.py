PROJECTS = [
        {
            "date": "2025",
            "title": "Sweatris (uOttaHack 7)",
            "description": """ Sweatris a Fitness-Themed Interactive Tetris Game, 
                                a web-based application that combines physical activity and gaming for a fun, 
                                engaging workout experience. Using object detection and an intelligent algorithm for move recommendations, 
                                this project turns your movements into game controls, allowing you to play Tetris while staying active! With 800+ hackers participating in the uOttahack 7 hackathon, 
                                this project got First Place in NAV CANADA’s challenge
                                and Third Place in uOttaHack 7 General Category. Side Note: The naive highschooler would have been proud to know that the live demo did not fail"""
        },
        {
            "date": "2024-Present",
            "title": "Data Science Sounds Fun", 
            "description": """Imagine you are a university student and winter break has started, suddenly you have nothing to do so what better thing to do than learn! • Performed data cleaning and encoding of categorical data with Scikit-Learn, Pandas and Numpy.
                            • Split data parsed from a CSV and stored it as a dataframe, which is then split in to X(independent variables) and y(dependent variable) datasets. 
                            The X and y datasets are then split into X_train, X_test, y_train, y_test by using the Scikit-Learn library
                                and a 80:20(train to test ratio, this ensures that 80% of the data parsed from the CSV file is allocated to training the model
                            and the other 20% is used to test the model to see how accurate its predictions are, this ratio can change based on the size of the datasets).
                            • Used Scikit-Learn to train different Simple/Multiple linear regression, polynomial regression, support vector regression,
                            decision tree regression, and random forest regression models to predict salaries based on someone’s previous position in a company.
                            • Used Scikit-Learn to train a logistic regression and K-nearest neighbors based classification models to classify whether someone with a certain age and salary would purchase a car.
                            • Plotted test and training data with respect to predicted/real values with Plotly, and Matplotlib.
                            • I have also performed the above data analysis using R and its respective libraries."""
        },
        {
            "date": "2024",
            "title": "A Basic Computer", 
            "description": """• Used an FPGA for this project.
                                • Developed the ALU (Arithmetic Logic Unit) of the basic computer so that it would be able to perform simple addition,
                                    subtraction, multiplication by 2, and perform logical operations like “AND”.
                                • Developed a controller for the basic computer which would be able to detect the set flags in the basic computer, for
                                    example, to check if the assembly instruction CMA (Compliment the value in the accumulator) is called then the controller
                                    would check the instruction cycle the computer is currently in and the first few bits of the instruction register. Then the
                                    values from the controller goes into a control register which makes sure that they are outputted in synchronous manner by
                                    utilizing positive edge triggered D-FF(flip flops) that are all connected to the same clock."""
        },
        {
            "date": "2024",
            "title": "Rentify", 
            "description": """Worked in a team to develop an Android app.
                            • The goal of the app is to connect people who want to rent out their belongings with people who are looking to rent. The app
                                supports item listing, searching, and renting, creating an easy-to-use service for both parties.
                            • The app uses SQL as the backend to facilitate the interactions between the renters and lessor accounts.
                            • I had a flexible role during this project where I mainly worked on the front end of the app where I made sure to make a
                                UI/UX experience that would be easy to understand and follow. I also worked on backend fixes as needed for the app, for
                                example debugging/fixing SQL queries as needed.
                            • Also did QA (Quality assurance) testing of the app to ensure high quality of the code."""
        },
        {
            "date": "2024",
            "title": "MindScribeAI (Hack the Hill II)", 
            "description": """• Developed an AI-powered journaling app using Flask for the backend and React for the frontend.
                                • The application has a feature that allows the user to generate monthly reports based on their previously written journals, this
                                    functionality was achieved by using Gemini 1.5 Flash as it is quick to respond to / generate text.
                                • Gemini was also used as a chatbot in the app but was prompt engineered so that it would talk like a therapist.
                                • I primarily worked on the backend, creating APIs for the frontend to access the SQLite database for storing and retrieving
                                    journals as well as authenticating users."""
        },
        {
            "date": "2024",
            "title": "Python Projects", 
            "description": """Gotta have that pythonic journey to start • Learned how to perform web scraping while adhering to the robots.txt
                                • Developed a GUI pomodoro timer. (check day 28 in my 100 days of code github repo)
                                • Developed a GUI quiz app that used APIs to get random False questions from Open Trivia DB. (check day 34 in my 100
                                    days of code github repo)
                                • Developed a GUI flashcard app that aims to aid in learning French by parsing French and English from a JSON file.
                                • Developed and worked with REST APIs.
                                • Developed my personal website using Reflex."""
        },
        {
            "date": "2023",
            "title": "Object Detection With Raspberry PI ", 
            "description": """• Used publicly available TensorFlow models to perform object detection.
                                • The project added the additional functionality of using a tkinter GUI to make a window prompting the user to engage in a
                                    search of the detected object, upon clicking a button in the window, the user is sent straight to the shopping section of
                                    google, with the query being the object type. Side Note: The naive highschooler wanted to do lip reading with AI on a raspberry pi but turns out that 
                                    requires cuda cores and unfortunatley the pi has 0 of those."""
        },
        {
            "date": "2023",
            "title": "RustyOS", 
            "description": """A naive high schooler wants to make his own operating system how bad can it be?• Developed a minimal operating system as a side project.
                                • Enabled RustyOS to print text onto a screen.
                                • Implemented Memory, simple clock-based scheduler and a few exceptional handlers in the system.
                                • Enabled it to be booted onto bare metal."""
        },
        {
            "date": "2023",
            "title": "Smart Dustbin Project", 
            "description": """A naive highschooler discovers that projects do always fail during live demos even after intensive testing. This was a team based project. This was my second big scale hardware project that I had make using Arduino.
            Having gone through the bad experience of live demo failing in the traffic light project. The naive highschooler goes on to test the dustbin 50 times at home and fixing any kinks that happen and said dustbin works perfectly,
            being proud of his accomplishments he does a video call with his teammates to show them the final result and even they are impressed, comes the day of the live demo and the dustbin fails.
            I did all of the coding, which was mainly detecting if a hand is near the proximity sensor and then to keep the lid open otherwise close it after a few seconds, and most of the wiring in the project. 
            Yes I boasted about multithreading in this project too even though it really wasn't.
            Unfortunately the video of the project has also been lost to time (curse you school board for taking away the account and curse you google takeout for NOT giving me all my data back)"""
        },
        {
            "date": "2022",
            "title": "Traffic Lights Project", 
            "description": """A naive highschooler discovers that projects do always fail during live demos. This was my first big scale hardware project that I had make using Arduino. 
            This was a team based project.
            I did all of the coding, which was mainly synchronising the leds, and most of the wiring in the project. I still remember back then thinking that multithreading was as easy as
            copy pasting function calls in random spots in a while loop, and then boasting about how I made a "multithreaded" application even though arduino apparently only supports single threaded things.
            Unfortunately the video of the project has been lost to time (curse you school board for taking away the account and curse you google takeout for NOT giving me all my data back)"""
        },
        {
            "date": "2021",
            "title": "Game Development Projects", 
            "description": """\n There is a naive highschooler and he wants to become a gamedeveloper because gaming is fun! • Worked in a team for both video games, where I worked on Dogscape first and then worked on Chaotigator later on.
                            • Team lead for both projects.
                            • Made sure that the team was able to work at its peak at all times.
                            • Gave motivation to teammates whenever they felt burnt out.
                            • Managed the full code base and took care of any merge conflicts during both projects.
                            • Did QA (Quality assurance) testing throughout the development of the games. Dogscape:
                            • Developed a 2D platformer where the main character is a dog that has to fight cats to reach the end of each level. Fostered
                                teamwork and collaboration among project members.
                            Chaotigator:
                            • Developed an infinitely generating platformer game where the main character is an alligator which has to survive disasters
                                happening on the map."""
        }
    ]