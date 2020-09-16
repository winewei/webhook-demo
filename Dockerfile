FROM python:3.7.5-slim-stretch

WORKDIR /srv

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["bash", "-c", "python app.py"]
