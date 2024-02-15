FROM python:3.8-slim

RUN mkdir /home/data /home/output

COPY script.py /home/script.py

WORKDIR /home

CMD ["python", "/home/script.py"]
