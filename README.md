# HeyZoom

### *Introducing your personal Zoom meeting assistant:*

![Zelda](/img/title.jpg)

A program for users to control Zoom meeting functionality with their voice. 

CS 338 Final Project - **Speech Based Control of Zoom**

> #### Project Theme
> Improving popular remote collaboration tools to facilitate virtual teamwork during the Coronavirus pandemic.

&nbsp;

## Contributors
- Aaron Keller (*aaronkeller2021@u.northwestern.edu*)
- Paulina Tarasul (*paulinatarasul2022@u.northwestern.edu*)
- Xunchuan Liu  (*xunchuanliu2021@u.northwestern.edu*)
- Zixuan Zhu (*zixuanzhu2021@u.northwestern.edu*)

## Demo 

Watch our demo video!

https://youtu.be/6g9BPz0VuhE

You can also check out an offshoot project I developed for the web.

https://github.com/xunchuan-liu/Zelda

If you're curious to try it out, follow the instructions below to get up and running with **Zelda**.

&nbsp;

## Requirements 
You will need:
- Python (*at least version 3*)
- Python package manager *i.e. `pip`*
- Command Line Tool that can run Python
- A working microphone input device

## Installation and Setup

> **Find your Python version using the command line:**
 
`python -V` (*notice capital **V***)

You will need the version number, *i.e. 3.8.1*, for the next step. 

&nbsp;

> **Download the compatible `.whl` file.** 

This file is necessary to make **`PyAudio`** work with audio inputs.

1. Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio 
2. Find the file that matches your python version number. \
*To match the file with your version number, look at the numbers after the letters **cp** in the file name.* \
*For instance:*
    - *Python 3.7 ==> PyAudio-0.2.11-cp**37**-cp**37**-win_amd64l.whl* 
    - *Python 3.5 ==> PyAudio-0.2.11-cp**35**-cp**35**-win_amd64l.whl*
3. Download the file to your local desktop. 

&nbsp;
 
> **Install the `.whl` file.**
 
Navigate to the folder with the downloaded file. With the command line, use your python package manager to install it. Example with `pip`:

`pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl`

&nbsp;

> **Make a local copy of this repo to begin working:** 

`git clone https://github.com/xunchuan-liu/HeyZoom`

&nbsp;

> **Install the necessary modules from `requirements.txt`.**

Navigate to the cloned repository. Run this on command line with your Python package manager, *i.e. with `pip`*:

`pip install -r requirements.txt`

***Note**: You can create a virtual env for this project if you would like.*

The following modules will be installed:
- [**SpeechRecognition**](https://pypi.org/project/SpeechRecognition/)
- [**pynput**](https://pypi.org/project/pynput/)
- [**pyperclip**](https://pypi.org/project/pyperclip/)



#### You are now setup in a working local copy of this project. Follow the instructions under **Usage** to run a test of the program.

&nbsp;

## Usage
Using the command line or an IDE like **pycharm**, run the `heyzoom.py` file with **python**. Be sure you are in the root directory of the cloned repo.  

Example running with command line:

`python heyzoom.py` 

This starts the main speech recognition loop. Begin speaking and the program should pick up what you're saying. 

You will see an output like this:
 
![Demo of speech recognition](/img/demo.jpg)

### With Zoom
You can now start a Zoom meeting and have this program running in the background. You can begin issuing commands to control the meeting. 

For instance, try:
- **Zelda turn off microphone**
- **Zelda turn on video**

> Remember to start with **Zelda** as a trigger word, otherwise the program won't react!

&nbsp;

## Reference - Zelda Commands
- type message
- send message
- close window
- switch to portrait view
- switch to landscape view
- switch tab
- join meeting
- start meeting
- schedule meeting
- screen share using direct share
- mute mic
- unmute mic
- turn on microphone
- turn off microphone
- mute everyone
- unmute everyone
- turn on video
- turn off video
- switch camera
- start screen share
- stop screen share
- pause screen share
- resume screen share
- start local recording
- start cloud recording
- pause recording
- resume recording
- switch to active speaker view
- switch to gallery view
- view previous participants
- display participants panel
- hide participants panel
- show in-meeting chat panel
- hide in-meeting chat panel
- open invite window
- raise hand
- lower hand
- gain remote control
- stop remote control
- enter full screen
- exit full screen
- switch to minimal window
- show meeting controls
- hide meeting controls
- toggle meeting controls option
- end meeting
- leave meeting
- jump to chat
- screenshot
- call highlighted phone number
- accept inbound call
- decline inbound call
- end current call
- hold call
- unhold call 
