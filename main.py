def main():
    # get data for report
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    wordcount = count_words(text)
    charcount = count_chars_occurence(text)
    formatted_charcount = format_dict(charcount)
    formatted_charcount.sort(reverse=True, key=sort_on)

    # generate report
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount} words found in the document")
    print()
    for item in formatted_charcount:
        if item["char"].isalpha():
            print(f"The '{item["char"]} character was found {item["num"]} times")
    print("--- End report ---")

def get_book(path_to_book):
    with open(path_to_book) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def count_chars_occurence(text):
    characters = {}
    for char in text:
        lower = char.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

def format_dict(dict):
    new_list = []
    for item in dict:
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = dict[item]
        new_list.append(new_dict)
    return new_list

def sort_on(dict):
    return dict["num"]

main()