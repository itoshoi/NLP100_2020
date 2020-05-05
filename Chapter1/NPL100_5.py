import re


def n_gram(_list, n):
    result = []
    for i in range(len(_list) - n + 1):
        result.append(_list[i:i+n])
    return result


def word_bi_gram(string):
    string_sp = re.findall('[^,. ]+', string)
    return n_gram(string_sp, 2)


def string_bi_gram(string):
    return n_gram(string, 2)


if __name__ == '__main__':
    test_str = "I am an NLPer"
    print(string_bi_gram(test_str))
    print(word_bi_gram(test_str))
