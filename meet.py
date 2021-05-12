import pyautogui
import webbrowser
from time import sleep
import schedule



# This function will open your meeting, turn off your mic and camera and enter the meeting! And will only start the code once you click the 'ok' button.
def openmeet(url):
    pyautogui.alert('The program is running. Please do not touch anything on your computer.')
    webbrowser.open(url)
    sleep(10)
    pyautogui.hotkey('ctrl','e')
    pyautogui.hotkey('ctrl','d')
    for i in range(0, 9):
        sleep(0.5)
        pyautogui.press('tab')
    pyautogui.press('enter')

#This function will close the meeting tab.
def closemeet():
    pyautogui.hotkey('ctrl','w')

#This function will define what the function schedule will do.
def job():
    open('https://meet.google.com/gmn-usoq-ynw')  

#This will say what day and time the meeting is going to open
schedule.every().sunday.at('16:45').do(job)

#This will keep the program running everytime
while True:
    schedule.run_pending()