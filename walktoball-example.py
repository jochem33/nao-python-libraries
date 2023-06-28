import naovision
import time

from naoqi import ALProxy

IP = "192.168.5.29" 
PORT = 9559

camera = ALProxy("ALVideoDevice", IP, PORT)
motion = ALProxy("ALMotion", IP, PORT)

motion.walkInit()


while True:
    naoImage = naovision.getImage(camera)
    print("image accuired")
    succes, x, y, r, shape = naovision.findOrangeBall(naoImage)
    if(succes == True):
        if(r > 5):
            print("Bal gevonden op: ", x, y)
            print("De groote van de bal is: ", r)
            print("Afstand van midden (x)", x - 460/2)
            angle = (320 - x) / 320.0 * 30.0
            if(angle > 5 or angle < -5):
                motion.walkTo(0, 0, angle * 0.01745329251)

    else:
        print("Geen bal gevonden")
    time.sleep(5)
