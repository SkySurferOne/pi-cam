from flask import Flask, render_template, request, json, send_file
from flask_mail import Mail, Message
from jinja2 import Environment, PackageLoader, select_autoescape

from camera import Camera
from camera.constants import ASSETS_DIR, TMP_DIR

env = Environment(
    loader=PackageLoader('web_server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
mail = Mail(app)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'my_username@gmail.com',
    MAIL_PASSWORD = 'my_password',
))
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


@app.route("/photo")
def make_photo():
    try:
        photo_name = cam.save_photo()
        content = {
            'name': photo_name
        }
        return json.dumps(content), 200, {'ContentType': 'application/json'}

    except Exception:
        return json.dumps({'msg': 'Make photo error'}), 500, {'ContentType': 'application/json'}


@app.route('/photo/<photo_name>')
def get_photo(photo_name):
    photo_dir = TMP_DIR + photo_name
    return send_file(photo_dir, mimetype='image/jpg')


@app.route('/mail/photo/<photo_name>', methods=['POST'])
def send_photo(photo_name):
    content = request.get_json()
    email = content['email']
    print(email)

    msg = Message("Hello " + photo_name,
                  sender="picam@picam.com",
                  recipients=[email])
    msg.body = "testing"
    msg.html = "<b>testing</b>"

    with mail.connect() as conn:
        conn.send(msg)

    return json.dumps({'message': 'send'}), 200,\
           {'ContentType': 'application/json'}


def run_app(camera_obj, host='127.0.0.1', port=5000):
    global cam
    cam = camera_obj
    app.run(host=host, port=port)
