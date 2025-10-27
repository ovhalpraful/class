#------------------------------------------------------------
#DSC 510
#Week 7
#Programming Assignment 7.1 -
#Author Praful Ovhal
#Date 10-25-2025

#Change#: 1
#Change(s) Made: Added comments
#Date of Change: 10-26-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 10-26-2025
#--------------------------------------------------------------
import logging
import string

# Error logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

#Reading words from the gettysburg file and adding to the dictionary
def add_word(word, word_dict):
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

#Reading the file & processing the line to remove special char, whitespaces and adding the words to the dictionary
def process_line(line, word_dict):
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower().strip().split()
    for word in line:
        add_word(word, word_dict)

#Printing the result in a grid format
def pretty_print(word_dict):
    print(f"{'Word':<15}{'Count':<15}")
    print("-"*20)
    for word, count in sorted(word_dict.items()):
        print(f"{word:<15}{count:<15}")

def main():
    word_dict = {}
    try:
        with open("gettysburg.txt") as fileHandle:                      #Opening file in Read only format
            for line in fileHandle:
                process_line(line, word_dict)                           #Reading the file and processing line by line to read words & add to dictionary
        print(f"\nTotal unique words in the dictionary: {len(word_dict)}\n")
        pretty_print(word_dict)
    except FileNotFoundError as e:
        logging.error(e)
        print(f"\n File not found: {e}")

if __name__ == '__main__':
    main()