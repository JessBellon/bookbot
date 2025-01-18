def get_file_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words_as_list(contents):
    return contents.split()

def get_word_count(contents): 
    words = get_words_as_list(contents)
    num = len(words)
    return num

def get_char_count_dict(contents):
    letters = {}
    for l in contents:
        if l not in letters:
            letters[l] = 0
        letters[l] += 1
    return letters

def report_on_char_count(char_cts):
    list_of_dicts = []
    for k in char_cts:
        if k.isalpha():
            list_of_dicts.append({ "char": k , "count": char_cts[k] })
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    for dic in list_of_dicts:
        print(f"The '{dic["char"]}' character was found {dic["count"]} times")
    


def sort_on(dict):
    return dict["count"]

def main(): 
    try:
        contents = get_file_contents("./books/frankenstein.txt")
        word_count = get_word_count(contents)
        print(f"There are {word_count} words.")
        char_cts = get_char_count_dict(contents.lower())
        report_on_char_count(char_cts)
    except Exception as e:
        print(f"error: {e}")

main()
