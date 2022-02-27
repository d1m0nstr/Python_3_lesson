def thesaurus(*names):
    lists = {}
    for name in names:
        key = name[0].capitalize()
        if key not in lists:
            lists[key] = []
        lists[key].append(name)
    return lists
