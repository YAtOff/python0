"""
Преди да стартирате инсталирайте:
pip install SpeechRecognition
pip install https://github.com/intxcc/pyaudio_portaudio/releases/download/1.1.1/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl

Повече информация тук: https://realpython.com/python-speech-recognition/
"""

import speech_recognition as sr


recognizer = sr.Recognizer()
with sr.AudioFile("OSR_us_000_0010_8k.wav") as source:
    audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    print(text)
