FROM python:3.9.18-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 520

ENTRYPOINT [ "python", "app.py" ]