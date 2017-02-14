import git
import subprocess
import tempfile
import os
from Tkinter import *

class Updater(Frame):
    def createWidgets(self):
        self.LOAD = Button(self)
        self.LOAD["text"] = "Load Firmware"
        self.LOAD["command"] = self.main
        self.LOAD.pack({"side":"left"})
    def __init__(self, master=None):
        self.DIR_NAME = ""
        self.DIR_PATH = ""

        self.REPO_NAME = "HuskieBoardPublic"
        self.REPO_PATH = "https://github.com/bennettjohnson/HuskieBoardPublic.git"
        self.REPO = None

        self.origin = None
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def mkTempDir(self):
        self.DIR_PATH = tempfile.mkdtemp("", self.REPO_NAME)
        self.DIR_NAME = os.path.basename(os.path.normpath(self.DIR_PATH))
        print self.DIR_NAME
        print self.DIR_PATH
        
    def repoConfig(self):
        self.REPO = git.Repo.init(self.DIR_PATH)
        self.origin = self.REPO.create_remote('master', self.REPO_PATH)

    def download(self):
        print "Downloading: " + self.REPO_NAME + " into: " + self.DIR_PATH
        self.origin.fetch()
        self.origin.pull("master")
        print "done"
    def loadBoard(self):
        print "loading board"
        subprocess.call([self.DIR_PATH + "\\propeller firmware\\bin\\proploader.exe",self.DIR_PATH + "\\propeller firmware\\bin\\main.binary", "-s"])
        print "done"
    def main(self):
        self.mkTempDir()
        self.repoConfig()
        self.download()
        self.loadBoard()
root = Tk()
updater = Updater(master=root)
updater.mainloop()
root.destroy()
