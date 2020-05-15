"""
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import NLP100_30

morpheme_list = NLP100_30.get_morpheme()

result = []
connection_list = []
for morpheme in morpheme_list:
    if morpheme['pos'] == '名詞':
        connection_list.append(morpheme['surface'])
    else:
        if 0 < len(connection_list):
            result.append(connection_list[:])
            connection_list.clear()

for con in result:
    print(''.join(con))