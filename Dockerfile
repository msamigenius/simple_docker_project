FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project code
COPY . .


# Command to start the Django server by default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
