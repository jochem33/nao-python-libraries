import sys
import math


def setPose(motion, pose):

    
    # Define The Initial Position for the upper body


    # Get the Robot Configuration
    # robotConfig = motion.getRobotConfig()
    # robotName = ""
    # for i in range(len(robotConfig[0])):
    print("naoH25 pose")

    Head     = [pose["HeadYawAngle"], pose["HeadPitchAngle"]]

    LeftArm  = [pose["LeftShoulderPitchAngle"], pose["LeftShoulderRollAngle"], pose["LeftElbowYawAngle"], pose["LeftElbowRollAngle"], pose["LeftWristYawAngle"], pose["LeftHandAngle"]]
    RightArm = [pose["RightShoulderPitchAngle"], -pose["RightShoulderRollAngle"], -pose["RightElbowYawAngle"], -pose["RightElbowRollAngle"], pose["RightWristYawAngle"], pose["RightHandAngle"]]
                                            
    LeftLeg  = [0.0,                      #hipYawPitch          
                pose["spreadAngle"],              #hipRoll
                -pose["leftKneeAngle"]/2-pose["torsoAngle"],  #hipPitch
                pose["leftKneeAngle"],                #kneePitch
                -pose["leftKneeAngle"]/2,             #anklePitch
                -pose["leftAnkleRoll"]]             #ankleRoll
    RightLeg = [0.0, 
                -pose["spreadAngle"],
                -pose["rightKneeAngle"]/2-pose["torsoAngle"],
                pose["rightKneeAngle"], 
                -pose["rightKneeAngle"]/2, 
                pose["rightAnkleRoll"]]

    # Gather the joints together
    pTargetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm

    # Convert to radians
    pTargetAngles = [ x * math.pi / 180 for x in pTargetAngles]
    
    motion.stiffnessInterpolation("Body", 1.0, 0.5)

    pNames = "Body"
    pMaxSpeedFraction = 0.2
    motion.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)



def doTimeline(motion, timeline):
    for pose in timeline:
        setPose(motion, pose)
