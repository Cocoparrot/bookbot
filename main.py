from stats import count_words, get_char_count, sort_char_count
import sys


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

# Main function to analyze the book
# and print the results
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
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