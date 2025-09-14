def get_num_words(buffer):
    return len(buffer.split())

def get_char_counts(file_path):
    with open(file_path) as book_file:
        contents = book_file.read()
        counts = char_counts(contents)
        return char_counts_to_sorted_dicts(counts)


def get_word_numbers(file_path):
    num_words = 0
    with open(file_path) as book_file:
        contents = book_file.read()
        num_words = get_num_words(contents)
        
    return num_words


def char_counts(string):
    counts = dict()
    for char in string.lower():
        try:
            counts[char] += 1
        except:
            counts[char] = 1

    return counts

def char_counts_to_sorted_dicts(char_counts):
    dicts = []
    for char_key in char_counts:
        d = {"char": char_key, "count": char_counts[char_key]}
        dicts.append(d)

    def key(items):
        return items["count"]
    dicts.sort(reverse=True, key=key)
    return dicts

