PROJECTS = [
    {
        "date": "2025",
        "title": "Real-Time Route Optimization System (🥇 1st Place, Programming Competition)",
        "description": """Developed a competition-winning route optimization system that solves the Vehicle Routing Problem with Time Windows (VRPTW) under strict performance constraints, achieving 1st place in a performance-based programming challenge.

**Challenge Requirements:**
* Optimize delivery routes for 100+ nodes with dynamic traffic conditions and strict time window constraints
* Execute complete optimization in under 5 seconds
* No external routing APIs (Google Maps, OpenRouteService, etc.)
* Handle real-time traffic adaptation with speed factors and congestion delays
* Output: Optimal delivery sequence with expected arrival times

**Algorithm Architecture & Implementation:**

* **Hybrid Optimization Strategy:**
    * Designed adaptive algorithm selection based on problem size:
        * Small instances (≤30 nodes): Nearest Neighbor + Clarke-Wright Savings comparison
        * Medium instances (31-60 nodes): Clarke-Wright Savings Algorithm
        * Large instances (61-100 nodes): Fast Nearest Neighbor with urgency scoring
    * Implemented custom urgency-based scoring balancing distance and time window slack
    * Built automatic route repair mechanism for edge cases and missing nodes

* **Performance Engineering:**
    * Precomputed symmetric distance matrices for O(1) lookup performance
    * Developed limited 2-opt local search refinement with adaptive iteration control
    * Hash-based traffic condition lookup for real-time travel time calculations
    * Time-budget aware optimization (4.8s limit for refinement phase)

* **Core Algorithms Implemented:**
    * Clarke-Wright Savings Algorithm with feasibility validation at each merge
    * Fast Nearest Neighbor with lookahead and greedy construction
    * Adaptive 2-opt refinement with gap-limited neighbor evaluation (15-30 nodes)
    * Custom time window constraint satisfaction solver

* **Data Processing & Validation:**
    * JSON-based input/output pipeline for delivery points and traffic data
    * Real-time feasibility validation with time window constraint checking
    * Comprehensive result analytics including slack analysis and violation detection
    * Automatic missing node detection and insertion

**Results:**
* ✅ Consistently sub-5 second execution (avg 4.8s for 100 nodes)
* ✅ Zero time window violations on feasible routes
* ✅ 100% node coverage across all test cases
* ✅ 1st Place in Programming Competition

**Key Technical Insights:**
* Demonstrated that effective optimization requires smart engineering decisions about when to deploy specific algorithms, not just algorithmic knowledge
* Balanced solution quality with computational efficiency under strict time constraints
* Successfully adapted routing strategies based on problem characteristics

**Tech Stack:** Python, Algorithm Design (Clarke-Wright, 2-Opt, Nearest Neighbor), Data Structures, JSON Processing, Performance Optimization, Computational Geometry

**Applications:** Last-mile delivery optimization, food delivery routing, service technician scheduling, courier dispatch systems

This project showcases practical application of combinatorial optimization to real-world logistics challenges, emphasizing the balance between solution quality and computational efficiency constraints.
""",
    },
    {
        "date": "Oct 2025",
        "title": "Quotify - Quantum Music Generator (🥉 3rd Place, IBM Qiskit Fall Fest 2025)",
        "description": """
* Developed Quotify, a quantum computing music generation system that won 3rd place at IBM Qiskit Fall Fest 2025 at the University of Ottawa.
* Designed and implemented a QuantumMusicGenerator class using Python and the Qiskit library to translate quantum algorithm outputs into musical compositions.
* Integrated multiple quantum algorithms as unique "instruments" in a digital orchestra:
    * Quantum Fourier Transform for harmonic progressions
    * Grover's Algorithm to amplify and accent specific notes
    * Quantum Walks to generate evolving melodic lines
    * Entangled Bell States to produce correlated duets
* Built a real-time audio-visual performance system using Pygame, streaming quantum data for synchronized music and visual effects.
* Developed custom firmware to control an LED light show synchronized with the quantum-generated music.
* Demonstrated practical applications of quantum computing beyond traditional computational problems, exploring the intersection of quantum mechanics and creative expression.
        """,
    },
    {
        "date": "2025",
        "title": "Code With Me",
        "description": """A full-stack, real-time collaborative coding platform designed to solve a critical problem for new developers: the frustration of getting stuck alone. Our mission was to democratize mentorship and transform the learning experience from a solitary struggle into a shared journey.

Secured **2nd Place** in the 'Code for Empowerment' challenge. The browser-based application instantly connects learners with peers and mentors for live, over-the-shoulder debugging and pair programming sessions, featuring a shared editor and integrated code execution—no downloads required.

**Technical Highlights & Problem-Solving:**

*   **Real-Time Collaborative Editor:** Developed a seamless, real-time collaborative code editor using **Yjs (CRDTs)** to ensure conflict-free, low-latency document synchronization between multiple users. This was the core challenge and a major technical achievement.
*   **Robust Real-Time Backend:** Architected a backend with **Node.js and WebSockets** to maintain persistent, real-time connections essential for live collaboration and state management.
*   **Secure Code Execution:** Integrated the **Piston API** to provide secure, sandboxed code execution, allowing users to instantly run and test code snippets from various languages directly within the platform.
*   **First-Principles Algorithm Design:** Before settling on a final library, we designed a **synchronization algorithm from first principles** using a pub/sub model to deconflict concurrent edits. This exercise demonstrated a deep understanding of the core distributed systems challenges involved in real-time collaboration.
*   **Modern Frontend:** Built a fast and responsive user interface with **Vite, React, and TypeScript**, ensuring a modern, type-safe, and intuitive experience for beginners.

This project successfully mimics an in-person debugging session, creating an accessible and powerful tool that breaks down barriers to coding education.

**Tech Stack:** React, TypeScript, Vite, Node.js, WebSockets, Yjs (CRDTs), Piston API

**[View on GitHub](https://github.com/oZep/cwm)**
""",
    },
    {
        "date": "2025",
        "title": "uOCTF",
        "description": """Our team achieved **1st place** 🥇 in the uOCTF 2025 Capture the Flag (CTF) competition, organized by the uOttawa Cybersecurity Club. This intense 3-hour event presented 30 challenges spanning Web Exploitation, Forensics, Hardware Security, and Cryptography.

We successfully solved 28 out of 30 challenges, demonstrating a strong grasp of diverse cybersecurity concepts and techniques. As a participant relatively new to CTFs, I found this experience incredibly rewarding, validating my self-taught knowledge from independent study.

**Key Learnings and Achievements:**

* Rapid Problem Solving: Navigating and solving complex security challenges under strict time constraints.
* Diverse Skill Application: Applying knowledge across various domains, including:
    * Cryptography: Successfully decrypting and analyzing encoded data.
    * Forensics: Recovering hidden information from digital artifacts.
    * Web Exploitation: Identifying and exploiting vulnerabilities in web applications.
    * Hardware: Understanding and working with hardware related security issues.
* Technical Discoveries:
    * Learned advanced techniques for hiding files within ZIP archives, bypassing standard extraction methods.
    * Gained practical experience in mounting and analyzing virtual flash drive file systems.
* Team Collaboration: Leveraging teamwork and shared expertise to efficiently tackle challenges.
""",
    },
    {
        "date": "2025",
        "title": "QNX FIGHTER (cuHacking 6)",
        "description": """* Ported a fighting game to multiple platforms:
    * Attempted porting Pygame to QNX.
    * Developed a Raylib version of the game.
    * Developed an NCurses version of the game.
    
Achievements:

* First Place in QNX’s "Best use of QNX - Hardware" challenge at cuHacking 6 (600+ hackers participating).

Project available here: [https://devpost.com/software/qnx-fighter](https://devpost.com/software/qnx-fighter)""",
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

Side Note: The naive highschooler would have been proud to know that the live demo did not fail.""",
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
    * Replicated the above data analysis using R and its respective libraries.""",
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
    * Control register ensures synchronous output using positive edge-triggered D-FF (flip-flops) connected to a common clock.""",
    },
    {
        "date": "2024",
        "title": "Rentify",
        "description": """* The goal of the app is to connect people who want to rent out their belongings with people who are looking to rent. The app supports item listing, searching, and renting, creating an easy-to-use service for both parties.
* The app uses SQL as the backend to facilitate the interactions between the renters and lessor accounts.
* I had a flexible role during this project where I mainly worked on the front end of the app where I made sure to make a UI/UX experience that would be easy to understand and follow. I also worked on backend fixes as needed for the app, for example debugging/fixing SQL queries as needed.
* Also did QA (Quality assurance) testing of the app to ensure high quality of the code.""",
    },
    {
        "date": "2024",
        "title": "MindScribeAI (Hack the Hill II)",
        "description": """* Developed an AI-powered journaling app using Flask (backend) and React (frontend).
* Implemented a feature to generate monthly reports from user journals, utilizing Gemini 1.5 Flash for rapid text generation.
* Integrated Gemini as a chatbot, prompt-engineered to simulate a therapist.
* Primarily focused on backend development:
    * Created APIs for frontend access to the SQLite database (journal storage and retrieval).
    * Implemented user authentication.

Project available here: [https://devpost.com/software/mindscribeai](https://devpost.com/software/mindscribeai)
""",
    },
    {
        "date": "2024",
        "title": "Regent",
        "description": """Apple shortcuts that help to extend Monarch Launcher's functionality.
* A regent is a person who rules a country for a limited period, because the king or queen (Basically a monarch) is absent or too young, too ill, etc. (Made these when Monarch Launcher Version < 0.6 basically beta)
* Yeah so I started my customize MacOS arc.
* Started using Monarch after going through using Spotlight and Raycast.
* Saw the cool functionality that Superlinks and Apple shortcuts can add to my workflow.
* Open sourced all the small scripts (Apple Shortcuts) I use with Monarch.
* Learned a lot about Applescript and Shell scripting.

Project available here: [https://github.com/UnknownCrafts/Regent](https://github.com/UnknownCrafts/Regent)
""",
    },
    {
        "date": "2024",
        "title": "DockDoor",
        "description": """Contributed to an open source project called DockDoor.
* Added a small feature to the swift app.
* Made it so that when the DockDoor minimized app preview is clicked, it opens and focuses on the minimized app.
* It was fun giving back to the devs especially since I use their app everyday.

PR can be found here: [https://github.com/ejbills/DockDoor/pull/118](https://github.com/ejbills/DockDoor/pull/118)
""",
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
* Developed my personal website using Reflex.
* And many other apps, websites, games, and scripts!

Projects available here: [https://github.com/UnknownCrafts/100-days-of-code-python-](https://github.com/UnknownCrafts/100-days-of-code-python-)
""",
    },
    {
        "date": "2024",
        "title": "NoPDFPass",
        "description": """A simple app to remove the password restriction from PDFs.
* This is not a PDF password cracking app.
* This an app that is supposed to output PDF files that don't have a password on them. (you are still supposed to give it the passwords)
* This was the first time I learned to compile a python script into a desktop application.
* The app is a simple tkinter based GUI and uses a PDF parsing library to do its operations.
* Learned how to compile for M series Macs so that the app can be installed without paying for the developer license.

Project available here: [https://github.com/UnknownCrafts/NoPDFPass](https://github.com/UnknownCrafts/NoPDFPass)
""",
    },
    {
        "date": "2023",
        "title": "Object Detection With Raspberry PI ",
        "description": """* Used publicly available TensorFlow models to perform object detection.
* The project added a tkinter GUI:
    * Upon detecting an object, a window prompts the user to search for it.
    * Clicking a button sends the user to Google Shopping with the object type as the search query.

Project available here: [https://github.com/UnknownCrafts/Raspberry-Pi-Object-Detection-With-Search-Functionality](https://github.com/UnknownCrafts/Raspberry-Pi-Object-Detection-With-Search-Functionality)

**Side Note:**

* The naive highschooler attempted lip reading with AI on a Raspberry Pi.
* Discovered that lip reading with AI requires CUDA cores, which the Raspberry Pi lacks.
    
""",
    },
    {
        "date": "2023",
        "title": "RustyOS",
        "description": """A naive high schooler wants to make his own operating system. How bad can it be?

* Developed a minimal operating system as a side project.
* Enabled RustyOS to print text onto a screen.
* Implemented memory management, a simple clock-based scheduler, and a few exception handlers.
* Enabled the OS to boot onto bare metal.""",
    },
    {
        "date": "2022",
        "title": "Porting Minecraft Mods",
        "description": """Small minecraft programming arc, I mean that was the whole reason I got allowance to buy Minecraft Java edition anyways. (I totally wouldn't have it for any other reason)
* I wanted to make a Minecraft modpack, quickly found out that it is really hard to make modpacks.
* Ported 1.18 versions Musica, Visuality, and Effective mods to 1.17.1 because thats the version I was aiming to make the modpack for.
* Quickly realized how confusing the modding documentation is for minecraft, I was making a fabric modpack.
* The modpack wasn't optimized for size at all, I was able to find modpacks with way more mods that were like half the size. So there was some optimization issue for sure.
* Also opened pull requests for the backport for Musica and Visuality, so that I could give back to the community. (The Visuality PR got approved! I think this was my first public PR getting approved)
* This was also the first time I touched java.
""",
    },
    {
        "date": "2022",
        "title": "Smart Dustbin Project",
        "description": """A naive highschooler learned a painful truth: even after *intensive* testing, live demos are destined to fail.

This was my second large-scale Arduino hardware project, a team effort.

* Worked on the wiring of the circuit. (Ultrasonic sensor with arduino)
* Having experienced the traffic light project's live demo failure, I rigorously tested the dustbin more than 50 times at home, fixing every issue that arose.
* The dustbin performed flawlessly during home tests, impressing even my teammates during a video call showcasing the final result.
* However, during the official live demo, the dustbin malfunctioned.
* I was responsible for all the coding, primarily detecting hand proximity via a sensor and controlling the lid's opening and closing.
* Yes, I again mistakenly boasted about "multithreading" despite it not being implemented correctly.
* I found the video for this project!!!

Project video here: [https://youtu.be/_KtPxIFETkk?si=-kiICwF3TsCzIW0w](https://youtu.be/_KtPxIFETkk?si=-kiICwF3TsCzIW0w) (Skip to 3:48 if you wanna see the dustbin in action)
""",
    },
    {
        "date": "2022",
        "title": "Traffic Lights Project",
        "description": """A naive highschooler learned a valuable lesson: projects *always* fail during live demos.

This was my first large-scale hardware project using Arduino, a team-based effort.

* Worked on the wiring of the circuit. (Multiple LEDs with arduino)
* I handled all the coding, primarily synchronizing LEDs, and most of the project's wiring.
* I mistakenly believed multithreading was achieved by randomly pasting function calls within a `while` loop, and proudly claimed to have created a "multithreaded" application, despite Arduino's single-threaded nature.
* Unfortunately, the project's video was lost:
    * Blame the school board for account termination.
    * Blame Google Takeout for incomplete data retrieval.""",
    },
    {
        "date": "2022",
        "title": "Vaccinator (STEM Hacks)",
        "description": """* Awarded 2nd place in a Covid-19 themed hackathon for the development of a 2D survival game using Unity. This project emphasized rapid prototyping, teamwork, and effective collaboration. Key contributions and achievements included:

* Developed core gameplay mechanics and implemented them using Unity's C# scripting.
* Designed and integrated 2D assets to create an engaging and thematic game environment.
* Effectively collaborated with team members to manage tasks and achieve project milestones within the tight hackathon deadline.
* Delivered a functional and engaging game that resonated with the judges, resulting in a 2nd place award.

This experience significantly enhanced my ability to work under pressure, apply Unity development skills, and contribute to a successful team project.

Project available here: [https://unknowncrafts.itch.io/vaccinator](https://unknowncrafts.itch.io/vaccinator)

Source code available here: [https://github.com/UnknownCrafts/Stem_HackathonVaccinator](https://github.com/UnknownCrafts/Stem_HackathonVaccinator)
""",
    },
    {
        "date": "2022",
        "title": "BetterMacMod",
        "description": """This was a personal project where I wanted to make a rainmeter like app for MacOS using Python.
* Learned about creating objects during runtime.
* Learned about why having code seperated in different files is important. (It was a pain to debug the code because everything was in one python file)
* Learned a bit about the lambda function.
* Later realized (after like 3 years) that making the app single threaded was one of the reasons my widgets didnt get updated all at once lol.
* Learned about bash commands and shell scripting through python.

Project video here: [https://www.youtube.com/watch?v=lgmoddUyE5Q](https://www.youtube.com/watch?v=lgmoddUyE5Q)
""",
    },
    {
        "date": "2021",
        "title": "Project Equinox (WolfHacks21)",
        "description": """Introducing to the residents of earth the first ever self sustaining habitable building that will make colonization on Plant Howler possible.

* Worked on designing the website for the hackathon.
* Learned a lot about frontend designing, UI/UX, and embedding things into a webpage.

Link for the website: [https://aryapatel987.github.io/Equinox/](https://aryapatel987.github.io/Equinox/)

Project available here: [https://devpost.com/software/welcome-to-project-equinox](https://devpost.com/software/welcome-to-project-equinox)

Github Link: [https://github.com/AryaPatel987/project-](https://github.com/AryaPatel987/project-)
""",
    },
    {
        "date": "2021",
        "title": "Carelton Design Studio Projects",
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

* Developed an infinitely generating platformer game where the main character is an alligator that survives disasters.

Both projects available here: [https://carleton.ca/vv/clubprojects/](https://carleton.ca/vv/clubprojects/)
""",
    },
    {
        "date": "2020",
        "title": "Lonely Survivor (Weekly Game Jam - Week 149)",
        "description": """My first ever gamejam!
* This was around when I started developing games on unity again (after 2017).
* The game is so unoptimized that it might as well be used as a cpu stress test.
* This hackathon pushed me to learn more about game development and Unity so that I could make better games.

Both projects available here: [https://unknowncrafts.itch.io/lonely-survivor](https://unknowncrafts.itch.io/lonely-survivor)
""",
    },
    {
        "date": "2017",
        "title": "The uh bricking incident",
        "description": """I bricked my mom's HTC M8 by trying to update SU using busybox. (So I guess technically it wasn't my fault)
* I had never done rooting before, but my cousin had rooted my phone before so that I could hack mobile games.
* Learned a lot about the rooting process, bootloaders etc.
* Learned a lot about android ROMs and flashing operating systems in general.
* I tried to do file recovery and maybe I could have been able to do file recovery if I had more knowledge. (A 12 year old can only do so much)
* Learning how to flash new operating systems onto older devices ignited a sustainability aspect in my mind.
* Sorry mom.
""",
    },
    {
        "date": "2017",
        "title": "Marble Rolling game",
        "description": """This was my first ever Unity project.
* This was where I followed a youtube video on how to make a marble rolling game.
* I was inspired by my cousin's astronaut game that he made in Unity.
* The game is lost to a computer virus and also the fact that Unity dropped 32 bit OS support during that time.

I think I followed this tutorial series: [https://www.youtube.com/watch?v=zlnJP0vloDg&list=PL-ptF2slHtJAYSWWJ8aqbf1a5tu9u7pAb](https://www.youtube.com/watch?v=zlnJP0vloDg&list=PL-ptF2slHtJAYSWWJ8aqbf1a5tu9u7pAb)
""",
    },
]
