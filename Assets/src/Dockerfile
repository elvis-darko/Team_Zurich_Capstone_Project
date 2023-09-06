# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8501 (Streamlit) and 8000 (FastAPI) available to the world outside this container
EXPOSE 8501
EXPOSE 8000

# Create a shell script to run both FastAPI and Streamlit
RUN echo 'uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --workers 4 &' > start.sh
RUN echo 'streamlit run streamlit.app.py' >> start.sh
RUN chmod +x start.sh

# Run the shell script as the CMD
CMD ["./start.sh"]
