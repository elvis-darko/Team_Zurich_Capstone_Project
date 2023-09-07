# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 (Streamlit) and 8000 (FastAPI) available to the world outside this container
EXPOSE 8501
EXPOSE 8000

# Create a startup script to run both FastAPI and Streamlit
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Run the startup script as the CMD
CMD ["/app/start.sh"]
