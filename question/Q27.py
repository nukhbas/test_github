def words_length1(words):
    wordsLength = []
    for word in words:
        wordsLength.append(len(word))
    return wordsLength


if __name__ == '__main__':

    print(words_length1(['lol', 'this', 'is', 'funny']))
