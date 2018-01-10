from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('web_server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
cam = None


@app.route("/")
def hello():
    return render_template('content.html', title='Pi-cam', header_text='Choose your filter!')


@app.route("/filter")
def set_filter():
    cam.set_effect_bundle()
    return "OK"


def run_app(camera_obj, host='127.0.0.1', port=5000):
    global cam
    cam = camera_obj
    app.run(host=host, port=port)
