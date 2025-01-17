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



def main(): 
    try:
        # contents = get_file_contents("./books/debug.txt")
        contents = get_file_contents("./books/frankenstein.txt")
        # word_count = get_word_count(contents)
        # print(f"There are {word_count} words.")
        char_cts =get_char_count_dict(contents.lower())
        print(char_cts)
    except Exception as e:
        print(f"error: {e}")

main()
