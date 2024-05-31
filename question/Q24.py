def make_3sg_form(verb):

    if verb.endswith('y'):
        return verb[:-1]+'ies'
    elif verb.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        return verb+'es'
    else:
        return verb+'s'


if __name__ == '__main__':

    print(make_3sg_form('fry'))
    print(make_3sg_form('brush'))
    print(make_3sg_form('bin'))
    print(make_3sg_form('piz'))
