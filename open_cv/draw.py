# BGR -> in cv2
import cv2 as cv
import numpy as np

blank = np.zeros((400,400,3), dtype = "uint8")
# blank[300:400, 200:300] = 0,255,0 
# green = blank.copy()

# green[:] =  0,255,0 
# cv.imshow("Green",green)

# 1 draw rect 

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=cv.FILLED)
# Draw Circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255),thickness = 3)
cv.text
cv.imshow("Green marked", blank)
cv.waitKey(0)
cv.destroyAllWindows()


