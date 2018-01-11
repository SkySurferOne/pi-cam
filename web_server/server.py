from flask import Flask, render_template, request, json
from jinja2 import Environment, PackageLoader, select_autoescape

from camera import Camera

env = Environment(
    loader=PackageLoader('web_server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
cam = None


@app.route("/")
def hello():
    return render_template('content.html', title='Pi-cam', header_text='Choose your filter!')


@app.route('/effect-bundle', methods=['POST'])
def set_effect_bundle():
    content = request.get_json()
    effect_name = content['name']

    try:
        effect_enum = Camera.EffectBundleEnum(effect_name)
        cam.set_effect_bundle(effect_enum)
    except ValueError:
        return json.dumps({'msg': 'Wrong effect name'}), 400, {'ContentType': 'application/json'}

    return json.dumps(content), 200, {'ContentType': 'application/json'}


def run_app(camera_obj, host='127.0.0.1', port=5000):
    global cam
    cam = camera_obj
    app.run(host=host, port=port)
