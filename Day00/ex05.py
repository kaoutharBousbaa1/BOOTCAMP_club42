def kata00(tuple):
    n = len(tuple)
    k = 0
    for i in range(n):
        k++
        print("the", k ,"numbers are")
    for c in tuple:
        print(c)

def kata01(dict()):
    for cle in dict.keys() and for valeur in dict.values():
        print(cle)
        print("was created by")
        print(cle)
        print("\n")

def kata02():
    tuple = (3, 30, 2019, 9, 35)
    print(tuple[3],"/")
    print(tuple[4],"/")
    print(tuple[2],"/")
    print(tuple[0], ":")
    print(tuple[1])


def kata03(string):
    print("----------------------------------The ", string)
    k = 0
    for i in string:
        k++
    print(k)
