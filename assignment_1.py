import argparse

filename = open("C:/Users/Niliya/Desktop/sample.txt", "r")

 
#########################################################################
 
parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--count_type',choices=['line_count', 'word_count', 'character_count'])
args = parser.parse_args()

if args.file is None:
    print("--file argument is required")
    raise Exception

if args.count_type == 'line_count':
    # logic for line count
    number_of_lines = 0
    for line in filename:
        line = line.strip("\n")
        number_of_lines += 1
    print(number_of_lines)
elif args.count_type == 'word_count':
    # logic for word count
    number_of_words =0
    for line in filename:
       line = line.strip("\n")
       words = line.split()
       number_of_words += len(words) 
    print(number_of_words)

elif args.count_type == 'character_count':
    # logic for char count
    number_of_characters = 0
    for line in filename:
        line = line.strip("\n")
        number_of_characters += len(line)
    print(number_of_characters)
#3##########################################################################
    
filename.close()

#3##########################################################################
