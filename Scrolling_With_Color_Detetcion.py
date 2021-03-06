import cv2
import numpy as np
import pyautogui

#  to use camera resource
cap = cv2.VideoCapture(0)

#  color array that by which we want to detect it
yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    #  frame to capture 
  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    # gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY )
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #  creating contour so we can have a shape arround yellow color to avoid noices

    for c in contours:
        area = cv2.contourArea(c)
        # print(area)
       
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('space')
     

            prev_y = y
    cv2.imshow('frame', frame)
  
    if cv2.waitKey(10) == ord('e'):
        
        break

cap.release() 
#  turn off camera
cv2.destroyAllWindows()
#  turn all windows / camera windows close

i