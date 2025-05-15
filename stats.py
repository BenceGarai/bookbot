def count_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_unique_chars(book):
    letter_dict = {}
    for letter in book:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict