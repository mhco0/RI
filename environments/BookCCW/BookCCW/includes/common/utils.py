
def names_list_from_file(text_file):
    with open(text_file, "r") as file:
        return file.read().splitlines()