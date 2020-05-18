"""
32. 動詞の原形
動詞の原形をすべて抽出せよ
"""

import NLP100_30

sentence_list = NLP100_30.get_morpheme()
for morpheme_list in sentence_list:
    for morpheme in morpheme_list:
        if morpheme["pos"] == "動詞":
            print(morpheme["base"])