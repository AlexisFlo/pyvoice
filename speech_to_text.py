import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
  # Loop in case of errors
  while(1):
    try:
      # use the mircrophone as source for input
      with sr.Microphone() as source2:
        # Prepare recognizer to receive input
        r.adjust_for_ambient_noise(source2, duration=0.2)

        # linsten for the user's input
        audio2= r.listen(source2)

        # Using google to recognize audio
        MyText = r.recognize_google_cloud(audio2, language="es-ES")

        return MyText

    except sr.RequestError as e:
      print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
      print("unknow error ocurred")

  return

def output_text(text):
  f = open("output.txt", "a")
  f.write(text)
  f.write("\n")
  f.close()
  return

while():
  text = record_text()
  output_text(text)

  print("Wrote text")