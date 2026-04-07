---
title: "Code With Me"
date: "2025"
featured: "true"
order: 3
---
A full-stack, real-time collaborative coding platform designed to solve a critical problem for new developers: the frustration of getting stuck alone. Our mission was to democratize mentorship and transform the learning experience from a solitary struggle into a shared journey.

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