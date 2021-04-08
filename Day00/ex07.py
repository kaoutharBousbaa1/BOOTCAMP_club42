def function(sentence, n):
    words = sentence.split(' ')
    liste = []
    for words in sentence:
        if len(words) >= n:
            liste.append(words)
    return liste
