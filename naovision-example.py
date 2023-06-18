import naovision
import time

from naoqi import ALProxy

IP = "192.168.5.29" 
PORT = 9559

camera = ALProxy("ALVideoDevice", IP, PORT)


while True:
    naoImage = naovision.getImage(IP, PORT, camera)
    x, y, r, shape = naovision.findCircle("camImage.png")
    if((x, y, r) != (None, None, None)):
        if(r > 20):
            print(x, y, r, shape, x - shape[0]/2)
    time.sleep(5)
