#Use the official python image from the dockerhub
FROM python:3

#set the working directory to /app
WORKDIR /app

#copy the script to the container
COPY script.py .

#install opencv
RUN pip install opencv-python-headless

#run the script
CMD ["python", "script.py"]