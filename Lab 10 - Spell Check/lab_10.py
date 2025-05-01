import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_file(file_name):
    with open("dictionary.txt") as dictionary_words:
        dictionary_list = []

        for line in dictionary_words:
            line = line.strip()

            dictionary_list.append(line)

        dictionary_words.close()

        return dictionary_list




def linear_search(dictionary_list):

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(dictionary_list) and dictionary_list[current_list_position]:

        # Advance to the next item in the list
        current_list_position += 1

    return current_list_position

def main():
    dictionary_list = read_in_file("dictionary.txt")
    list_position = linear_search(dictionary_list)
    if list_position < len(dictionary_list):
        print( "There are", len(dictionary_list), "words in the dictionary.")

    chapter_lines = read_in_file("AliceInWonderland200.txt")
    for i in range(len(chapter_lines)):
        words = split_line(chapter_lines[i])
        for word in words:
            if not linear_search(word.upper(), dictionary_words):
                print(f'The word \'{word}\' is not in the dictionary')
                print(f'This word is found on line {i + 1}.')

main()



