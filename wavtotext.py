import speech_recognition as sr
from os import path
from pydub import AudioSegment

filename = "test.wav"
file = open("text.txt", "w+")
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    file.write(text)

file.close()