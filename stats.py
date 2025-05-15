def count_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count