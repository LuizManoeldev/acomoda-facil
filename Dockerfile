# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /api
WORKDIR /api

# Copy the entire contents of the current directory into the container at /api
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run uvicorn with the correct module and application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
