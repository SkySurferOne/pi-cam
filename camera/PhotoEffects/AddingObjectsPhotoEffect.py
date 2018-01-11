import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect


# def laplacian(img):
#     return cv2.Laplacian(img, cv2.CV_64F)


# def sobel(img, axis='x'):
#     if axis == 'x':
#         return cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
#
#     return cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


def nothing(x):
    pass


class AddingObjectsPhotoEffect(PhotoEffect):
    def __init__(self, object_image) -> None:

        '''
            :param object_image: filename
            '''
        super().__init__()
        self.object_image = object_image
        #

    def apply_filter(self, image):
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        #
        cv2.namedWindow('trackbar_image')
        cv2.createTrackbar('colormap', 'trackbar_image', 0, 12, nothing)
        cv2.createTrackbar('R', 'trackbar_image', 0, 255, nothing)
        cv2.createTrackbar('G', 'trackbar_image', 0, 255, nothing)
        cv2.createTrackbar('B', 'trackbar_image', 0, 255, nothing)

        switch = 'Colorize\n0 : OFF \n1 : ON'
        cv2.createTrackbar(switch, 'trackbar_image', 0, 1, nothing)
        #
        # cap = cv2.VideoCapture(0)
        #
        anterior = 0
        #
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(90, 90)
        )
        for (x, y, w, h) in faces:
            obj_img = cv2.imread(self.object_image)
            res = cv2.resize(obj_img, (w, h), interpolation=cv2.INTER_CUBIC)
            # rows, cols, channels = res.shape
            roi = image[y:(y + h), x:(x + w)]

            obj_imggray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(obj_imggray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
            img2_fg = cv2.bitwise_and(res, res, mask=mask_inv)
            dst = cv2.add(img1_bg, img2_fg)
            image[y:(y + h), x:(x + w)] = dst

        colormap_num = cv2.getTrackbarPos('colormap', 'trackbar_image')
        r = cv2.getTrackbarPos('R', 'trackbar_image')
        g = cv2.getTrackbarPos('G', 'trackbar_image')
        b = cv2.getTrackbarPos('B', 'trackbar_image')
        s = cv2.getTrackbarPos(switch, 'trackbar_image')

        print(colormap_num)
        if colormap_num == -1:
            colormap_num = 0

        if colormap_num != 0:
            img = cv2.applyColorMap(image, colormap_num - 1)
        else:
            img = image

        if s != 0:
            color = np.zeros(shape=img.shape, dtype=np.uint8)
            color[:] = [b, g, r]
            img = cv2.add(img, color)
        return img

    def set_colormap_num(self, colormap_num):
        self.colormap_num = colormap_num
