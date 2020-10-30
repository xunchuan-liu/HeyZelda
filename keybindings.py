from pynput.keyboard import Key, Controller

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