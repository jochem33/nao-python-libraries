import naovision
import time

from naoqi import ALProxy

IP = "192.168.5.29" 
PORT = 9559

camera = ALProxy("ALVideoDevice", IP, PORT)


while True:
    naoImage = naovision.getImage(camera)
    succes, x, y, r, shape = naovision.findOrangeBall(naoImage)
    if(succes == True):
        if(r > 20):
            print(x, y, r, shape, x - shape[0]/2)
    time.sleep(5)
