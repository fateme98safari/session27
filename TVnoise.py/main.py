import cv2
import imageio
import numpy as np

image=cv2.imread("TVnoise.py\TV.png")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
row,col = image.shape
writer = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(*'xivd'), 30, (col, row))

while 1==1:
    my_image=np.random.random((255,450))*255
    my_image=np.array(my_image,dtype=np.uint8)
    image[95:350,30:480]=my_image
    frame=image
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("TVnoise",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break


writer.release()
# imageio.mimsave('TVnoise.gif', frame, fps=60)

