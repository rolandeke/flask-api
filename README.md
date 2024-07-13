# Flask API with SQLite Database

This is a simple Flask application that uses a SQLite database.

## Prerequisites

* Python 3
* Flask
* sqlite3

## Installation

1. Clone this repository or download the files.
2. Create a virtual environment:

   ```bash
   python -m venv .venv

3. Activate Virtual environment
  
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate.bat  # Windows

4. Install required dependencies

   ```bash
   pip install -r requirements.txt

5. Run the ``create_db.py`` script to create the database schema:

    ```bash
   python3 create_db.py

6. Run the Flask application:

    ```bash
   python3 api.py 

This will start the Flask development server on port 5000 by default. You can access the API at http://localhost:5000/.