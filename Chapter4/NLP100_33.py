"""
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import re
import NLP100_30

sentence_list = NLP100_30.get_morpheme()

# for morpheme in morpheme_list:
#     if morpheme['pos'] == '名詞':
#         if re.match(r'.+?の.+?', morpheme['surface']) != None:
#             print(morpheme['surface'])

for morpheme_list in sentence_list:
    for i in range(1, len(morpheme_list) - 1):
        prev = morpheme_list[i-1]
        now = morpheme_list[i]
        mnext = morpheme_list[i+1]
        if now['surface'] == 'の':
            if prev['pos'] == '名詞' and mnext['pos'] == '名詞':
                print(prev['surface'] + now['surface'] + mnext['surface'])