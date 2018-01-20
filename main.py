import argparse
import threading
import os

from camera import Camera
from camera.constants import TMP_DIR
from web_server import run_app


def clear_tmp():
    for the_file in os.listdir(TMP_DIR):
        file_path = os.path.join(TMP_DIR, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    clear_tmp()

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", '--server_ip', help="Http server ip. If empty uses 127.0.0.1.", default='127.0.0.1')
    parser.add_argument("-p", '--port', help="Server port. If empty uses 5000.", default='5000', type=int)
    args = parser.parse_args()

    cam = Camera('pi-cam', 0)

    camera_thread = threading.Thread(target=cam.start_capturing)
    camera_thread.start()

    webapp_thread = threading.Thread(target=run_app, args=(cam, args.server_ip, args.port,))
    webapp_thread.start()


