from flask import Flask, render_template
from celery import Celery
import time

app = Flask(__name__)

celery = Celery(app.name, broker='amqp://guest@localhost:5672//', backend='rpc://')

@celery.task
def activate_pin_task(pinNum):
    # ACTIVATE PIN
    return True

@celery.task
def diactivate_pin_task(pinNum):
    # ACTIVATE PIN
    return True

@app.route('/api/status')
def api_status():

    return "disabled"

@app.route('/api/zalivaj/<int:id>/<int:cas>')
def api_zalivaj(id, cas):
    activate_pin_task.apply_async(args=[id,])
    diactivate_pin_task.apply_async(args=[id,], countdown=cas*60)
    return "done"

@app.route('/api/stop')
def api_ustavi_zalivanje():
    return "done"

@app.route('/')
def index():
    teamplateData = {
        "title": "hello"
    }
    return render_template('index.html', **teamplateData)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
