import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as source:
  print("Say somethings: ")
  audio = listener.listen(source)

try:
  text = listener.recognize_google(audio)
  print(f"You said: {text}")
except sr.UnknownValueError:
  print("Can't understand audio")
except sr.RequestError as e:
  print(f"Could not request results: {e}")