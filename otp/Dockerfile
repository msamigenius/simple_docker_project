FROM python:3.12-slim

# Set the working directory
WORKDIR /otp

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy OTP app code
COPY . .


# Start Celery worker
CMD ["celery", "-A", "management_celery", "worker", "--loglevel=info"]
