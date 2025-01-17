def main(): 
    try:
        with open("./books/frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents)
    except Exception as e:
        print(f"error: {e}")

main()
