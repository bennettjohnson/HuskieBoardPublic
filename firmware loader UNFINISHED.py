import git
import subprocess
import tempfile
import os

class Updater(object):
    def __init__(self):
        self.DIR_NAME = ""
        self.DIR_PATH = ""

        self.REPO_NAME = "HuskieBoardPublic"
        self.REPO_PATH = "https://github.com/bennettjohnson/HuskieBoardPublic.git"
        self.REPO = None

        self.origin = None

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
def main():
    updater = Updater()
    updater.mkTempDir()
    updater.repoConfig()
    updater.download()
    updater.loadBoard()
main()
