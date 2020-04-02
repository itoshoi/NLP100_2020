import random


def typoglycemia(string):
    result = ''
    string_sp = string.split()
    for word in string_sp:
        if 4 < len(word):
            inner = word[1:-1]
            result += word[0] + \
                ''.join(random.sample(inner, len(inner))) + word[-1:]
        else:
            result += word
        result += ' ' if word != string_sp[-1:] else ''
    return result


test_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(test_str))
