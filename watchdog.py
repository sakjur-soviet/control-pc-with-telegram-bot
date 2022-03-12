# IMPORTANT
# This code is ugly. It just had to work. You can make it better.
# I made this telegram bot to prank my brother (https://www.youtube.com/watch?v=BOkSupPtWCQ)
# I changed some parts to ********************** for privacy reasons
# If you know a little bit of coding you will realize it's an extremely easy program. If you don't know coding learn it and then come back.




import telepot
import os
import psutil
from pygame import mixer
import time
import socket
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup

def greenSquare():
    return u'\U00002705'
def redSquare():
    return u'\U0000274C'
def playGlitch():
    mixer.init()
    mixer.music.load('C:\dev\watchdog\sound.mp3')
    mixer.music.play()
def davidId():
    return "**********************"
def davidUsername():
    return "**********************"
def botToken():
    return "**********************"

def notifyTelegramPoint():
    bot.sendMessage(davidId(), '.')

def waitForInternetConnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def killFortnite(): #kill fortnite process
    if(fortniteRunning()):
        os.system("taskkill /f /im FortniteClient-Win64-Shipping.exe")
def fortniteRunning():
    return checkIfProcessRunning("FortniteClient-Win64-Shipping.exe")


def killFortniteLauncher(): #kill fortnite launcher process
    if(fortniteLauncherRunning()):
        os.system("taskkill /f /im EpicGamesLauncher.exe")
def fortniteLauncherRunning():
    return checkIfProcessRunning("EpicGamesLauncher.exe")


def killTelegram():
    if(telegramRunning()):
        os.system("taskkill /f /im Telegram.exe")
def telegramRunning():
    return checkIfProcessRunning("Telegram.exe")


def killDiscord():
    if(discordRunning()):
        os.system("taskkill /f /im Discord.exe")
def discordRunning():
    return checkIfProcessRunning("Discord.exe")


def apexRunning():
    return checkIfProcessRunning("r5apex.exe")
def killApex():
    if(apexRunning()):
        os.system("taskkill /f /im r5apex.exe")


def killAll():
    killFortniteLauncher()
    killFortnite()
    killTelegram()
    killDiscord()
    killApex()


def updateUser():
    killTelegram() #prevent user seeing message on desktop

    if(fortniteLauncherRunning()):
        bot.sendMessage(davidId(), "FL" + greenSquare())
    else:
        bot.sendMessage(davidId(), "FL" + redSquare())

    if (fortniteRunning()):
        bot.sendMessage(davidId(), "F" + greenSquare())
    else:
        bot.sendMessage(davidId(), "F" + redSquare())

    if (discordRunning()):
        bot.sendMessage(davidId(), "D" + greenSquare())
    else:
        bot.sendMessage(davidId(), "D" + redSquare())

    if(apexRunning()):
        bot.sendMessage(davidId(), "A" + greenSquare())
    else:
        bot.sendMessage(davidId(), "A" + redSquare())

def shutdownPc():
    os.system('shutdown -s -t 0')

def handle(msg): #what to do if new message is received
    contentType, chatType, chatId = telepot.glance(msg)
    text = msg['text'].upper()
    if not (chatId == 7876786786):
        bot.sendMessage(chatId, "WHO ARE YOU?! I WILL TELL MY MASTER")
        bot.sendMessage(davidId(), 'Someone contacted me! Here is the information:\n' + msg)
    elif(text == 'KILL' or text == 'KILLALL' or text == 'KILL ALL' or text == 'KA'):
        killAll()
        notifyTelegramPoint()
    elif(text == 'KILL FORTNITE' or text == 'KF' or text == 'K'):
        killTelegram()
        killFortnite()
        killFortniteLauncher()
        notifyTelegramPoint()
    elif(text == 'UPDATE' or text == 'U'):
        updateUser()
    elif (text == '/START'):
        bot.sendMessage(davidId(), "Welcome back Master", reply_markup=keyboard)
    elif(text == 'SHUTDOWN'):
        bot.sendMessage(davidId(), "Shutting down. Bye Bye")
        shutdownPc()
    elif(text == 'KILL ALL WITH REACTION' or text == 'KAWR'):
        killAll()
        notifyTelegramPoint()
        bot.sendMessage(davidId(), "Reaction still not implemented")
    elif(text == 'KIM'):
        time.sleep(60)
        killAll()
        notifyTelegramPoint()
    elif(text == 'KITENS'):
        time.sleep(10)
        killAll()
        notifyTelegramPoint()
    elif(text == 'S'):
        playGlitch()
        notifyTelegramPoint()
    else:
        bot.sendMessage(davidId(), "I don't understand...", reply_markup=keyboard)

time.sleep(120)
waitForInternetConnection()
bot = telepot.Bot(botToken())
MessageLoop(bot, handle).run_as_thread()
keyboard = ReplyKeyboardMarkup(keyboard=[['KA', 'U'], ['KF', 'KAWR'], ['KIM', 'KITENS']])
bot.sendMessage(davidId(), 'wO.Ow', reply_markup=keyboard)
while 1:
    time.sleep(10)