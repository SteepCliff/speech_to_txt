# -- coding: utf-8 --
__author__ = "SteepCliff"
__email__ = "s.steepcliff@gmail.com"
__licence__ = "GPL v.3"

import speech_recognition as sr

recognizer_test = sr.Recognizer()

file_audio_sample = sr.AudioFile('./static/sample.wav')
with file_audio_sample as source:
    audio_sample = recognizer_test.record(source) 

output = recognizer_test.recognize_google(audio_sample) 
print(output)
