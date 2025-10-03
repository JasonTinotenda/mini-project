# Course Recommender System

Welcome! This small desktop app lets students explore available modules by program and year level.
It's built with Python and tkinter. The course data is stored in a simple Python structure
(`courses_data.COURSES`) so it's easy to read and edit.

## What you can do

- Pick a program from the dropdown
- Pick a level (Level 1 to Level 4)
- See the modules for that program and level, grouped by semester, with credits and prerequisites

## Quick setup

1. Make sure you have Python 3.8 or newer. Check with:

```powershell
python --version
```

2. (Optional) Create a virtual environment and activate it so dependencies are isolated:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate
```

3. Install any required packages (there are none for the basic app, but this keeps things explicit):

```powershell
pip install -r requirements.txt
```

## Run the app

From the project folder run:

```powershell
python main.py
```

The window will open. Pick a program and level, then click "Get Recommended Courses".

## Edit or add course data

Open `courses_data.py`. You will see a `COURSES` dictionary containing each program.
Each program has a `levels` dictionary with `Level 1`..`Level 4`, and each level contains
semester lists of module entries. A module should include at least `code`, `name`, and `credits`.
You may also add `core` (True/False) and `prerequisite` (string or comma-separated codes).

Example:

```python
{"code": "CS101", "name": "Intro to Programming", "credits": 10, "core": True}
```

## Troubleshooting tips

- If nothing happens when you run `main.py`, make sure Python is installed and on your PATH.
- If the program list is empty, open `courses_data.py` and look for a typo or syntax error.
- If you get a permissions error when creating a virtual environment, try running PowerShell
  as Administrator.

## Notes for developers

- The app is intentionally simple so it's easy to modify. You can add features like filters,
  searches, or prerequisite checks by editing `main.py` and `courses_data.py`.

## Short user guide

1. Start the app: `python main.py`
2. Choose a program from the first dropdown.
3. Choose a level (Level 1..4) from the second dropdown.
4. Click "Get Recommended Courses" to see the modules.
5. If a message box appears, follow the instruction (for example, select a missing input).

That's all — enjoy exploring the course listings!