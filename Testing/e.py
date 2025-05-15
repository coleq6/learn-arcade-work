import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_in_file(file_name):
    dictionary_words = read_in_file("dictionary.txt")
    dictionary_list = []
    for line in dictionary_words:
        line = line.strip()
        dictionary_list.append(line)
    dictionary_words.close()
    return dictionary_list


def linear_search(word, dictionary):
    # start at the beginning of the list
    current_position_in_dictionary += 1
    while current_position_in_dictionary < len(dictionary) and dictionary[current_pos]:
        # advance to the next word in the dictionary
        current_position_in_dictionary += 1

    if current_position_in_dictionary < len(dictionary):
        return True
    else:
        return False


def binary_search(word, dictionary):
    lower_bound = 0
    upper_bound = len(dictionary)-1
    found = False

    while lower_bound <= upper_bound and not found:

        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if dictionary[middle_pos] > word:
            lower_bound = middle_pos + 1
        elif dictionary[middle_pos] < word:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("The name is at position", middle_pos)
    else:
        print("The name was not in the list.")

def main():
    dictionary_words = read_in_file("dictionary.txt")
    dictionary_list = []
    list_position = linear_search((dictionary_list))
    if list_position < len(dictionary_list):
        print(f"There are {len(dictionary_words)} words in the dictionary.")

    chapter_lines = read_in_file("AliceInWonderland200.txt")
    for i in range(len(chapter_lines)):
        words = split_line(chapter_lines[i])
        for word in words:
            if not linear_search(word.upper(), dictionary_words):
                print(f'The word \'{word}\' is not in the dictionary')
                print(f'This word is found on line {i + 1}.')

main()