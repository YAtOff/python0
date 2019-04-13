"""
Преди да стартирате инсталирайте:
pip install pyttsx3
pip install pywin32
"""

import pyttsx3


engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
