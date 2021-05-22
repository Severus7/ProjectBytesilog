from tkinter import *
from tkinter import filedialog
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collections import Counter
import matplotlib.pyplot as plt
import pyttsx3 as p

root = Tk()
root.title('Bytesilog - SAPALARAN, MORAGA, RIOS')
root.geometry("720x480")

#Enter title
def input_title():
    title = input("Type the title of the file: ")
    text_box.insert(END, title)

#Open a file
def open_file():
    try:
        open_file = filedialog.askopenfilename() #open a dialog box
        text_file = open(open_file, 'r')
        global read_file
        read_file = text_file.read()

        #Insert the content of the file to the gui
        text_box.insert(END, f'\n{read_file}')
        text_file.close()

        return text_file
    except:
        text_box.insert(END, "Invalid file")
        print("Invalid file")

#count the words
def count_words():
    global word_count
    word_count = Counter(word_tokenize(read_file))

    text_box.insert(END, f'\n Number of occurrences of each word in the attached file:')
    for key, value in word_count.items():
        text_box.insert(END, f' \n {key} : {value}')
        print(f''' 
        {key} : {value}
        ''')
    return

def graph_word():
    fdist = FreqDist(word_tokenize(read_file))
    print(fdist)
    fdist.plot(101, cumulative=False)
    plt.show()

def speak():
    engine = p.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 118)
    engine.say(read_file)
    engine.runAndWait()

text_box = Text(root, width=100, height=20, font=("Helvetica", 12))
text_box.pack(pady=10)

enter_title_button = Button(root, text="Input", command=input_title)
enter_title_button.pack(pady=10)

open_button = Button(root, text="Attach", command=open_file)
open_button.pack(pady=10)

count_button = Button(root, text="Count", command=count_words)
count_button.pack(pady=10)

graph_button = Button(root, text="Graph", command=graph_word)
graph_button.pack(pady=10)

read_button = Button(root, text="Read", command=speak)
read_button.pack(pady=10)

root.mainloop()