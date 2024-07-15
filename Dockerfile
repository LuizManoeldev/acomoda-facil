# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY environment/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the API code into the container
COPY api /app/api
COPY data /app/data
COPY environment /app/environment
# Make port 8000 available to the world outside this container
EXPOSE 9000

# Run main.py when the container launches
CMD ["uvicorn", "api.src.main:app"]