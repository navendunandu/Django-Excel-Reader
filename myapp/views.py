import pandas as pd
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Student

def upload_excel(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        # Validate file type
        if not (file.name.endswith('.xlsx') or file.name.endswith('.xls')):
            messages.error(request, "Invalid file format! Only .xlsx or .xls files are allowed.")
            return render(request, "myapp/upload.html")

        try:
            df = pd.read_excel(file)

            # Required columns check
            required_columns = {"Name", "Email", "Contact", "Department", "Course"}
            if not required_columns.issubset(df.columns):
                messages.error(request, "Invalid Excel format! Required columns: Name, Email, Contact, Department, Course")
                return render(request, "myapp/upload.html")

            for _, row in df.iterrows():
                name, email, contact, department, course = row["Name"], row["Email"], row["Contact"], row["Department"], row["Course"]

                # Validate email format
                if "@" not in str(email):
                    messages.error(request, f"Invalid email: {email}")
                    continue  # Skip this record

                # Validate phone number (assuming a 10-digit format)
                if not str(contact).isdigit() or len(str(contact)) != 10:
                    messages.error(request, f"Invalid contact number: {contact}")
                    continue

                # Prevent duplicate emails
                if not Student.objects.filter(email=email).exists():
                    Student.objects.create(
                        name=name, email=email, contact=contact, department=department, course=course
                    )

            messages.success(request, "File uploaded and data saved successfully!")
        except Exception as e:
            messages.error(request, f"Error processing file: {str(e)}")

    return render(request, "myapp/upload.html")
