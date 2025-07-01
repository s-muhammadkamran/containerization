FROM python:slim

WORKDIR /WelcomeApp

ENV FLASK_APP=welcome-app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /WelcomeApp

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]