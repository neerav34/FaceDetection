import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
# path='dataset/'+face_id
while (1):
    face_id = (input('\n Enter User ID ==>  '))
    path = './FacialDetection/dataset/User.'+face_id+'.1.jpg'
    isExist = os.path.exists(path)
    # print(isExist)
    if isExist:
        print(" User ID Already Taken")
    else:
        break
            
	    # face_id=str(input("Enter User ID Again: "))
# else:
#     os.makedirs(path)
# Initialize individual sampling face count
count = 0



name = input(" Enter your name: ")
with open("Details.txt", "a") as f:
     f.write(f"{name}\n")
     
print("\n [INFO] Initializing face capture. Look the camera and wait ...")




while(True):
    ret, img = cam.read()
    # frame=cam.read()
    # img = cv2.flip(img, -1) # flip video image vertically
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)     
        count += 1
        name='"./FacialDetection/dataset/User."'+face_id+'/'+ str(count) + '.jpg'  # count of number of images taken
        print("Creating Images........." +name)
        # Save the captured image into the datasets folder
        cv2.imwrite("FacialDetection/dataset/User." + str(face_id) + '.' +  
                    str(count) + ".jpg", img[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 200: # Take 100 face sample and stop video
         break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()