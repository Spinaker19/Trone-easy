import RPi.GPIO as GPIO
import os
from ffpyplayer.player import MediaPlayer

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
    sono = args + ".mp4"
    path = '/home/pi/Trone/Source/' + img
    path_sono = '/home/pi/Trone/Source/' + sono
    string = 'sudo fbi -T 1 ' + path
    os.system('sudo pkill fbi')
    os.system(string)
    player = MediaPlayer(path_sono)
    audio_frame, val = player.get_frame()
    if val != 'eof' and audio_frame is not None:
        img, t = audio_frame
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
            read("TestBlanc.mp4")
        elif GPIO.input (green_button) :
            read("TestBleue.mp4", 25)
        elif GPIO.input (red_button) :
            read("TestJaune.mp4", 25)
        elif GPIO.input (white_button) :
            read("TestRouge.mp4", 25)
        elif GPIO.input (yellow_button) :
            read("TestVerte.mp4", 25)
        elif GPIO.input (buzzer) :
            GPIO.output (led, GPIO.HIGH)
            read("aglou")
            GPIO.output (led, GPIO.LOW)
        elif GPIO.input (40):
            os.system('sudo pkill fbi')
            break

os.system(path_background)
main()