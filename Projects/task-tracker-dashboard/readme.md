# Task Tracker Dashboard

This project is a lightweight task tracking dashboard that supports adding, editing, and organizing tasks with an intuitive UI and dynamic priority handling. It simulates a simplified task manager for internal teams such as operations, engineering, or marketing to track priorities without needing full-scale project management tools.

## Features

- Create, update, delete tasks
- Assign task priorities and auto-adjust based on reordering
- Simple drag-and-drop interface for sorting
- Persistent storage using SQLite or flat file (JSON/CSV)
- Visual status indicators (e.g., completed, high-priority)
- Clean frontend using vanilla JavaScript or Chart.js for basic stats

## Tech Stack

- Python (Flask) or Node.js (Express)
- SQLite or JSON/CSV for storage
- HTML/CSS/JavaScript (Chart.js optional for task metrics)
- Deployed locally or on GitHub Pages / Render

## Use Case

- Internal team task board (agile sprint substitute)
- Personal to-do list manager with metadata
- Education project to show CRUD, UI interaction, and database handling

## File Structure

```
task-tracker-dashboard/
├── app.py / index.js
├── static/
│   └── style.css, script.js
├── templates/
│   └── index.html
├── data/
│   └── tasks.db or tasks.json
└── README.md
```

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/task-tracker-dashboard.git
cd task-tracker-dashboard
```

2. Install dependencies:
- For Flask:
```bash
pip install flask
python app.py
```
- For Node.js:
```bash
npm install
node index.js
```

3. Open in browser:
```
http://localhost:5000
```

## Screenshots

Include screenshots or screen recording of your drag-and-drop UI and priority indicator logic here.

## Author

Felicia Acuna  
[LinkedIn](https://www.linkedin.com/in/felicia-acuna) | [GitHub](https://github.com/fracuna1)
