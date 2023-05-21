import time
from win10toast import ToastNotifier
import win32com.client
import winsound
import random

reminderCount = int(input("Enter the number of reminders: "))
afterCertainDuration = int(input("Enter the reminder interval in seconds: "))
typeOfReminder = input(
    '''Types of Reminder:
    ----------------------
    Beep Sound -> S
    Notification -> N
    Voice -> V

    Choose a reminder type: ''')

def drink_water_reminder_notification(iterations):
    # Display desktop notifications
    toaster = ToastNotifier()
    for _ in range(iterations):
        toaster.show_toast("Drink Water Reminder", "Remember to drink water!")
        time.sleep(afterCertainDuration) # Delay in seconds

def drink_water_reminder_voice(iterations):
    # Use voice reminders
    messages = [
        "Remember to drink water regularly!",
        "Stay hydrated by drinking enough water!",
        "It's time for a water break!",
        "Hydrate yourself with some refreshing water!",
        "Don't forget to keep yourself hydrated!"
    ]
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for _ in range(iterations):
        message = random.choice(messages) # Choose a random message from the list
        speaker.Speak(message)
        time.sleep(afterCertainDuration) # Delay in seconds

def drink_water_reminder_sound(iterations):
    # Play beep sound reminders
    frequency = 2500  
    duration = 1000  
    for _ in range(iterations):
        winsound.Beep(frequency, duration)
        time.sleep(afterCertainDuration) # Delay in seconds

# Choose the appropriate reminder type
if typeOfReminder == "V":
    drink_water_reminder_voice(reminderCount)
elif typeOfReminder == "S":
    drink_water_reminder_sound(reminderCount)
elif typeOfReminder == "N":
    drink_water_reminder_notification(reminderCount)
else:
    print("You entered an invalid reminder type.")