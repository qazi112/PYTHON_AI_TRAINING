import cv2 as cv
img = cv.imread("photos/cat.jpeg")
import numpy as np

# Function for rescaling 

def rescaleFrame(frame,scale=0.5):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = tuple((width,height))

    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

capture = cv.VideoCapture(0)

def getWebcamFrames(capture):
# Video reading
    while True:
        
        isTrue,frame = capture.read()
        if isTrue:
            frame_resize = rescaleFrame(frame)

            gray_ori = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            gray_resized = cv.cvtColor(frame_resize,cv.COLOR_BGR2GRAY)
            
            cv.imshow("Frame",gray_ori)
            cv.imshow("Frame Resized", gray_resized)        
            if cv.waitKey(2) & 0xFF == ord('q'):
                break
       
# getWebcamFrames(capture)
capture.release()



resized_img = rescaleFrame(img, scale = 0.4)
cv.imshow("Image",resized_img)
cv.waitKey(0)


cv.destroyAllWindows()