def main(): 
    try:
        with open("./books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            print(len(words))
    except Exception as e:
        print(f"error: {e}")

main()
