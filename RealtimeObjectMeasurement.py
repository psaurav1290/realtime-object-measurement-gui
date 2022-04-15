import cv2
import utils

class App():
    _webcam = False
    _path = "sample_image.jpg"
    _cam = cv2.VideoCapture(0)
    _cam.set(10,160) # Brightness
    _cam.set(3,1920) # Width
    _cam.set(4,1080) # Height
    _scale = 3
    _hP = 455 * _scale
    _wP= 305 * _scale

    def __init__(self):
        pass

    def get_image(self, path=""):
        if self._webcam:
            success,img = self._cam.read()
        else:
            img = cv2.imread(path)

        yield img
        imgContours, conts = utils.getContours(img, minArea=50000, filter=4)
        if len(conts) != 0:
            biggest = conts[0][2]
            # print(biggest)
            imgWarp = utils.warpImg(img, biggest, self._wP, self._hP)
            imgContours2, conts2 = utils.getContours(imgWarp, minArea=2000, filter=4, cThr=[50, 50], draw=False)
            if len(conts) != 0:
                for obj in conts2:
                    cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                    nPoints = utils.reorder(obj[2])
                    nW = round((utils.findDis(nPoints[0][0]//self._scale, nPoints[1][0]//self._scale)/10), 1)
                    nH = round((utils.findDis(nPoints[0][0]//self._scale, nPoints[2][0]//self._scale)/10), 1)
                    cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]), (255, 0, 255), 3, 8, 0, 0.05)
                    cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]), (255, 0, 255), 3, 8, 0, 0.05)
                    
                    x, y, w, h = obj[3]
                    cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 0, 255), 2)
                    cv2.putText(imgContours2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 0, 255), 2)
            # cv2.imshow('A4', imgContours2)
            # imgContours2 = cv2.resize(imgContours2, (0, 0), None, 0.5, 0.5)
            yield imgContours2

        # img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
        # cv2.imshow('Original', img)
        # cv2.waitKey(1)
        
        return
