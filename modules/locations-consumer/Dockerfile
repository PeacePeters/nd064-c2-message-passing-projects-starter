FROM python:3.8-slim

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5007

COPY . .

CMD ["python", "connect.py"]