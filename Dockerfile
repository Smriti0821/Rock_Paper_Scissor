FROM python:3.9
WORKDIR app
COPY . .
EXPOSE 8000
CMD ["python","reminder.py"]