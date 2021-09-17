import RPi.GPIO as GPIO

blue_button = 11
green_button = 13
red_button = 15
white_button = 29 
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
    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    while True:
        if GPIO.input (blue_button) :
            print('Blue Button Pushed')
        elif GPIO.input (green_button) :
            print('Blue Button Pushed')
        elif GPIO.input (red_button) :
            print('Blue Button Pushed')
        elif GPIO.input (white_button) :
            print('Blue Button Pushed')
        elif GPIO.input (yellow_button) :
            print('Blue Button Pushed')
        elif GPIO.input (buzzer) :
            GPIO.output (led, GPIO.HIGH)
            print('Blue Button Pushed')
            GPIO.output (led, GPIO.LOW)
        elif GPIO.input (36):
            print('=====Program Shutdown=====')
            break
print('======Program Start======')
main