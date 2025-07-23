import keyboard
import pyttsx3
from PyPDF2 import PdfReader
import time


def getalline(path):
    reader = PdfReader(path)
    pages = reader.pages
    return pages


def speaking(line):
    if not line.strip():
        return
    print(f"{line}  {len(line)}")

    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.say(line)
    engine.runAndWait()
    engine.stop()


def readlines(pages):
    for page in pages:
        speaking(page.extract_text())


fpath = "C:/Users/user/OneDrive/Documents/Article How to choose an international school.pdf"
ftext = getalline(fpath)
readlines(ftext)
time.sleep(600)
