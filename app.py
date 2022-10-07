import cv2
from random import randrange
#step 1
#load some pretrained data on frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#choose an image to detect faces in
img = cv2.imread('assets/many.png')
#img = cv2.resize(img,(340, 220))
#convert to black and white images
black_and_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#DETECT faces 
face_coordinate = trained_face_data.detectMultiScale(black_and_white,3) #multiscale helps check multiple appearences

#print(face_coordinate) #[[106  49 172 172]] [upper left hand, width and height]

#draw rectangles aroun the faces
for (x_coord, y_coord, width, height) in face_coordinate:
    cv2.rectangle(img,(x_coord ,y_coord ),(x_coord+width ,y_coord+height ), (0,randrange(256),255), 4)
   
""" another way to loop   
for i in range(len(face_coordinate)):
    (x_coord, y_coord, width, height)= face_coordinate[i]
    cv2.rectangle(img,(x_coord ,y_coord ),(x_coord+width ,y_coord+height ), (0,0,255), 4)
"""

#------------------------------------------------#
#detect faces on a video




cv2.imshow('martin junior',img)
#cv2.imshow('martin junior',black_and_white)

#helps wait until a key is pressed
cv2.waitKey()


print("code completed")