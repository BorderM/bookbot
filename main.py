def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    report = get_letter_count(text)
    for letter, count in report:
        print(f"The letter {letter} was found {count} times")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open('books/frankenstein.txt') as f:
        return f.read()
    
def get_letter_count(text):
    alphabet = {}
    alph_list = []
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            alphabet[char_lower] = alphabet.get(char_lower, 0) + 1
            
    for letter, count in alphabet.items():
        alph_list.append([letter, count])
        alph_list.sort()
    return alph_list


main()