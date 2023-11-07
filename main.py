import gtts
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf")])

reader = PdfReader(file_path)
text = ""

for page in reader.pages:
    text += f"\n{page.extract_text()}"

tts = gtts.gTTS(text,lang="en")
tts.save("audio.mp3")
