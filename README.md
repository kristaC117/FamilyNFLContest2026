# FamilyNFLContest2026 - In Progress...

🏈 Family NFL Pick’em Contest

A Python desktop application for managing a family NFL pick’em contest, tracking player selections, and organizing game data using SQLite.

This project is part of my hands-on journey into Python development. I'm building it to strengthen my understanding of application architecture, database integration, object-oriented programming, and user interface development while applying the software engineering concepts I've used in C# and VB.NET.

🚀 Project Overview

The Family NFL Pick’em Contest application is designed to provide a simple desktop interface for managing NFL game picks and player scoring. The application uses Python for its logic, Tkinter for its graphical user interface, and SQLite for local data storage.

Rather than putting everything into one large script, I've organized the project into separate layers for database operations, data models, business logic, and the user interface.

My goal is to build an application that is easy to maintain, understand, and expand as new features are added.

✨ Features

Desktop user interface: Built with Python's Tkinter library.

SQLite database: Stores contest-related data locally.

Player management: Organizes player information and scores.

Game data management: Separates NFL game data from application logic.

Pick management: Provides a foundation for creating and managing player selections.

Scoring logic: Uses a dedicated service to handle scoring functionality.

Modular architecture: Separates database access, models, services, and UI components.

Ongoing development: Designed to grow as I add functionality and refine the application.

🛠️ Technology Stack

Technology

Purpose

Python

Application logic and functionality

Tkinter

Desktop graphical user interface

SQLite

Local relational database

SQL

Data storage and database operations

Git

Version control and change tracking

GitHub

Remote repository and project history

Visual Studio

Development environment

🏗️ Project Structure

FamilyNFLContest2026/
│
├── database/
│   ├── connection.py
│   ├── games_db.py
│   ├── picks_db.py
│   ├── players_db.py
│   └── setup_db.py
│
├── models/
│   ├── game.py
│   ├── picks.py
│   └── player.py
│
├── services/
│   ├── picks_services.py
│   ├── player_services.py
│   ├── scoring_service.py
│   └── setup_services.py
│
├── UI/
│   └── contest_UI.py
│
├── main.py
├── .gitignore
└── FamilyNFLContest2026.pyproj

Architecture and Design

The application is organized by responsibility so that database operations, business rules, data models, and presentation logic can be developed and maintained separately.

database/ — Handles database connections, table setup, and data access operations.

models/ — Represents the application's core data entities, including players, games, and picks.

services/ — Contains application services for player operations, pick management, scoring, and setup.

UI/ — Contains the Tkinter interface and user interactions.

main.py — Serves as the application entry point.

This structure helps reduce unnecessary coupling between components and makes the application easier to extend and troubleshoot.

⚙️ Getting Started

Prerequisites

Python 3

A Python environment with Tkinter available

Git, if you want to clone the repository

SQLite is included with most standard Python installations, so a separate database server is not required.

Installation

1. Clone the repository

git clone https://github.com/kristaC117/FamilyNFLContest2026.git

2. Navigate to the project directory

cd FamilyNFLContest2026

3. Run the application

python main.py

Depending on your Python installation, you may need to use python3 main.py instead.

Note: This project is actively being developed. Database initialization and local configuration may need to be completed before the application runs successfully in a fresh environment.

🧠 What I'm Learning

This project gives me an opportunity to deepen my Python skills while applying my existing software development experience.

Areas of focus include:

Translating familiar C# and VB.NET programming patterns into Python.

Separating database operations from business logic and the UI.

Designing and working with relational database tables.

Managing application state and user selections.

Building reusable services and data models.

Debugging, testing, and refining application behavior.

Using Git and GitHub to track changes and maintain project history.

🔭 Future Enhancements

Planned improvements as development continues include:

Completing and refining the player pick-selection workflow.

Loading saved picks from SQLite when the interface opens.

Improving selection-state handling and validation.

Expanding game scoring and contest standings.

Adding more robust error handling and data validation.

Improving the user interface and overall user experience.

Adding automated tests for database operations and business logic.

👩‍💻 About the Developer

I'm a software development professional with a Bachelor of Science in Computer Science and experience building, maintaining, troubleshooting, and improving business applications using C#/.NET, VB.NET, and SQL.

I'm currently expanding my Python skills through hands-on projects, focusing on clean architecture, practical problem-solving, and building applications that solve real problems.

I believe the best way to learn a technology is to build something with it, work through the problems, and keep improving the solution.

This project represents that approach: learn by building, solve problems methodically, and keep getting better.

Built with Python, curiosity, and a love of football. 🏈
