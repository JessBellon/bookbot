def get_file_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(contents): 
    words = contents.split()
    num = len(words)
    return num
def main(): 
    try:
        contents = get_file_contents("./books/frankenstein.txt")
        word_count = get_word_count(contents)
        print(f"There are {word_count} words.")
    except Exception as e:
        print(f"error: {e}")

main()
