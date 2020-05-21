'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
'''

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
