FROM python:3.9

WORKDIR /app

#RUN pip install -r requirements.txt

CMD uvicorn main app.main:app --port=8000 --host=0.0.0.0