# Use an official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy your Streamlit app code and model file into the container
COPY streamlit.app.py /app/
COPY tuned_gb_model.joblib /app/

# Install required Python packages
RUN pip install streamlit joblib scikit-learn matplotlib numpy requests

# Expose the port for Streamlit
EXPOSE 8501

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "streamlit.app.py"]
