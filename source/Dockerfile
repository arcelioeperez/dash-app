FROM python:3.8 

WORKDIR /code

COPY requirements.txt app.py insurance.csv /code/ 
RUN pip3 install -r requirements.txt 

CMD ["python3", "docker_app.py"]
