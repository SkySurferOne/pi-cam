import threading
import argparse

from camera import Camera
from camera.constants import ASSETS_DIR
from web_server import run_app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", '--server_ip', help="Http server ip. If empty uses 127.0.0.1.", default='127.0.0.1')
    args = parser.parse_args()

    cam = Camera('pi-cam', 0)

    camera_thread = threading.Thread(target=cam.start_capturing)
    camera_thread.start()

    webapp_thread = threading.Thread(target=run_app, args=(cam, args.server_ip, ))
    webapp_thread.start()


