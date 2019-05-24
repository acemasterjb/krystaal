import os
import tkinter
import tkinter.filedialog
import mutagen
from mutagen.flac import FLAC


# Make and hide a GUI interface that will house the directory chooser
root = tkinter.Tk()
root.withdraw()

# 1) Get the current directory the file was opened from.
# 2) Choose a directory to function from.
# 3) Change the current directory to the one chossen in step 2.
# 4) Make a list of the song files and store them in a variable.
currDir = os.getcwd()
getDir = tkinter.filedialog.askdirectory(
    parent=root, initialdir=currDir, title="Pick song library...")

os.chdir(getDir)

songs = os.listdir(getDir)


# Change the name of every .flac in the list of songs
# based on "genre - artist - album - tracknumber - title"
for s in songs:
    if s.endswith('.flac'):
        songObject = mutagen.File(s)

        newname = songObject['genre'].pop() + ' - '
        newname += songObject['artist'].pop() + ' - '
        newname += songObject['album'].pop() + ' - '
        newname += songObject['tracknumber'].pop() + ' - '
        newname += songObject['title'].pop() + '.flac'

        song = FLAC(s)

        song.delete()
        song.save()
        os.rename(s, newname)
