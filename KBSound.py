import threading
import random
from pynput.keyboard import Key, Listener
import wx
import wx.adv


class KBSoundThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.onPress = None
        self.onRelease = None

    def run(self):
        with Listener(
                on_press=self.onPress,
                on_release=self.onRelease) as listener:
            listener.join()


class KBSound:
    def __init__(self):
        self.running = False
        self.randomized = False
        self.soundArray = []
        self.counter = 0

    def onPress(self, key):
        self.playSound()
        return self.running

    def onRelease(self, key):
        return self.running

    def addSound(self, path):
        self.soundArray.append(wx.adv.Sound(path))

    def startService(self):
        if len(self.soundArray) <= 0:
            return

        self.running = True

        thr = KBSoundThread()
        thr.onPress = self.onPress
        thr.onRelease = self.onRelease

        thr.start()

    def stopService(self):
        self.running = False

    def nextSound(self):
        if len(self.soundArray) <= 0:
            return

        nxs = self.soundArray[self.counter]
        self.counter += 1
        if self.counter >= len(self.soundArray):
            self.counter = 0
        return nxs

    def nextRandomSound(self):
        if len(self.soundArray) <= 0:
            return

        return random.choice(self.soundArray)

    def playSound(self):
        if len(self.soundArray) <= 0:
            return

        sndToplay = None
        if self.randomized == True:
            sndToplay = self.nextRandomSound()
        else:
            sndToplay = self.nextSound()

        sndToplay.Play(wx.adv.SOUND_ASYNC)
