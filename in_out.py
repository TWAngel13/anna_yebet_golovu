import sasha


def read():
    f = open('input.txt', 'r')
    return f.read()


def write(str):
    f = open('output.txt', 'w')
    f.write(str)


def init():
    str_from_file = read()
    for symbol in str_from_file:
        temp = sasha.transliteration(symbol)
        if not temp[0]:
            return temp
    return True, "Vse zbs"


temp2 = init()
if not temp2[0]:
    write("REJECT. " + temp2[1])
else:
    write("ACCEPT")
