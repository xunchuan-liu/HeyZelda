from win_keybindings import Keybinding

class TextInterpreter:
    def __init__(self, transcription):
        self.transcription = transcription
        self.trigger = "Zelda"
        self.commands = {
            0: "turn off microphone",
            1: "turn on microphone",
            2: "turn off video",
            3: "turn on video",
            4: "type message",
            5: "send message"
        }
    
    #interpret what the audio command is and return a command
    def interpret_text(self):
        if self.trigger in self.transcription:
            if self.commands[0] in self.transcription:
                self.simulate_keypress(0)
                mic_status = 0
            elif self.commands[1] in self.transcription:
                self.simulate_keypress(1)
                mic_status = 1
            elif self.commands[2] in self.transcription:
                self.simulate_keypress(2)
                vid_status = 0
            elif self.commands[3] in self.transcription:
                self.simulate_keypress(3)
                vid_status = 1
            elif self.commands[4] in self.transcription:
                self.simulate_keypress(4)
            elif self.commands[5] in self.transcription:
                self.simulate_keypress(5)
            else:
                return
        else:
            return

    #Based on command, simulate the key press
    def simulate_keypress(self, command):
        keyboard = Keybinding()
        if command == 0:# and mic_status == 1:
            print("muting")
            keyboard.enable_disable_mic()
        if command == 1:# and mic_status == 0:
            print("unmuting")
            keyboard.enable_disable_mic()
        elif command == 2:# and vid_status == 1:
            keyboard.enable_disable_vid()
            print("turning off video")
        elif command == 3:# and vid_status == 0:
            keyboard.enable_disable_vid()
            print("turning on video")
        elif command == 4:
            message = self.transcription.split(self.trigger + " " + self.commands[4])[1].strip()
            keyboard.type_chat_message(message)
        elif command == 5:
            keyboard.send_chat_message()
        else:
            return