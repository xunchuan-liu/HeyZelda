from win_keybindings import Keybinding

class TextInterpreter:
    def __init__(self, transcription):
        self.transcription = transcription
        self.trigger = "Zelda"
        self.keyboard = Keybinding()
        self.commands = {
            0: "turn off microphone",
            1: "turn on microphone",
            2: "turn off video",
            3: "turn on video",
            4: "type message",
            5: "send message",
            6: "quick message",
            7: "raise hand",
            8: "lower hand",
            9: "start local recording",
            10: "stop_local_recording",
            11: "share screen",
            12: "stop screen sharing",
            13: "read speaker name"
        }
        self.keypress_switch = {
            0: self.keyboard.enable_disable_mic,
            1: self.keyboard.enable_disable_mic,
            2: self.keyboard.enable_disable_vid,
            3: self.keyboard.enable_disable_vid,
            4: self.type_message,
            5: self.keyboard.send_chat_message,
            6: self.quick_message,
            7: self.keyboard.raise_lower_hand,
            8: self.keyboard.raise_lower_hand,
            9: self.keyboard.start_stop_local_recording,
            10: self.keyboard.start_stop_local_recording,
            11: self.keyboard.share_stop_screen,
            12: self.keyboard.share_stop_screen,
            13: self.keyboard.read_speaker_name
        }
    
    #interpret what the audio command is and return a command
    def interpret_text(self):
        if self.trigger in self.transcription:
            if self.commands[0] in self.transcription:
                self.simulate_keypress(0)
                #mic_status = 0
            elif self.commands[1] in self.transcription:
                self.simulate_keypress(1)
                #mic_status = 1
            elif self.commands[2] in self.transcription:
                self.simulate_keypress(2)
                #vid_status = 0
            elif self.commands[3] in self.transcription:
                self.simulate_keypress(3)
                #vid_status = 1
            elif self.commands[4] in self.transcription:
                self.simulate_keypress(4)
            elif self.commands[5] in self.transcription:
                self.simulate_keypress(5)
            elif self.commands[6] in self.transcription:
                self.simulate_keypress(6)
            elif self.commands[7] in self.transcription:
                self.simulate_keypress(7)
            elif self.commands[8] in self.transcription:
                self.simulate_keypress(8)
            elif self.commands[9] in self.transcription:
                self.simulate_keypress(9)
            elif self.commands[10] in self.transcription:
                self.simulate_keypress(10)
            elif self.commands[11] in self.transcription:
                self.simulate_keypress(11)
            elif self.commands[12] in self.transcription:
                self.simulate_keypress(12)
            elif self.commands[13] in self.transcription:
                self.simulate_keypress(13)
            else:
                return
        else:
            return

    #Based on command, simulate the key press
    def simulate_keypress(self, command):
        self.keypress_switch[command]()
    
    #Helper functions
    def type_message(self):
        message = self.transcription.split(self.trigger + " " + self.commands[4])[1].strip()
        self.keyboard.type_chat_message(message)
    
    def quick_message(self):
        message = self.transcription.split(self.trigger + " " + self.commands[6])[1].strip()
        self.keyboard.quick_message(message)