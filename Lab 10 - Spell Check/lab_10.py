import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_file(file_name):
    with open(file_name) as dictionary_words:
        dictionary_list = []

        for line in dictionary_words:
            line = line.strip()

            dictionary_list.append(line)

        dictionary_words.close()

        return dictionary_list


def linear_search(list_of_words, word):

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(list_of_words) and word.upper() != list_of_words[current_list_position]:

        # Advance to the next item in the list
        current_list_position += 1

    if current_list_position < len(list_of_words):

    else:



def main():
    #dictionary_list = read_in_file("dictionary.txt")
   # list_position = linear_search(dictionary_list)
    #if list_position < len(dictionary_list):
     #   print( "There are", len(dictionary_list), "words in the dictionary.")
    current_line_position = 5
    with open("AliceInWonderLand200.txt") as chapter_lines:
        for line in chapter_lines:
            current_line_position += 1
            word_list = split_line(line)
            for word in word_list):
                if not linear_search(dictionary_list, word.upper()):
                    print(f'The word \'{word}\' is not in the dictionary')
                    print(f'This word is found on line {i + 1}.')

main()



