FROM python:3

WORKDIR /app

COPY . /app/

ENV FLASK_APP=app.py 

ENV FLASK_RUN_HOST='0.0.0.0'

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--debug" ]