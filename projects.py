PROJECTS = [
        {
            "date": "2025",
            "title": "QNX FIGHTER (cuHacking 6)", 
            "description": """* Ported a fighting game to multiple platforms:
    * Attempted porting Pygame to QNX.
    * Developed a Raylib version of the game.
    * Developed an NCurses version of the game.
    
Achievements:

* First Place in QNX’s "Best use of QNX - Hardware" challenge at cuHacking 6 (600+ hackers participating).

Project available here: [https://devpost.com/software/qnx-fighter](https://devpost.com/software/qnx-fighter)"""
        },
        {
            "date": "2025",
            "title": "Sweatris (uOttaHack 7)",
            "description": """Sweatris: A Fitness-Themed Interactive Tetris Game

* A web-based application combining physical activity and gaming.
* Provides a fun and engaging workout experience.
* Uses object detection and an intelligent algorithm for move recommendations.
* Turns user movements into Tetris game controls.

Achievements:

* First Place in NAV CANADA’s challenge at uOttaHack 7 (800+ hackers participating).
* Third Place in uOttaHack 7 General Category.

Project available here: [https://github.com/bravesirrobin358/Sweatris](https://github.com/bravesirrobin358/Sweatris)

Side Note: The naive highschooler would have been proud to know that the live demo did not fail."""
        },
        {
            "date": "2024-Present",
            "title": "Data Science Sounds Fun", 
            "description": """Alright, winter break! Time to turn boredom into learning. Here's what I did:

* **Data Wrangling:**
    * Cleaned and encoded categorical data using Scikit-Learn, Pandas, and NumPy.
* **Data Splitting:**
    * Parsed CSV data into a Pandas DataFrame.
    * Separated data into independent variables (X) and dependent variables (y).
    * Split X and y into training (X\_train, y\_train) and testing (X\_test, y\_test) sets using Scikit-Learn, with an 80:20 train-test ratio.
        * (Adjusted ratio depending on dataset size).
* **Regression Modeling (Salary Prediction):**
    * Trained various regression models using Scikit-Learn:
        * Simple/Multiple Linear Regression
        * Polynomial Regression
        * Support Vector Regression
        * Decision Tree Regression
        * Random Forest Regression
    * Predicted salaries based on previous job positions.
* **Classification Modeling (Car Purchase Prediction):**
    * Trained classification models using Scikit-Learn:
        * Logistic Regression
        * K-Nearest Neighbors
    * Classified whether a person would purchase a car based on age and salary.
* **Data Visualization:**
    * Plotted test and training data against predicted/actual values using Plotly and Matplotlib.
* **R Implementation:**
    * Replicated the above data analysis using R and its respective libraries."""
        },
        {
            "date": "2024",
            "title": "A Basic Computer", 
            "description": """* Used an FPGA for this project.
* Developed the ALU (Arithmetic Logic Unit) of a basic computer:
    * Implemented simple arithmetic operations: addition, subtraction, multiplication by 2.
    * Implemented logical operations: AND.
* Developed a controller for the basic computer:
    * Capable of detecting set flags within the computer.
    * Example: When the CMA (Complement Accumulator) assembly instruction is called:
        * The controller checks the current instruction cycle.
        * The controller checks the first few bits of the instruction register.
    * Controller outputs are sent to a control register.
    * Control register ensures synchronous output using positive edge-triggered D-FF (flip-flops) connected to a common clock."""
        },
        {
            "date": "2024",
            "title": "Rentify", 
            "description": """* Developed an AI-powered journaling app using Flask (backend) and React (frontend).
* Implemented a feature to generate monthly reports from user journals, utilizing Gemini 1.5 Flash for rapid text generation.
* Integrated Gemini as a chatbot, prompt-engineered to simulate a therapist.
* Primarily focused on backend development:
    * Created APIs for frontend access to the SQLite database (journal storage and retrieval).
    * Implemented user authentication."""
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
            "description": """Gotta have that Pythonic journey to start!

* Learned how to perform web scraping while adhering to `robots.txt`.
* Developed a GUI pomodoro timer. (See day 28 of my 100 Days of Code GitHub repo.)
* Developed a GUI quiz app that uses APIs to fetch random True/False questions from Open Trivia DB. (See day 34 of my 100 Days of Code GitHub repo.)
* Developed a GUI flashcard app for learning French, parsing French and English from a JSON file.
* Developed and worked with REST APIs.
* Developed my personal website using Reflex."""
        },
        {
            "date": "2023",
            "title": "Object Detection With Raspberry PI ", 
            "description": """* Used publicly available TensorFlow models to perform object detection.
* The project added a tkinter GUI:
    * Upon detecting an object, a window prompts the user to search for it.
    * Clicking a button sends the user to Google Shopping with the object type as the search query.

**Side Note:**

* The naive highschooler attempted lip reading with AI on a Raspberry Pi.
* Discovered that lip reading with AI requires CUDA cores, which the Raspberry Pi lacks."""
        },
        {
            "date": "2023",
            "title": "RustyOS", 
            "description": """A naive high schooler wants to make his own operating system. How bad can it be?

* Developed a minimal operating system as a side project.
* Enabled RustyOS to print text onto a screen.
* Implemented memory management, a simple clock-based scheduler, and a few exception handlers.
* Enabled the OS to boot onto bare metal."""
        },
        {
            "date": "2023",
            "title": "Smart Dustbin Project", 
            "description": """A naive highschooler learned a painful truth: even after *intensive* testing, live demos are destined to fail.

This was my second large-scale Arduino hardware project, a team effort.

* Having experienced the traffic light project's live demo failure, I rigorously tested the dustbin 50 times at home, fixing every issue that arose.
* The dustbin performed flawlessly during home tests, impressing even my teammates during a video call showcasing the final result.
* However, during the official live demo, the dustbin malfunctioned.
* I was responsible for all the coding, primarily detecting hand proximity via a sensor and controlling the lid's opening and closing.
* Yes, I again mistakenly boasted about "multithreading" despite it not being implemented correctly.
* Unfortunately, the project's video was also lost:
    * Blame the school board for account termination.
    * Blame Google Takeout for incomplete data retrieval."""
        },
        {
            "date": "2022",
            "title": "Traffic Lights Project", 
            "description": """A naive highschooler learned a valuable lesson: projects *always* fail during live demos.

This was my first large-scale hardware project using Arduino, a team-based effort.

* I handled all the coding, primarily synchronizing LEDs, and most of the project's wiring.
* I mistakenly believed multithreading was achieved by randomly pasting function calls within a `while` loop, and proudly claimed to have created a "multithreaded" application, despite Arduino's single-threaded nature.
* Unfortunately, the project's video was lost:
    * Blame the school board for account termination.
    * Blame Google Takeout for incomplete data retrieval."""
        },
        {
            "date": "2021",
            "title": "Game Development Projects", 
            "description": """A naive highschooler wants to become a gamedeveloper because gaming is fun!

* Worked in a team for two video games:
    * Dogscape (first project)
    * Chaotigator (later project)
* Team lead for both projects.
* Ensured the team worked at its peak at all times.
* Motivated teammates when they felt burnt out.
* Managed the full code base and resolved merge conflicts for both projects.
* Performed QA (Quality Assurance) testing throughout the development of both games.

**Dogscape:**

* Developed a 2D platformer where the main character is a dog that fights cats to reach the end of each level.
* Fostered teamwork and collaboration among project members.

**Chaotigator:**

* Developed an infinitely generating platformer game where the main character is an alligator that survives disasters."""
        },
    ]