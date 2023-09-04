# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose a port for the FastAPI server (if you plan to use FastAPI)
EXPOSE 8000

# Run Streamlit app when the container launches
CMD ["streamlit", "run", "your_streamlit_app.py"]
