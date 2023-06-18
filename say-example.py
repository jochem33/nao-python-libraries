from naoqi import ALProxy, ALModule

IP = "192.168.5.29"  # Replace here with your Nao's IP address.
PORT = 9559

tts = ALProxy("ALTextToSpeech", IP, PORT)

tts.say("Hello world!")