def kata00((19,42,21)):
    print("The 3 numbers are: {0[0]}, {0[1]}, {0[2]}".format(tuple))

def kata01(dictionary):
    print("{0} was created by {0}".format(**dictionary))
languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
kata01(languages)

def kata02(tup):
    print("{0[3]/{0[6]}/{0[2]}".format(tup) + "{:2d}:{0[1]}".format(tup[0], tup))
tup = (3,30,2019,9,25)
kata02(tup)


def kata03(phrase):
    print("----------------------------------", phrase + "%")
    k = 0
    for i in string:
        k++
    print(k)
phrase = "The right format"
