def main():
    book_path = "books/frankenstein.txt"
    content = get_book_content(book_path)
    word_count = get_number_of_words(content)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    char_count_dict = get_num_characters_dict(content)
    char_dict_list = convert_char_dict(char_count_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    print_dict_list(char_dict_list)
    print("--- End report ---")
    
    

def get_number_of_words(content):
    return len(content.split())

def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_num_characters_dict(content):
    lower_str = content.lower()
    char_count = {}
    for c in lower_str:
        if c.isalpha():
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    return char_count

def convert_char_dict(dict):
    l = []
    for k, v in dict.items():
        l.append({"character": k, "count": v})
    return l

def sort_on(dict):
    return dict["count"]

def print_dict_list(list):
    for e in list:
        print(f"The '{e['character']}' character was found {e['count']} times")



if __name__ == "__main__":
    main()