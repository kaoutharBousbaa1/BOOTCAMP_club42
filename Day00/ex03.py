def text_analyzer(text_to_analyze):
    c = 0, k = 0, l = 0, i = 0, j = 0
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
   print("===========The text contains", c ,"characters==========\n\n")
   print(k ,"upper letters\n")
   print(l ,"lower letters\n")
   print(i ,"punctuation marks\n")
   print(j ,"spaces")


