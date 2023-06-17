from naoqi import ALProxy
import pose

IP = "192.168.5.29"
PORT = 9559


motion = ALProxy("ALMotion", IP, PORT)

pose0 = {
    # head
    "HeadYawAngle": 0.0,
    "HeadPitchAngle": 0.0,

    # left arm 
    "LeftShoulderPitchAngle": 80.0,
    "LeftShoulderRollAngle": 20.0,
    "LeftElbowYawAngle": 80.0,
    "LeftElbowRollAngle": 60.0,
    "LeftWristYawAngle": 0.0,
    "LeftHandAngle": 0.0,

    # right arm
    "RightShoulderPitchAngle": 80.0,
    "RightShoulderRollAngle": 20.0,
    "RightElbowYawAngle": 80.0,
    "RightElbowRollAngle": 60.0,
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

pose1 = {
    # head
    "HeadYawAngle": 0.0,
    "HeadPitchAngle": 0.0,

    # left arm 
    "LeftShoulderPitchAngle": 80.0,
    "LeftShoulderRollAngle": 20.0,
    "LeftElbowYawAngle": 80.0,
    "LeftElbowRollAngle": 60.0,
    "LeftWristYawAngle": 0.0,
    "LeftHandAngle": 0.0,

    # right arm
    "RightShoulderPitchAngle": 80.0,
    "RightShoulderRollAngle": 20.0,
    "RightElbowYawAngle": 80.0,
    "RightElbowRollAngle": 60.0,
    "RightWristYawAngle": 0.0,
    "RightHandAngle": 0.0,

    # legs
    "leftKneeAngle": 90.0,
    "rightKneeAngle": 90.0,
    "leftAnkleRoll": 0.0, # should be the same as spreadangle
    "rightAnkleRoll": 0.0, # should be the same as spreadangle
    "torsoAngle": 0.0,
    "spreadAngle": 30.0 
}



pose2 = {
    # head
    "HeadYawAngle": 0.0,
    "HeadPitchAngle": 0.0,

    # left arm 
    "LeftShoulderPitchAngle": 80.0,
    "LeftShoulderRollAngle": 20.0,
    "LeftElbowYawAngle": 80.0,
    "LeftElbowRollAngle": 60.0,
    "LeftWristYawAngle": 0.0,
    "LeftHandAngle": 0.0,

    # right arm
    "RightShoulderPitchAngle": 80.0,
    "RightShoulderRollAngle": 20.0,
    "RightElbowYawAngle": 80.0,
    "RightElbowRollAngle": 60.0,
    "RightWristYawAngle": 0.0,
    "RightHandAngle": 0.0,

    # legs
    "leftKneeAngle": 120.0,
    "rightKneeAngle": 120.0,
    "leftAnkleRoll": 0.0, # should be the same as spreadangle
    "rightAnkleRoll": 0.0, # should be the same as spreadangle
    "torsoAngle": 0.0,
    "spreadAngle": 0.0 
}


pose.setPose(motion, pose1)

tl = [pose0, pose1]

pose.doTimeline(motion, tl)