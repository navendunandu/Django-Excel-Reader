# Student Excel Upload System

## Overview
This is a Django-based web application that allows users to upload an Excel file containing student details (Name, Email, Contact, Department, Course) and automatically stores the data in an SQLite database after validation.

## Features
- **File Upload System**
  - Supports `.xlsx` and `.xls` formats
  - File size validation
- **Data Validation**
  - Checks required fields
  - Validates email format and phone number
  - Prevents duplicate entries
- **Database Storage**
  - Saves student records into SQLite
  - Handles batch processing
- **User Interface**
  - Responsive upload interface with Bootstrap
  - Displays success/error messages
- **Security**
  - File type validation
  - CSRF protection

## Technologies Used
- **Backend:** Django 4.x, Python 3.x
- **Database:** SQLite
- **Excel Processing:** pandas, openpyxl, xlrd
- **Frontend:** Bootstrap

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/student-upload.git
   cd student-upload
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the server:
   ```sh
   python manage.py runserver
   ```
6. Open in browser:
   ```
   http://127.0.0.1:8000/upload/
   ```

## Usage
- Navigate to the **Upload Page**.
- Upload an Excel file containing student details.
- The system validates and stores the data.
- View the uploaded student records in the database.

## Project Structure
```
student_upload/
│── myapp/
│   │── migrations/
│   │── templates/
│   │   │── base.html
│   │   │── upload.html
│   │── models.py
│   │── views.py
│   │── urls.py
│── student_upload/
│── db.sqlite3
│── manage.py
│── requirements.txt
│── README.md
```

## Excel File Format
Ensure your Excel file follows this format:
| Name         | Email                  | Contact     | Department       | Course |
|-------------|------------------------|------------|-----------------|--------|
| John Doe    | johndoe@example.com     | 9876543210 | Computer Science | B.Tech |

## License
This project is open-source under the MIT License.

## Contributing
Feel free to submit pull requests or report issues!

