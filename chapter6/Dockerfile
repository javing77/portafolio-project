# Dockerfile for Chapter 6
# Start with the slim parent image
FROM python:3.12-slim

# Set the Docker working directory
WORKDIR /code

# Copy from the build context directory to the Docker working directory
COPY requirements.txt /code/

# Install the Python libraries listed in the requirements file
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Copy the code files and database from the build context directory
COPY *.py /code/
COPY *.db /code/

# Launch the uvicorn web server and run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
