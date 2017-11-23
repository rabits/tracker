import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, 1)

    import time
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting")
finally:
    GPIO.cleanup()
