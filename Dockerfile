FROM python:3.8-silm

WORKDIR /app

COPY app.py /app

RUN pip install Flsk

EXPOSE 5000

CMD ["python","app.py"]
