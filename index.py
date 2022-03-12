import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
import os
import psutil
from pygame import mixer
import sys, time
import socket
from config import TOKEN
from pprint import pprint


#COLOR
def greenSquare():
    return u'\U00002705'
def redSquare():
    return u'\U0000274C'

#INFO
def user_id():
    return "Your Telegram ID"
    

#CHECK PROCESS
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

#CONNECTION
def waitForInternetConnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False



# NOTEPAD
def killNotepad(): 
    if(notepadRunning()):
        os.system("taskkill /f /im notepad.exe")
def notepadRunning():
    return checkIfProcessRunning("notepad.exe")

# DISCORD
def killDiscord(): 
    if(discordRunning()):
        os.system("taskkill /f /im DiscordCanary.exe")
def discordRunning():
    return checkIfProcessRunning("DiscordCanary.exe")
    

#SHUTDOWN
def shutdownPc():
    os.system('shutdown -s -t 0')
#RESTART
def restartPc():
    os.system("shutdown /r")
#SLEEP
def sleepPc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


#UPDATE USER
def updateUser():
# Notepad
    if(notepadRunning()):
        bot.sendMessage(user_id(), "FL" + greenSquare)
    else:
        bot.sendMessage(user_id(), "FL" + redSquare)
# Discord
    if(discordRunning()):
        bot.sendMessage(user_id(), "FL" + greenSquare)
    else:
        bot.sendMessage(user_id(), "FL" + redSquare)



#HANDLE
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    text = msg['text'].upper()

    if not (chat_id == 413318410):
        bot.sendMessage(chat_id, "CHI CAZZO SEI PORCODIO")
        bot.sendMessage(user_id(), 'Qualcuno mi ha contattato:\n' + chat_id)

    if(text == 'SHUTDOWN' or text == 'SD'):
        bot.sendMessage(user_id(), "PC Spento, arrivederci!")
        shutdownPc()
    if(text == 'RESTART' or text == 'R'):
        bot.sendMessage(user_id(), "Restart avviato")
        restartPc()
    if(text == 'SLEEP' or text == 'S'):
        bot.sendMessage(user_id(), "PC a mimir")
        sleepPc()
    if(text == 'DISCORD' or text == 'DS'):
        bot.sendMessage(user_id(), "discord.exe chiuso")
        shutdownPc()
    if(text == 'NOTEPAD' or text == 'NP'):
        bot.sendMessage(user_id(), "notepad.exe chiuso")
        killNotepad()
    

    





#OTHERS
time.sleep(20)
waitForInternetConnection()
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
while 1:
    time.sleep(3)
