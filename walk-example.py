from naoqi import ALProxy, ALModule, ALBroker

IP = "192.168.5.29"  # Replace here with your NaoQi's IP address.
PORT = 9559

motion = ALProxy("ALMotion", IP, PORT)


# voordat we kunnen lopen moeten we eerst altijd walkInit doen
# walkInit zorgt ervoor dat de robot staat en dat alle motors klaar zijn
motion.walkInit()

# we gebruiken motion.walkTo(x, y, theta)
# loop een halve meter naar voren
motion.walkTo(0.5, 0, 0)

# loop een meter naar rechts
# met post wachten we totdat 
motion.post.walkTo(0, 1, 0)

# loop naar voren en draai naar rechts
motion.post.walkTo(1, 0, 1)