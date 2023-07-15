# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the code into the container
COPY . .

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Lint the code
RUN flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
RUN flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Run tests
RUN pytest

# Set the command to run the application
CMD [ "python", "main.py" ]
