def thesaurus(*args):
    names = {}
    for name in args:
        s = name[0]
        if s not in names:
            names[s] = []
        names[s].append(name)
    return names


print(thesaurus('Кирилл', 'Юрий', 'Джава', 'Кристина', 'Юля', 'Дана'))
