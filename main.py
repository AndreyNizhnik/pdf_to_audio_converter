import pyttsx3
import PyPDF4
from tkinter import *
from tkinter import filedialog

pdf_reader = ""


def open_pdf():
    global pdf_reader
    pdf_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select PDF",
        filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
    )
    # creating a PdfFileReader object
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)


def play_pdf_audio():
    global pdf_reader
    # this will read the pages in given range (from start).
    from_page = pdf_reader.getPage(int(pages.get()))
    # extracting the text from the PDF
    text = from_page.extractText()
    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()


# def open_file():
#     os.startfile('pdf-audio.mp3')


window = Tk()
window.title('PDF to Audio Converter -- v1.012')
window.config(padx=25, pady=25, background="light green")
window.wm_minsize(width=400, height=380)

button_open = Button(text="Select PDF File", font=("Arial", 20, "normal"), width=30, command=open_pdf)
button_open.grid(column=0, row=0, padx=25, pady=25)

pages = Entry(width=30, font=("Arial", 20, "normal"), fg="grey")
pages.insert(0, "  Enter number of pages starting from 0.",)
pages.grid(column=0, row=2, padx=25, pady=25, ipadx=20, ipady=5)

button_save = Button(text="Play Pages", font=("Arial", 20, "normal"), width=30, command=play_pdf_audio)
button_save.grid(column=0, row=3, padx=25, pady=25)

window.mainloop()
