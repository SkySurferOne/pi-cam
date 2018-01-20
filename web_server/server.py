from flask import Flask, render_template, request, json, send_file
from flask_mail import Mail, Message
from jinja2 import Environment, PackageLoader, select_autoescape

from camera import Camera
from camera.constants import TMP_DIR

env = Environment(
    loader=PackageLoader('web_server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
app.config.from_object('default_config')
app.config.from_envvar('PICAM_CONFIG')
mail = Mail(app)

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

    msg = Message('Photo from picam',
                  recipients=[email])
    msg.html = "Hi,<br> that is your photo!"

    with app.open_resource(TMP_DIR + photo_name) as fp:
        msg.attach('photo-picam', "image/jpg", fp.read())

    with mail.connect() as conn:
        conn.send(msg)

    return json.dumps({'message': 'send'}), 200,\
           {'ContentType': 'application/json'}


def run_app(camera_obj, host='127.0.0.1', port=5000):
    global cam
    cam = camera_obj
    app.run(host=host, port=port, debug=True, use_reloader=False)
