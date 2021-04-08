def text_analyzer(text_to_analyze):
    c = 0, k = 0, l = 0, i = 0, j = 0
    try:
        for char in text_to_analyze:
            c++
            if char.isupper():
                 k++
            if char.islower():
                l++
            if char == ' ':
                i++
            else:
                j++
        printf("===========The text contains", c ,"characters==========\n\n")
        printf(k ,"upper letters\n")
        printf(l ,"lower letters\n")
        printf(i ,"punctuation marks\n")
        printf(j ,"spaces")
     except:
        printf("Please type a valid sentence to the given function!")


