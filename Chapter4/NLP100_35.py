"""
35. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import NLP100_30
from pprint import pprint

def get_morpheme_frequency():
    result = {}
    sentence_list = NLP100_30.get_morpheme()

    for morpheme_list in sentence_list:
        for morpheme in morpheme_list:
            if morpheme['surface'] in result:
                result[morpheme['surface']] += 1
            else:
                result[morpheme['surface']] = 1
    return sorted(result.items(), key=lambda x:x[1], reverse=True)

if __name__ == "__main__":
    pprint(get_morpheme_frequency())