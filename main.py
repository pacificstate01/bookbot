import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
    with open(book_path, "r") as f:
        file_contents = f.read()

    words = file_contents.split()
    print(f"--- Begin report of {book_path} ---")
    print(len(words), "words found in the document")
    countchar(file_contents)
    print("--- End report ---")

def countchar(file_contents):
    text = file_contents.lower()
    char_symbols = {}
    for char in text:
        if char.isalpha():
            if char in char_symbols:
                char_symbols[char] += 1
            else:
                char_symbols[char] = 1

    chardic = []
    for letter, count in char_symbols.items():
        char_dic = {"char": letter, "num": count}
        chardic.append(char_dic)

    # Sort by count in descending order
    chardic.sort(reverse=True, key=lambda x: x["num"])

    # Print each character's count
    for i in chardic:
        letter = i["char"]
        cont = i["num"]
        print(f"{letter}: {cont}")
if __name__ == "__main__":
    main()
    
