def get_num_words(text):
    return len(text.split())

def get_char_nums(text):
    char_nums = {}
    for char in text:
        c = char.lower()
        char_nums[c] = char_nums.get(c, 0) + 1
    return char_nums

def convert_to_dict_list(char_nums):
    dict_list = []
    for c in char_nums:
        if c.isalpha():
            dict_list.append({"char": c, "num": char_nums[c]})
    return dict_list

def sort_on(dict):
    return dict["num"]

def get_dict_list(char_nums):
    dict_list = convert_to_dict_list(char_nums)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
