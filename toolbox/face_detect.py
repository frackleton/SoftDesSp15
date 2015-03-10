import numpy as np 
import cv2

cap =cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((40,40),'uint8')


while(True):
	#capture frame by frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for(x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		cv2.line(frame,(x,y),(x+w,y+h),(0,0,255),5)
		cv2.line(frame,(x,y+h),(x+w,y),(0,0,255),5)
    	
	#Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#When everything done, release the capture

cap.release()
cv2.destroyAllWindows()