import speech_recognition

r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    audio = r.listen(source)

r.recognize_bing(audio, language='zh-TW')