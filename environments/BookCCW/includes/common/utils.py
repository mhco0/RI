import re

def names_list_from_file(text_file):
    with open(text_file, "r") as file:
        return file.read().splitlines()

def get_domain_main_name(url):
    return url.split(".")[1]

def rank_books(text):
    rank = 0
    rank_points = 5
    relevant_words = ["livro", "book", "livraria", "leitura"]

    text = text.lower()

    for j in relevant_words:
        if j in text:
            rank += rank_points

    return rank

def pair_binary_search(pair_list, element):
    start = 0
    end = len(pair_list) - 1

    if end == -1:
        return -1

    while True:
        mid = (start + end) // 2
        
        pair = pair_list[mid]

        if pair[0] == element:
            return mid
        elif pair[0] > element:
            end = mid
        else:
            start = mid

        if start == mid:
            break
    
    return -1