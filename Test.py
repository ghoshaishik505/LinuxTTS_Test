

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
choice = input("Choose the voice index\n")
engine.setProperty('voice', voices[int(choice)].id)
engine.say("जी हाँ, आप बजाज के लोन के लिए आवेदन कर सकते हैं। कृपया बताएं कि आप किस तरह के लोन के लिए आवेदन करना चाहते हैं?")
engine.runAndWait()