import cv2
import numpy as np

from camera.PhotoEffects.PhotoEffect import PhotoEffect


class AddingObjectsPhotoEffect(PhotoEffect):

    def __init__(self, object_image) -> None:
        
        '''
            :param object_image: filename
            '''
        super().__init__()
        self.object_image = object_image
        #???
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        #
        cv2.namedWindow('image')
        cv2.createTrackbar('colormap', 'image', 0, 12, nothing)
        cv2.createTrackbar('R', 'image', 0, 255, nothing)
        cv2.createTrackbar('G', 'image', 0, 255, nothing)
        cv2.createTrackbar('B', 'image', 0, 255, nothing)

        switch = 'Colorize\n0 : OFF \n1 : ON'
        cv2.createTrackbar(switch, 'image', 0, 1, nothing)
        
        cap = cv2.VideoCapture(0)
        #
        anterior = 0
        #

    def apply_filter(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(90, 90)
        )
        for (x, y, w, h) in faces:
            obj_img = cv2.imread(self.object_image)
            res = cv2.resize(obj_img,(w, h), interpolation = cv2.INTER_CUBIC)
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            rows, cols, channels = res.shape
            roi = image[y:(y+h), x:(x+w)]
            
            obj_imggray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(obj_imggray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
            img2_fg = cv2.bitwise_and(res,res,mask = mask_inv)
            # Put logo in ROI and modify the main image
            dst = cv2.add(img1_bg,img2_fg)
            image[y:(y+h), x:(x+w)] = dst
            return image

    def set_colormap_num(self, colormap_num):
        self.colormap_num = colormap_num

