import speech_recognition as sr

# Create a speech recognizer object
r = sr.Recognizer()

# Start speech recognition
with sr.Microphone() as source:
    audio = r.listen(source)

# Transcribe the audio
try:
    text = r.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Could not recognize speech")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
