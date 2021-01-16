import cv2 as cv
import numpy as np
img = np.zeros((500,500),dtype = "uint8")
cv.putText(img,"Qazi Arsalan",(10,300),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
cv.imshow("tetx",img)

cv.waitKey(0)
cv.destroyAllWindows()

# Stackoverflow
# font                   = cv2.FONT_HERSHEY_SIMPLEX
# bottomLeftCornerOfText = (10,500)
# fontScale              = 1
# fontColor              = (255,255,255)
# lineType               = 2

# cv2.putText(img,'Hello World!', 
#     bottomLeftCornerOfText, 
#     font, 
#     fontScale,
#     fontColor,
#     lineType)