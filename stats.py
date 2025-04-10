def get_number_of_words(text):
    # it takes a string as input and returns the number of words in the string
    words = text.split()
    return len(words)

def get_number_of_characters(text):
    # it takes the a string and returns the number of times each (including symbols and spaces) character appears in the string.
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def get_sorted_list_of_dictionaries(dictionary):
    # it takes a dictionary as input and returns a sorted list of tuples (key, value) based on the values in descending order
    sorted_list = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return sorted_list


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
