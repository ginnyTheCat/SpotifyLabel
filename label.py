import eyed3
from shutil import copyfile
import os
import glob

FILE_NAME = "audio.mp3"
DIR_NAME = "Labels"

tag = eyed3.load(FILE_NAME).tag
counter = 0

name = None
while name is None or name != "":
    name = input("Name: ")
    tag.title = name

    tag.save()
    copyfile(FILE_NAME, DIR_NAME + "/" + str(counter) + ".mp3")
    counter += 1

files = glob.glob(DIR_NAME + "/*")
for f in files:
    os.remove(f)