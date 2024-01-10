
My Clock Project
Overview
This project is a CLI application that solves a real-world problem related to time management. The CLI allows users to interact with a database that stores user information and their associated posts. It includes SQLAlchemy ORM for managing the database, Click for building the command-line interface, and basic sorting algorithms for demonstration purposes.

Features
User Management: Add users to the database.
Post Creation: Add posts associated with a user.
Sorting Algorithm: Sort a list of numbers using the Bubble Sort algorithm.
Prerequisites
Python 3.x
Pipenv (for managing dependencies)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/asmaali2/my-clock-project.git
Navigate to the project directory:

bash
Copy code
cd my-clock-project
Create and activate a virtual environment:

bash
Copy code
pipenv install --python 3.x
pipenv shell
Install project dependencies:

bash
Copy code
pipenv install
Create the database tables:

bash
Copy code
python -c "from my_clock.db import create_tables; create_tables()"
Usage
Add User
bash
Copy code
python my_clock_cli.py add_user <username>
Add Post
bash
Copy code
python my_clock_cli.py add_post <username> <title> <content>
Sort Numbers
bash
Copy code
python my_clock_cli.py sort_numbers <number1> <number2> ...
Help
bash
Copy code
python my_clock_cli.py --help
Project Structure
plaintext
Copy code
my-clock-project/
│
├── my_clock/
│   ├── __init__.py
│   ├── models.py
│   ├── db.py
│   └── algorithms.py
│
├── tests/
│   ├── __init__.py
│   └── test_cli.py
│
├── Pipfile
├── Pipfile.lock
└── my_clock_cli.py

Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request.

Acknowledgments
SQLAlchemy - SQL toolkit and Object-Relational Mapping (ORM) library.
Click - Command-line interface creation kit.
Pipenv - Python dependency management tool.

Authors
ASMA ALI








