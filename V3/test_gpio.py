import RPi.GPIO as GPIO
import pygame

blue_button = 37
green_button = 18
red_button = 22
white_button = 36 
yellow_button = 31 
buzzer = 16
led = 18

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(blue_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(white_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(buzzer, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    while True:
        if GPIO.input (blue_button) :
            print('Blue Button Pushed')
        elif GPIO.input (green_button) :
            print('Green Button Pushed')
        elif GPIO.input (red_button) :
            print('Red Button Pushed')
        elif GPIO.input (white_button) :
            print('White Button Pushed')
        elif GPIO.input (yellow_button) :
            print('Yellow Button Pushed')
        elif GPIO.input (buzzer) :
            GPIO.output (led, GPIO.HIGH)
            print('Buzzer Button Pushed')
            GPIO.output (led, GPIO.LOW)
        elif GPIO.input (40):
            print('=====Program Shutdown=====')
            break
print('======Program Start======')
main()
