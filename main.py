from stats import count_words
from stats import count_unique_chars
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    frankenstein_path = "books/frankenstein.txt"

    frankenstein = get_book_text(frankenstein_path)
    num_words = count_words(frankenstein)
    frankenstein_letter_dict = count_unique_chars(frankenstein)
    sorted_letter_dict = sort_dict(frankenstein_letter_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_letter_dict:
        letter = char["char"]
        count = char["num"]
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()