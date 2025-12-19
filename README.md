📦 How to Run This Project Locally

Follow these steps to run the project on your own computer.

🔹 Prerequisites

Make sure you have the following installed:

Python 3.9+

Git

A code editor (VS Code recommended)

🔹 Step 1: Clone the Repository

Open terminal / command prompt and run:

git clone https://github.com/your-username/file-manager.git
cd file-manager

🔹 Step 2: Create & Activate Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate


You should see (venv) in the terminal.

🔹 Step 3: Install Backend Dependencies
pip install -r requirements.txt

🔹 Step 4: Start the Backend Server
uvicorn app.main:app --reload


Backend will start at:

http://127.0.0.1:8000

🔹 Step 5: Open Frontend

There are two ways:

Option 1: Open directly

Go to frontend/

Open login.html or index.html in browser

Option 2: Using VS Code Live Server (Recommended)

Install Live Server extension

Right-click login.html

Click Open with Live Server

🔹 Step 6: Use the Application

Register a new account

Login

Upload / view files

Logout

🔹 API Documentation (Optional)

Once backend is running, visit:

http://127.0.0.1:8000/docs


This opens FastAPI Swagger UI.

🔹 Common Issues & Fixes

Port already in use

uvicorn app.main:app --reload --port 8001


Module not found error

pip install -r requirements.txt


CORS issue

Make sure backend is running before frontend

🔹 Project Structure
file-manager/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── routes_auth.py
│   │   ├── routes_files.py
│   │   └── utils.py
│
├── frontend/
│   ├── login.html
│   ├── index.html
│   ├── dashboard.html
│   ├── *.css
│   └── *.js
│
├── uploads/
├── requirements.txt
└── README.md
------------------------------------------------------------------
🔹 Notes

Database (app.db) is created automatically on first run

uploads/ folder stores uploaded files

JWT authentication is used

--------------------------------------------------------------

# File Manager Project

A File Manager web application built using:
- FastAPI (Backend)
- HTML, CSS, JavaScript (Frontend)
- JWT Authentication

## Features
- User Authentication
- File Upload & Download
- Secure API routes

## Run Backend
uvicorn app.main:app --reload
