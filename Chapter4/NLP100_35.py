"""
35. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import NLP100_30

def get_morpheme_frequency():
    result = {}
    morpheme_list = NLP100_30.get_morpheme()

    for morpheme in morpheme_list:
        if morpheme['surface'] in result:
            result[morpheme['surface']] += 1
        else:
            result[morpheme['surface']] = 1
    return sorted(result.items(), key=lambda x:x[1], reverse=True)

if __name__ == "__main__":
    print(get_morpheme_frequency())