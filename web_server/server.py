from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('web_server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
cam = None

@app.route("/")
def hello():
    cam.test()
    template = env.get_template('main.html')
    return template.render(title='Pi-cam', header_text='Hello world!')


def run_app(camera_obj, host='127.0.0.1', port=5000):
    global cam
    cam = camera_obj
    app.run(host=host, port=port)
