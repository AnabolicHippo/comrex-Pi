import RPi.GPIO as GPIO


def connect():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18, GPIO.LOW)

connect()
