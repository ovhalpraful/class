#------------------------------------------------------------
#DSC 510
#Week 8
#Programming Assignment 8.1 - To read content from gettysburg.txt and write in the file created based on user input
#Author Praful Ovhal
#Date 10-30-2025

#Change#: 1
#Change(s) Made: Added comments in the code
#Date of Change: 11-01-2025
#Author: Praful Ovhal
#Change Approved by: Praful Ovhal
#Date Moved to Production: 11-01-2025
#--------------------------------------------------------------
import logging
from logging import basicConfig
import string

# Error logging
basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='error.log',  # Logs will be written to this file
    filemode='a'           # Append mode
)

#Adding the words from the gettysburg file to the dictionary
def add_word(word, word_dict):
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

#Processing the line to remove special char, whitespaces and adding the words to the dictionary
def process_line(line, word_dict):
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower().strip().split()
    for word in line:
        add_word(word, word_dict)

#Processing the output to write in the file from user
def process_file(word_dict, output_filename):
    try:
        with open(output_filename, 'a', encoding='utf-8') as out_file:
            out_file.write(f"Total unique words in the dictionary: {len(word_dict)}\n\n")
            out_file.write(f"{'Word':<15}{'Count':<15}\n")
            out_file.write("-" * 20 + "\n")
            for word, count in sorted(word_dict.items()):
                out_file.write(f"{word:<15}{count:<15}\n")
    except IOError as e:
        logging.error(f"Error writing to the {output_filename}: {e}")
        print(f"Error writing to the file")

def main():
    word_dict = {}
    readfile = "gettysburg.txt"
    try:
        with open(readfile, 'r', encoding='utf-8') as fileHandle:
            for line in fileHandle:
                process_line(line, word_dict)
    except FileNotFoundError as e:
        logging.error(e)
        print(f"\nFile not found")

    try:
        #User input filename to create and write the output.
        output_filename = input("Enter the filename to save the results: ").strip()
        #Validating for blank input.
        if output_filename == "":
            print("Please enter a valid filename.")
        #Checking the file extension and applying txt if not present.
        elif not output_filename.endswith(".txt"):
            output_filename += ".txt"
            # Writing the output to file.
            process_file(word_dict, output_filename)
            print(f"\nContent from {readfile} file copied to {output_filename}")
    except KeyboardInterrupt as e:
        logging.error(f"Keyboard interrupt: {e}")
        print(f"\nProgram stopped from executing. Exiting...")
    except IOError as e:
        logging.error(e)
        print(f"Error creating output file")

if __name__ == '__main__':
    main()