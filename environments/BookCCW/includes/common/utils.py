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