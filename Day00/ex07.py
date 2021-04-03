def function(sentence, n):
    liste = []
    for i in sentence:
        if len(i) >= n:
            liste.append(i)
    return liste