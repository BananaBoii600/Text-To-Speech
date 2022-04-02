from tkinter import *
import pyttsx3


# tkinter window settings
root = Tk()
root.title("Text To Speech")
root.geometry("800x300")


# Functions
def voice():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0, END)

# Title Label
text_to_speech_label = Label(root, text="Text To Speech", font=("Helvetica", 30))
text_to_speech_label.pack(pady=20)

# The typeable area where the user enters the sentence that should be spoken
entry = Entry(root, font=("Helvetica", 28))
entry.pack(pady=20)

# Button which speaks the sentence typed in the entry
voice_btn = Button(root, text="Speak", command=voice)
voice_btn.pack(pady=5)

root.mainloop()
