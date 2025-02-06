def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
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
        print(f"The '{letter}' character was found {cont} times")

if __name__ == "__main__":
    main()
    