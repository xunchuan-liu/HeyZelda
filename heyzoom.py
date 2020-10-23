import speech_recognition as sr
from pynput.keyboard import Key, Controller
import re
#%%
'''
   // Voice Recognition (Speech-to-Text) - Google Speech Recognition API
   -> This API converts spoken text (microphone) into written text (Python strings)
   -> Personal or testing purposes only
   -> Generic key is given by default (it may be revoked by Google at any time)
   -> If using API key, quota for your own key is 50 requests per day
'''

commands = {
    0: "turn off microphone",
    1: "turn on microphone",
    2: "turn off video",
    3: "turn on video",
}
#%%

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #   update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

#%%

#interpret what the audio command is and return a command (string)
def interpret_text(transcription):
    if commands[0] in transcription:
        simulate_keypress(0)
        mic_status = 0
    elif commands[1] in transcription:
        simulate_keypress(1)
        mic_status = 1
    elif commands[2] in transcription:
        simulate_keypress(2)
        vid_status = 0
    elif commands[3] in transcription:
        simulate_keypress(3)
        vid_status = 1
    else:
        return

#Based on command, look up appropriate key-binding in dictionary and simulate the key press
def simulate_keypress(command):
    keyboard = Controller()
    if command == 0:# and mic_status == 1:
        print("muting")
        keyboard.press(Key.alt_l)
        keyboard.press('a')
        keyboard.release(Key.alt_l)
        keyboard.release('a')
    if command == 1:# and mic_status == 0:
        print("unmuting")
        keyboard.press(Key.alt_l)
        keyboard.press('a')
        keyboard.release(Key.alt_l)
        keyboard.release('a')
    elif command == 2:# and vid_status == 1:
        keyboard.press(Key.alt_l)
        keyboard.press('v')
        keyboard.release(Key.alt_l)
        keyboard.release('v')
        print("turning off video")
    elif command == 3:# and vid_status == 0:
        keyboard.press(Key.alt_l)
        keyboard.press('v')
        keyboard.release(Key.alt_l)
        keyboard.release('v')
        print("turning on video")
    else:
        return

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    while True:
        response = recognize_speech_from_mic(recognizer, mic)
        print('\nSuccess : {}\nError   : {}\n\nText from Speech\n{}\n\n{}' \
            .format(response['success'],
                    response['error'],
                    '-'*17,
                    response['transcription']))
        if response['transcription'] == None:
            continue
        else:
            interpret_text(response['transcription'].strip())
# %%
