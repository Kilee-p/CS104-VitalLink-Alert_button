import time
import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

json_body = {
	"chat_id": "8977374084",
	"text": "Someone pressed the alert button!"
	}

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")
button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            button_pressed = True
            requests.post("https://api.telegram.org/bot8779396990:AAGDMkiC03BCQnLk1CLIm8lg0hzwAyH_jtc/sendMessage", json = json_body)        
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()
