# Task Tracker CLI

A lightweight Command Line Interface (CLI) application built purely in Python to manage tasks and to-do lists. 
This project runs without any external dependencies and stores data locally in a JSON file.

## Requirements
- Python 3.x

## Getting Started
1. Clone the repository.
2. Run the application using the CLI commands below. 

## Usage

### Adding a new task
.\task-cli add "Buy groceries"

### Updating and deleting tasks
.\task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

### Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

### Listing all tasks
task-cli list

### Listing tasks by status
task-cli list done

task-cli list todo

task-cli list in-progress