# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:44:45 2020

@author: K Chidananda Adiga
"""

import speech_recognition as s
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3 as pp   #for audio
import threading

from tkinter import *

root = Tk()

engine=pp.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

#function for the bot to speak
def speak(word):
    engine.say(word)
    engine.runAndWait()

# takes audio as input and converts it to string
def take_audio():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print('Your bot is listening...')
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            e.delete(0, END)
            e.insert(0, query)
            sendq()
        except Exception as ex:
            print(ex)


def sendq():
    send = e.get()  # message from input entry given by the user
    txt.insert(END, "\nYou: " + send)  # message printed to the text area
    if (send == 'Bye' or send == 'bye'):
        reply = 'Nice Talking to you.Bye'
        txt.insert(END, '\n{}: {}'.format(bot.name, reply))
        speak(reply)
        e.delete(0, END)  # delete the input given by user after send button is pressed so that next input can be given.

    if (send != 'Bye' or send != 'bye'):
        reply = bot.get_response(send)  # response from the dataset fed
        txt.insert(END, '\n{}: {}'.format(bot.name, reply))
        speak(reply)
        e.delete(0, END)
    txt.yview(END)

    # Define Chatbot with a name


bot = ChatBot('Siri')

# set the trainer algorithm
bot.set_trainer(ChatterBotCorpusTrainer)

# training the chatbot on the data
# data : chatterbot/corpus/english
bot.train('chatterbot.corpus.english')

# title of the interface
root.title('CHATBOT')



# text area where the display is shown
txt = Text(root, bg='light blue')
txt.grid(columnspan=2)

scrollbar = Scrollbar(root, command=txt.yview)
scrollbar.place(x=630, y=4, height=385)

# input area where the user gives input
e = Entry(root, width=100)
e.grid(row=1, column=0)

# button to send the input.
send = Button(root, text="SEND", width=5, command=sendq, bg='light pink')
send.grid(row=1, column=1)



#function for invoking the button if enter key is pressed
def enter_fuction(event):
    send.invoke()

#bind root window with enter key
root.bind('<Return>',enter_fuction)

# to listen to audio continuously
def repeatl():
    while True:
        take_audio()


t = threading.Thread(target=repeatl)  # defined a thread so that both speech recognition and UI is shown simultaneously.
t.start()

root.mainloop()




