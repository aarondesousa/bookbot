def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_char_count(dict):
    return dict["count"]

def sort_chars_by_count(char_counts):
    sorted_chars = []
    for char in char_counts:
        sorted_chars.append({
            "char": char,
            "count": char_counts[char],
        })
    sorted_chars.sort(key=get_char_count, reverse=True)
    return sorted_chars

# dict instead of list
def alt_sort_chars_by_count(char_counts):
    return dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
