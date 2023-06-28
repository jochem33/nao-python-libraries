import naovision
import time
import pose

from naoqi import ALProxy

IP = "192.168.5.29" 
PORT = 9559

camera = ALProxy("ALVideoDevice", IP, PORT)
motion = ALProxy("ALMotion", IP, PORT)


pose0 = {
    # head
    "HeadYawAngle": 0.0,
    "HeadPitchAngle": 60.0,

    # left arm 
    "LeftShoulderPitchAngle": 80.0,
    "LeftShoulderRollAngle": 20.0,
    "LeftElbowYawAngle": 0.0,
    "LeftElbowRollAngle": 0.0,
    "LeftWristYawAngle": 0.0,
    "LeftHandAngle": 0.0,

    # right arm
    "RightShoulderPitchAngle": 80.0,
    "RightShoulderRollAngle": 20.0,
    "RightElbowYawAngle": 0.0,
    "RightElbowRollAngle": 0.0,
    "RightWristYawAngle": 0.0,
    "RightHandAngle": 0.0,

    # legs
    "leftKneeAngle": 20.0,
    "rightKneeAngle": 20.0,
    "leftAnkleRoll": 0.0, # should be the same as spreadangle
    "rightAnkleRoll": 0.0, # should be the same as spreadangle
    "torsoAngle": 0.0,
    "spreadAngle": 0.0 
}

motion.walkInit()




while True:
    pose.setPose(motion, pose0)
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
                motion.walkTo(0.5, 0, 0)

    else:
        print("Geen bal gevonden")
    time.sleep(10)
