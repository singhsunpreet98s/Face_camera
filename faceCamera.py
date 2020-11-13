import cv2 as cv
video = cv.VideoCapture(0)
faceCasacade = cv.CascadeClassifier("face.xml")
color1 = (0,146,220)
color2 = (0,0,220)
while True:
    check, frame = video.read()
    gray_img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    ret, otsu = cv.threshold(frame, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    face = faceCasacade.detectMultiScale(th3,
                                  scaleFactor=1.2,
                                  minNeighbors=1,
                                  minSize=(20,20))
    for (x,y,w,h) in face:
        if(w>200):
            cv.putText(frame,"face",(x+int(w/2),int(y-5)),cv.FONT_HERSHEY_SIMPLEX,1,color2,2 )
            cv.rectangle(frame,(x,y),(x+w,y+h),color2,2)
        else:
            cv.rectangle(frame, (x, y), (x + w, y + h), color1, 2)
        cv.imshow('app',frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
video.release()
cv.destroyAllWindows()