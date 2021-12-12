
searches = {'a': 1, 'b': 2, 'c': 3, 'asd': 4, 'we': 5}
for key, value in sorted(list(searches.items()), key=lambda x: x[0].lower(), reverse=True):
    print(key, value)
