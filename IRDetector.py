import RPi.GPIO as gpio import time

sensor = 16 buzzer = 18 brake = 24
gpio.setmode(gpio.BCM) gpio.setup(sensor, gpio.IN)
gpio.setup(buzzer, gpio.OUT, initial=gpio.LOW) gpio.setup(brake, gpio.OUT, initial=gpio.LOW)

try:
while True:
if gpio.input(sensor): gpio.output(buzzer, True) print
"Obstacle Detected" while gpio.input(sensor):
gpio.output(brake, True) if speed > 0:
speed -= 1 time.sleep(0.2)

else:
gpio.output(buzzer, False) gpio.output(brake, True)


except KeyboardInterrupt: gpio.cleanup()
