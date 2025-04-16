from stats import count_words, get_char_count, sort_char_count

filepath = 'books/frankenstein.txt'

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    text = get_book_text(filepath)
    num_words = count_words(text)
    char_counts = get_char_count(text)
    report = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char, count in report:  # Unpack the tuple directly
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")

    print("============= END ===============")
if __name__ == "__main__":
    main()
# This code reads the content of a file named 'book.txt' and prints it to the console.  