FROM python:3.12.0-slim-bullseye
WORKDIR /docker
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./ ./
CMD [ "python3", "-m", "flask", "--app", "learn_flask", "run", "--host=0.0.0.0" ]