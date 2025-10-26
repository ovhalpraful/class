#------------------------------------------------------------
#DSC 510
#Week 7
#Programming Assignment 7.1 -
#Author Praful Ovhal
#Date 10-25-2025

#Change#: 1
#Change(s) Made:
#Date of Change: 10-25-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 10-25-2025
#--------------------------------------------------------------
import logging
import string
from time import process_time

from fontTools.ttx import process

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

def add_word(word, word_dict):
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

def process_line(line, word_dict):
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower().strip().split()
    for word in line:
        add_word(word, word_dict)

def pretty_print(word_dict):
    print(f"{'Word':<15}{'Count':<15}")
    print("-"*20)
    for word, count in sorted(word_dict.items()):
        print(f"{word:<15}{count:<15}")

def main():
    word_dict = {}
    try:
        with open("gettysburg.txt", "r") as fileHandle:
            for line in fileHandle:
                process_line(line, word_dict)
        print(f"\n Total unique words: {len(word_dict)}\n")
        pretty_print(word_dict)
    except FileNotFoundError as e:
        logging.error(e)
        print(e)

if __name__ == '__main__':
    main()