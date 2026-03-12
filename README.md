

## 1 Problem Statement
Libraries often face difficulty in managing book records manually. Tracking which books are available, issued, or returned can become time-consuming and prone to errors when handled without a proper system.

This project aims to develop a simple Python-based Library Management System that helps manage library operations efficiently. The system allows users to add new books, issue books, return books, and view the list of available books, making basic library management easier and more organized.


##  Features
- Add new books to the library
- Return issued books
- Interactive menu-driven interface via Command-Line Interface (CLI)
- Modular project structure (separate files for each functionality)
- Clean and easy-to-maintain codebase

##  Technologies / Tools Used
- *Python 3*
- Modular programming (multiple Python files)
- Command-line interface


## Installation

- Clone the repository:
  git clone <https://github.com/tanviag2601/library-management-system.git>

- Navigate to the project directory:
  cd library-Management-System

- Ensure Python is installed (version 3.x recommended).


## Usage

- Run the main program:
  python main.py

- Follow on-screen prompts to:
  - Add books
  - Issue books
  - Return books
  - View all books

## Example
Library Menu:
    Enter 1 to view all the books
    Enter 2 to add a new book
    Enter 3 to return a book
    Enter 4 to issue a book
    Enter 5 to exit the program
    Enter your choice as stated above: 2
    Enter name of the new book: Python Programming
    New Book Added!


##  Target Users
- Students searching for books in a library  
- Librarians managing book records  


## Project Structure

Library-Management-System/
│
├── MAIN.py             # Main program
├── ADD.py              # Adds new book
├── ISSUE.py            # Issues book
├── LIB_MANAGE.py       # manages the constructor
├── RETURN.py           # Returns the book 
└── README.md           # This file  


## Future Improvements

- Add a GUI for better user experience.
- Implement search functionality by author or book title.
- Track fines for late returns.
- Store data in a database instead of text files for scalability