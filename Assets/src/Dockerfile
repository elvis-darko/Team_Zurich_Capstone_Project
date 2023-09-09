# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install streamlit
RUN pip install streamlit

# Expose the ports

EXPOSE 8501
EXPOSE 8000

# Create an entry point script to run both FastAPI and Streamlit
RUN echo 'uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --workers 4 & streamlit run streamlit.app.py' > entrypoint.sh
RUN chmod +x entrypoint.sh

# Use the entry point script to start the services
CMD ["./entrypoint.sh"]
