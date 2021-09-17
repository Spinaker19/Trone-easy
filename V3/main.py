import RPi.GPIO as GPIO
import os
import pygame

blue_button = 37
green_button = 18
red_button = 22
white_button = 36 
yellow_button = 31 
buzzer = 16
led = 18
path_background = 'sudo fbi -T 1 Background.jpg'

def read(args):
    img = args + ".jpg"
    sono = args + ".mp3"
    path = '/home/pi/Trone/Source/' + img
    path_sono = '/home/pi/Trone/Source/' + sono
    string = 'sudo fbi -T 1 ' + path
    os.system('sudo pkill fbi')
    os.system(string)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(path_sono)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    print("Son joue")
    os.system('sudo pkill fbi')
    os.system(path_background)

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
            read("Lac")
        elif GPIO.input (green_button) :
            read("BAISE", 25)
        elif GPIO.input (red_button) :
            read("point_pour_mamouth", 25)
        elif GPIO.input (white_button) :
            read("RienAFoutre")
        elif GPIO.input (yellow_button) :
            read("sasageyo")
        elif GPIO.input (buzzer) :
            GPIO.output (led, GPIO.HIGH)
            read("aglou")
            GPIO.output (led, GPIO.LOW)
        elif GPIO.input (40):
            os.system('sudo pkill fbi')
            break

os.system(path_background)
main()