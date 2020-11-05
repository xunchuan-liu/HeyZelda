from keybindings import Keybinding

class TextInterpreter:
    def __init__(self, transcription):
        self.transcription = transcription
        self.trigger = "Zelda"
        self.commands = {
            0: "type message",
            1: "send message",
            2: "close window",
            3: "switch to portrait view",
            4: "switch to landscape view",
            5: "switch tab",
            6: "join meeting",
            7: "start meeting",
            8: "schedule meeting",
            9: "screen share using direct share",
            10: "turn on microphone",
            11: "turn off microphone",
            12: "mute everyone",
            13: "unmute everyone",
            14: "turn on video",
            15: "turn off video",
            16: "switch camera",
            17: "start screen share",
            18: "stop screen share",
            19: "pause screen share",
            20: "resume screen share",
            21: "start local recording",
            22: "start cloud recording",
            23: "pause recording",
            24: "resume recording",
            25: "Switch to active speaker view",
            26: "Switch to gallery view",
            27: "View previous participants",
            28: "View next participants",
            29: "display participants panel",
            30: "hide participants panel",
            31: "show in-meeting chat panel",
            32: "hide in-meeting chat panel",
            33: "open invite window",
            34: "raise hand",
            35: "lower hand",
            36: "gain remote control",
            37: "stop remote control",
            38: "enter full screen",
            39: "exit full screen",
            40: "switch to minimal window",
            41: "show meeting controls",
            42: "hide meeting controls",
            43: "toggle meeting controls option",
            44: "end meeting",
            45: "leave meeting",
            46: "jump to chat",
            47: "screenshot",
            48: "call highlighted phone number",
            49: "accept inbound call",
            50: "decline inbound call",
            51: "End current call",
            52: "mute mic",
            53: "unmute mic",
            54: "hold call",
            55: "unhold call"
        }

    #interpret what the audio command is and return a command
    def interpret_text(self):
        if self.trigger in self.transcription:
            for i in range(len(self.commands)):
                if self.commands[i] in self.transcription:
                    print("Begin:", self.commands[i])
                    self.simulate_keypress(i)
                    return
            return

    #Based on command, simulate the key press
    def simulate_keypress(self, command):
        keyboard = Keybinding()
        if command == 0:
            message = self.transcription.split(self.trigger + " " + self.commands[0])[1].strip()
            keyboard.t0(message)
        else: 
            keyboard.func_name(command)
            