##Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
##Type "copyright", "credits" or "license()" for more information.
import cv2
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture=cv2.VideoCapture(0)
while True:
	ret, frame= video_capture.read()
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2Gray)
	faces=faceCascade.detectMultiscale(gray,scaleFactor=1.1,minNeighbours=5,minSize=(30,30))
	for (x,y,w,h) in faces:
		cv2.rectagle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.imshow('Video',frame)
		if cv2.waitkey(1) &  0xFF==ord('q'):
	break
return 0

video_capture.release()
cv2.destroyAllWindows()

 
 

	
