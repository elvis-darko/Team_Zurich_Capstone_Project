# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Create and activate a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install streamlit
RUN pip install streamlit


# Make port 8501 (Streamlit) and 8000 (FastAPI) available to the world outside this container
EXPOSE 8501
EXPOSE 8000

# Run FastAPI and Streamlit together using uvicorn
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
CMD ["streamlit", "run", "streamlit.app.py"]
