import threading

from camera import Camera
from web_server import run_app

if __name__ == '__main__':
    cam = Camera('pi-cam', 0)

    camera_thread = threading.Thread(target=cam.start_capturing)
    camera_thread.start()

    webapp_thread = threading.Thread(target=run_app, args=(cam,))
    webapp_thread.start()



