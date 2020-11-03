# HeyZoom

### Introducing your personal Zoom assistant: ***Zelda***

&nbsp;


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
    - *Python 3.7 ==> PyAudio-0.2.11-cp****37**-cp****37**-win_amd64l.whl* 
    - *Python 3.5 ==> PyAudio-0.2.11-cp****35**-cp****35**-win_amd64l.whl*
3. Download the file to your local desktop. 

&nbsp;
 
> **Install the `.whl` file.**
 
Navigate to the folder with the downloaded file. Use your python package manager to install it. Example with `pip`:

`pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl`

&nbsp;

> **Make a local copy of this repo to begin working:** 

`git clone https://github.com/akeller98/HeyZoom`

&nbsp;

> **Install the necessary modules from `requirements.txt`.**

Navigate to the cloned repository. Run this command with your Python package manager, *i.e. with `pip`*:

`pip install -r requirements.txt`

***Note**: You can create a virtual env for this project if you would like.*

The following modules will be installed:
- [**SpeechRecognition**](https://pypi.org/project/SpeechRecognition/)
- [**pynput**](https://pypi.org/project/pynput/)
- [**pyperclip**](https://pypi.org/project/pyperclip/)



#### You are now setup in a working local copy of this project. Follow the instructions under **Usage** to run a test of the program.

&nbsp;

## Usage
Using command line or an IDE like **pycharm**, run the `heyzoom.py` file. Be sure you are in the root directory of the cloned repo.  

Example running with command line:

`python heyzoom.py` 

This starts the main speech recognition loop. Speak into your microphone and see if the program can pick up what you're saying. 
