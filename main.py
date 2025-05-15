from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    frankenstein_path = "books/frankenstein.txt"

    frankenstein = get_book_text(frankenstein_path)
    num_words = count_words(frankenstein)

    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()