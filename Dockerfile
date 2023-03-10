FROM python:2.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "runserver.py"]

EXPOSE 5000