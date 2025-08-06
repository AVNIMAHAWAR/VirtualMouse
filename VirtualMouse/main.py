import cv2                                   #(1)video capturing
import mediapipe as mp                       #(8)hand capturing n all its work
cap=cv2.VideoCapture(0)                      #(2)
hand_detector = mp.solutions.hands.Hands()   #(9) haatho ke coordinates deta h jaise hi camera per haath dikhenge
while True:                                  #(3)
    _, frame = cap.read()                    #(4)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #(5) rgb or greyscale conversion we can do, convertColor
   
    output = hand_detector.process(rgb_frame)         #(9)using HD we'll process the rgb frame n processing se op milega store it in output
    hands = output.multi_hand_landmarks               #(10)
    #print(hands)                                             #(11)since while true ke andar h hum jabtk no hands in frame none prints and jab hands r there in frame toh coordinates print infinatelyyy
    cv2.imshow('Virtual Mouse',frame)                         #(6)to show the img
    cv2.waitKey(1)                                            #(7)