FROM python:3.10.0-alpine
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install flask
COPY . /app
CMD flask run -h 0.0.0.0 -p 5000
