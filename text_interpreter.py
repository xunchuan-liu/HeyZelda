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
            13: "read speaker name",
            14: "switch camera"
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
            13: self.keyboard.read_speaker_name,
            14: self.keypress.switch_camera
        }
    
    #interpret what the audio command is and return a command
    def interpret_text(self):
        if self.trigger in self.transcription:
            selected_command = ''
            for command in self.commands:
                if self.commands[command] in self.transcription:
                    selected_command = command
                    self.simulate_keypress(selected_command)
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