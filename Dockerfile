FROM python:latest

WORKDIR /aioblog

COPY requirements.txt /aioblog

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /aioblog

EXPOSE 8080
CMD ["python", "/aioblog/app/main.py"]
