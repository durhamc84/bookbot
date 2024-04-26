def main():
    book_path = "/home/durhamc84/workspace/github.com/durhamc84/bookbot/books/frankenstein.txt"    
    print_report(book_path)    

def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(book):
    letter_count = {}
    for char in book:
        new_char = char.lower()
        if new_char in letter_count:
            letter_count[new_char] += 1
        else:
            letter_count[new_char] = 1
    return letter_count

def sort_on(dict):
    return dict["count"]

def sort_letters(letter_dict):
    new_list = []
    for item in letter_dict:
        if item.isalpha():
            new_list.append({"letter": item, "count": letter_dict[item]})
    new_list.sort(reverse=True, key=sort_on)    
    for item in new_list:
        print(f"The '{item["letter"]}' character was found {item["count"]} times")

def print_report(book_path):
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_count = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    print("")
    sort_letters(letter_count)
    print("--- End Report ---")

main()
