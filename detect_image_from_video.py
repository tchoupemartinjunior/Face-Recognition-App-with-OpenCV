import cv2
from random import randrange
#step 1
#load some pretrained data on frontals from opencv
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #training takes a lot of time, oencv did it for us

#capture video from webcam
#webcam = cv2.VideoCapture("video.mp4") # you can also pass in a video file
webcam = cv2.VideoCapture(0)

#iterate forever over the frames
while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()
    #convert to black and white images
    
    black_and_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #DETECT faces 
    face_coordinate = trained_face_data.detectMultiScale(black_and_white) #multiscale helps check multiple appearences

    #draw rectangles aroun the faces
    for (x_coord, y_coord, width, height) in face_coordinate:
        cv2.rectangle(frame,(x_coord ,y_coord ),(x_coord+width ,y_coord+height ), (0,randrange(256),randrange(256)), 4)

    cv2.imshow('martin junior',frame)
    key=cv2.waitKey(1) #displays a frame every millisecond
    
    #press q or Q to quit
    if key == 81 or key ==113:
        break
   


""""
#DETECT faces 
face_coordinate = trained_face_data.detectMultiScale(black_and_white) #multiscale helps check multiple appearences

#print(face_coordinate) #[[106  49 172 172]] [upper left hand, width and height]

#draw rectangles aroun the faces
for (x_coord, y_coord, width, height) in face_coordinate:
    cv2.rectangle(img,(x_coord ,y_coord ),(x_coord+width ,y_coord+height ), (0,randrange(256),255), 4)

#------------------------------------------------#
#detect faces on a video




cv2.imshow('martin junior',img)
#cv2.imshow('martin junior',black_and_white)

#helps wait until a key is pressed



print("code completed")"""