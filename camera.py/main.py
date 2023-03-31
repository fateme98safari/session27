import cv2
import numpy as np

cap=cv2.VideoCapture(0)
_,frame=cap.read()
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
row,col=frame.shape
writer = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(*'xivd'), 30, (col, row))

while 1==1:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    row,col=frame.shape
    cv2.rectangle(frame,(230,300),(380,200),0,3)
    pic=frame[240:260 , 300:340]

    blurred = cv2.GaussianBlur(frame, (25,25), 0)
    frame[0:200, 0:640] = blurred[0:200, 0:640]
    frame[300:480, 0:640] = blurred[300:480, 0:640]
    frame[200:300, 0:228] = blurred[200:300, 0:228]
    frame[200:300, 380:640] = blurred[200:300, 380:640]

    mean=np.mean(pic)
    if mean>180:
        color="White"

    elif mean<60:
        color="Black"

    else:
        color="Gray"

    cv2.putText(frame,color,(270,180),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)

    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("result",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

writer.release()
