import cv2

a=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #pre defined file jo install kr rakhi h usko use kr re
if a.empty():
    print("Error: Haar cascade not loaded. Check the XML file path.")
    exit()
b=cv2.VideoCapture(0) 
if not b.isOpened():
    print("Error: Could not open webcam")
    exit()
# #camera access given
#b VARIABLE KA COMMENT REMOVE KRKE CAMERA KO VAPAS ACCESS DEKR IT WILL WORK
#AGAR IMPORT CV2 ME BOLE MODULE NOT FOUNF TO VAPAS pip install opencv-python CHALANA,WE HAVE ALREADY DOWNLOADED THOUGH 
#YEH GADHA H THODU SA.....ALSO OPEN CV ME JO BHI FILE U WANT TO RUN VO python-filename then enter se CHALTI HAI.
#ALSO SAB TERMINAL COMMAND PROMP PER CHALAYA H APAN NE.
while True:
    c_rec,d_image = b.read() #c rectangle h jo muh per aayega on detection,d_image will be the image i.e the face jo capture ho rha h
    e = cv2.cvtColor(d_image,cv2.COLOR_BGR2GRAY)# apni d image ko grayscale me convert kr re
    f = a.detectMultiScale(e,1.3,6)

    for (x1,y1,w1,h1) in f:  #height n width rectangle ki
        cv2.rectangle(d_image,(x1,y1),(x1+w1,y1+h1),(0,255,0),5) #x1,w1 are horizontal n y1,h1 are verticle,als BGR h toh 255,0,0 mtlb blue hollow box around our face,5 is width of the rect box

    cv2.imshow('img',d_image)
    h = cv2.waitKey(40) & 0xff   #40sec tk koi face detect ni hua toh exit types
    if h == 40:
        break

b.release()  #exit from camera
cv2.destroyAllWindows()