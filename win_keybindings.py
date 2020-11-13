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
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('v')

    def send_chat_message(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('h')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('h')

    def quick_message(self, message):
        self.type_chat_message(message)
        self.send_chat_message()

    def raise_lower_hand(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('y')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('y')
    
    def start_stop_local_recording(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('r')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('r')

    def pause_resume_recording(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('p')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('p')

    def share_stop_screen(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('s')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('s')

    def read_speaker_name(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('2')
        self.keyboard.release(Key.ctrl)
        self.keyboard.release('2')

    def switch_camera(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press('n')
        self.keyboard.release(Key.alt_l)
        self.keyboard.release('n')