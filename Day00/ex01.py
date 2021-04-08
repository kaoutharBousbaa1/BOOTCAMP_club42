def reverse_function(sentence):
    #words = sentence.split(' ')
    #reverse_sentence = ' '.join(reversed(words))
    n = len(sentence)
    for i in range(0,n):
        sentence[i] = sentence[n-i]
    for caractere in sentence:
        if caractere.islower():
            caractere.upper()
        else:
            caractere.lower()
    
    return sentence

printf(reverse_function("Hello World"))
