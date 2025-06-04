from stats import get_num_words, get_char_nums, get_dict_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_nums = get_char_nums(text)
    dict_list = get_dict_list(char_nums)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for dict in dict_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()
