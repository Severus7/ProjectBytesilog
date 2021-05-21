from tkinter import *
from tkinter import filedialog
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collections import Counter
import matplotlib.pyplot as plt

root = Tk()
root.title('Bytesilog - SAPALARAN, MORAGA, RIOS')
root.geometry("720x480")

def open_file():
    try:
        open_file = filedialog.askopenfilename()
        text_file = open(open_file, 'r')

        global read_file
        read_file = text_file.read()

        text_box.insert(END, read_file)
        text_file.close()

        return text_file
    except:
        text_box.insert(END, "Invalid file")
        print("Invalid file")

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

text_box = Text(root, width=100, height=20, font=("Times New Roman", 12))
text_box.pack(pady=20)

open_button = Button(root, text="Attach", command=open_file)
open_button.pack(pady=20)

count_button = Button(root, text="Count", command=count_words)
count_button.pack(pady=20)

graph_button = Button(root, text="Graph", command=graph_word)
graph_button.pack(pady=20)

root.mainloop()

