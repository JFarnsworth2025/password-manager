# 🔐 Password Manager

A beginner-friendly command-line password manager built with Python.

This project allows users to store, load, search, and delete website credentials using a local JSON file. It was built as part of my Python automation learning journey to practice working with files, JSON, functions, and user input.

## Features

- Add new passwords
- Load saved passwords
- Search passwords by website
- Delete saved passwords
- Automatically creates the data folder and password file
- Persists password data locally using JSON

## Technologies Used

- Python 3
- pathlib
- json

## Project Structure

```text
password-manager/
├── data/
│   └── passwords.json
├── main.py
├── password_manager.py
├── README.md
└── .gitignore
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/YourUsername/password-manager.git
```

2. Navigate to the project folder.

```bash
cd password-manager
```

3. Run the application.

```bash
python main.py
```

## What I Learned

Through this project I practiced:

- Creating and calling functions
- Organizing code across multiple Python files
- Reading and writing JSON files
- Using `pathlib` for file management
- Working with lists and dictionaries
- Searching through collections
- Validating user input
- Building a command-line application

## Skills Demonstrated

- File handling
- JSON serialization and deserialization
- Modular program design
- Command-line interface development
- Data validation
- Search algorithms
- CRUD operations (Create, Read, Update, Delete)

## Future Improvements

- Hide passwords during input using `getpass`
- Encrypt stored passwords instead of plain JSON
- Generate secure random passwords
- Confirm before permanently deleting a password
- Edit existing password entries
- Prevent duplicate website/username combinations
- Copy passwords directly to the clipboard
- Display password strength when creating passwords
- Organize passwords into categories or folders
- Add sorting by website or username
- Import and export password databases
- Support a master password for unlocking the vault
- Add logging for password changes
- Improve error handling with `try`/`except`
- Refactor the project into classes and separate modules
- Build a graphical desktop interface (PySide6)
- Package the application as a standalone executable
- Store passwords in a database (SQLite) instead of JSON
- Sync encrypted passwords across devices

## License

This project is licensed under the MIT License.

## Final Note

Note: This is a Version 1 project built while learning Python fundamentals. The focus was on practicing file handling, JSON, functions, and command-line application development before exploring more advanced topics such as encryption, databases, and graphical user interfaces.