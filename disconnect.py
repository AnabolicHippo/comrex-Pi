import RPi.GPIO as GPIO


def disconnect():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18, GPIO.HIGH)
	GPIO.cleanup()
disconnect()
