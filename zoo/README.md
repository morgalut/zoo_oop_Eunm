# Zoo Management System

This is a Zoo Management System implemented in Python using Object-Oriented Programming (OOP) principles. The system supports adding animals, logging their actions, and saving information to a database.

## Features

- Categorize animals into mammals, fish, and birds using Enums.
- Log every action taken using a logger.
- Save animal information to a SQLite database.
- Enable debugging mode via command-line arguments.
- List animal counts by category via command-line arguments.

## Directory Structure


## File Descriptions

### `main.py`

The main entry point of the application. It sets up the debugging, initializes the animals, interacts with the database, and handles command-line arguments.

### `animal.py`

Defines the base `Animal` class, which other specific animal classes inherit from. It includes basic properties and methods that all animals should have.

### `animals/lion.py`

Defines the `Lion` class, which inherits from the `Animal` class and implements the specific behaviors of a lion.

### `animals/elephant.py`

Defines the `Elephant` class, which inherits from the `Animal` class and implements the specific behaviors of an elephant.

### `utils/constants.py`

Contains the `AnimalType` and `AnimalCategory` Enums used to categorize animals.

### `utils/debug.py`

Defines the `Debug` class for logging debug messages. It uses the logger configured in `logger_config.py`.

### `utils/logger_config.py`

Configures the logger to log messages to both the console and a file (`zoo.log`).

### `database/db_helper.py`

Handles interactions with the SQLite database, including setting up the database, adding animals, and counting animals by category.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-repo/zoo-management-system.git
    cd zoo-management-system
    ```

2. Ensure you have Python installed. This project is compatible with Python 3.6 and above.

3. Install required packages (if any). For SQLite, no external packages are needed as it's included with Python.

## Usage

### Running the Application

To run the application, navigate to the `zoo` directory and use the following command:

```sh
python -m zoo.main
