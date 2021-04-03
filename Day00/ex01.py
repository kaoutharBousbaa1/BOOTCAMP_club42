def reverse_function(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    for caractere in reverse_sentence:
        if caractere.islower():
            caractere.upper()
        else:
            caractere.lower()
    return reverse_sentence

print(reverse_function("Hello World"))