"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

import NLP100_30

morpheme_list = NLP100_30.get_morpheme()
for morpheme in morpheme_list:
    if morpheme['pos'] == '動詞':
        print(morpheme['surface'])