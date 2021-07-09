import leks


def classificator(symbol):
    if ord('a') <= ord(symbol) <= ord('z'):
        return symbol, "буква"

    elif ord('A') <= ord(symbol) <= ord('Z'):
        return symbol, "буква"

    elif ord('0') <= ord(symbol) <= ord('9'):
        return symbol, "цифра"

    elif symbol == ":":
        return symbol, "двоеточие"

    elif symbol == "=":
        return symbol, "равно"

    elif symbol == " ":
        return symbol, "пробел"

    elif symbol == "-" or symbol == "+" or symbol == "*":
        return symbol, "знак"

    elif symbol == "(":
        return symbol, "скобка1"

    elif symbol == ")":
        return symbol, "скобка2"

    elif symbol == "[":
        return symbol, "квскобка1"

    elif symbol == "]":
        return symbol, "квскобка2"

    elif symbol == ",":
        return symbol, "запятая"

    elif symbol == ";":
        return symbol, "тчкзпт"
    else:
        return symbol, "ошибка"


def transliteration(symbol):
    leksema = classificator(symbol)
    if leksema[1] == "ошибка":
        return False, "ошибка! неопознанный символ \"" + symbol + "\""
    leks.leks_analyze(leksema)
    return True, "Vse zbs"
