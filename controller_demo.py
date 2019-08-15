from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



"""
setupPins for GPIO use
"""
def setupPins():
	pins = [2, 3, 4, 17]
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)


def turnOnPins(pins):
	if isinstance(pins, list):
		for pin in pins:
			GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pins, GPIO.HIGH)
	
def turnOffPins(pins):
	if isinstance(pins, list):
		for pin in pins:
			GPIO.output(pin, GPIO.LOW)
	else:
		GPIO.output(pins, GPIO.LOW)

def main():
	while True:
		try:
			with ControllerResource() as joystick:
				print('Found a joystick and connected')
				while joystick.connected:
					x, y = joystick['l']
					if (x > 0.5):
						turnOnPins(2)
					else:
						turnOffPins(2)
					
					rtX = joystick['rt']
					#print(rtX)
					if(rtX > 0.99):
						turnOnPins([2, 3, 4, 17])
					elif(rtX > 0.75):
						turnOnPins([2, 3, 4])
						turnOffPins([17])
					elif(rtX > 0.5):
						turnOnPins([2, 3])
						turnOffPins([4, 17])
					elif(rtX > 0.25):
						turnOnPins([2])
						turnOffPins([3, 4, 17])
					else:
						turnOffPins([2, 3, 4, 17])

					
							
				
			print('Connection to joystick lost')
		except IOError:
			print('Unable to find any joysticks')
			time.sleep(1.0)
			
setupPins()
main()
