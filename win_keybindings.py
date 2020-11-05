from pynput.keyboard import Key, Controller
import pyperclip

class Keybinding:
    def __init__(self):
        self.keyboard = Controller()
    
    def enable_disable_mic(self):
        print("muting")
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('a')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('a')
    
    def enable_disable_vid(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('v')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('v')

    def type_chat_message(self, message):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('h')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('h')
        pyperclip.copy(message)
        #pyperclip.paste()
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('v')

    def send_chat_message(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)