# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
# NOTE: must be the same value as env. variable WORKDIR inside .env file
WORKDIR /usr

# Copy the current directory contents into the container at /usr
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# list everything inside container 
# RUN ls 

# Make the entrypoint script executable
RUN chmod +x ./entrypoint.sh

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run Streamlit when the container launches
# CMD ["python", "run", "ingest.py"]
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Use the shell script to run multiple commands
CMD ["./entrypoint.sh"]