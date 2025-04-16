def count_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)