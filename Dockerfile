# Use an existing base image
FROM python:3.11-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the files to the container
COPY . .

# Specify the command to run when the container starts
CMD ["python", "main.py"]

# Port to expose
EXPOSE 5000

# Volume to mount
VOLUME /opt/unetlab/
