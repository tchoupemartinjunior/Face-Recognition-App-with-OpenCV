import cv2
import cv2.aruco as aruco
from random import randrange
#step 1
#load some pretrained data on frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #training takes a lot of time, oencv did it for us

#capture video from webcam
webcam = cv2.VideoCapture("assets\capture1.mp4") # you can also pass in a video file
#webcam = cv2.VideoCapture(0)

"""def findAruco(img,marker-size=6,total_markers=250,draw = True):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_{marker_size}x{marker_size}_{total_markers}')
    arucoDict =aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bbox, ids,_ =aruco.detectMarkers(gray,arucoDict,parameters=arucoParam)
    print(ids)
    if draw:
        aruco.drawMarkers(img,bbox)

    return bbox, ids
"""
#iterate forever over the frames
while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()
    #convert to black and white images
    frame= cv2.resize(frame,(1000,600))
    
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