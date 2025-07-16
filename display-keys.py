from tkinter import *
from pynput import keyboard
import threading

key_history = []

def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key).replace('Key.', '')

    key_history.append(key_name)
    if len(key_history) > 3:
        key_history.clear()

    combined = '+'.join(key_history)
    label.config(text=combined)

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

root = Tk()
root.title("Display keys")
root.geometry("400x100")
root.attributes("-topmost", True)

label = Label(root, font=("Helvetica", 30))
label.pack()

listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

root.mainloop()
