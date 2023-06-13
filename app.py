import os
from dotenv import load_dotenv
from celery import Celery
from flask import Flask, render_template
import requests
import json

load_dotenv()

# used to load our env variables

# used to setup celery with flask as per the official documentation
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_BACKEND_URL"], #desde el archivo de conf
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask_app = Flask(__name__)
#actualizamos la conf con la info traida del .env file
flask_app.config.update(
    CELERY_BROKER_URL=os.environ.get("CELERY_BROKER_URL"),
    CELERY_BACKEND_URL=os.environ.get("CELERY_BACKEND_URL"),
)

# create an instance of celery using the function created earlier
celery = make_celery(flask_app)

# This fetches the links and returns an array of what's consumed
@celery.task() #Se usa este decorador para indicar que esto es una tarea
def get_dog_pics(breed_type, limit):
    url = "https://dog.ceo/api/breed/" + breed_type + "/images/random/" + limit
    r = requests.get(url)
    files = r.json()
    print(r.status_code)

    for file in files["message"]:
        with open("url.txt", "a") as myfile:
            myfile.write(" " + file)
    return files["message"]

# import routes as this is the client-side
import routes
