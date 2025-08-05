import cv2                                   #(1)video capturing
cap=cv2.VideoCapture(0)                      #(2)
while True:                                  #(3)
    _, frame = cap.read()                    #(4)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #(5) rgb or greyscale conversion we can do, convertColor
    cv2.imshow('Virtual Mouse',frame)                         #(6)to show the img
    cv2.waitKey(1)                                            #(7)