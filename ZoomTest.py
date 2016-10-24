import numpy as np
import cv2
import imutils
'''
This Zoom Program was written by: Carlos J. Flores of F.I.U.
'''
cap = cv2.VideoCapture(0)
ret, frame = cap.read() # Initializing the video frame
# setting width & height of the video frame
width = frame.shape[1] 
height = frame.shape[0]

def Zoom(cv2Object, zoomSize):
    # Resizes the image/video frame to the specified amount of "zoomSize".
    # A zoomSize of "2", for example, will double the canvas size
    cv2Object = imutils.resize(cv2Object, width=(zoomSize * cv2Object.shape[1]))
    # center is simply half of the height & width (y/2,x/2)
    center = (cv2Object.shape[0]/2,cv2Object.shape[1]/2)
    # cropScale represents the top left corner of the cropped frame (y/x)
    cropScale = (center[0]/zoomSize, center[1]/zoomSize)
    # The image/video frame is cropped to the center with a size of the original picture
    # image[y1:y2,x1:x2] is used to iterate and grab a portion of an image
    # (y1,x1) is the top left corner and (y2,x1) is the bottom right corner of new cropped frame.
    cv2Object = cv2Object[cropScale[0]:(center[0] + cropScale[0]), cropScale[1]:(center[1] + cropScale[1])]
    return cv2Object

#Zoom(frame, 4)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Zooming in
    #frame = imutils.resize(frame, width=1280) #doubling the width
    #frame = frame[240:720,320:960]
    frame = Zoom(frame,2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing the capture
cv2.imwrite("CanvasTest12.png", frame)
cap.release()
cv2.destroyAllWindows()