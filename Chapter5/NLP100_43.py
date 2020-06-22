'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

import NLP100_41
import sys
import re

fname = sys.argv[1]

sentence_list = NLP100_41.get_chunk_sentence_list(fname)

for sentence in sentence_list:
    for chunk in sentence:
        if chunk.dst == -1:
            continue
        if "名詞" in [morph.pos for morph in chunk.morphs]\
        and "動詞" in [morph.pos for morph in sentence[chunk.dst].morphs]:
            noun = chunk.get_morphs_surface()
            verb = sentence[chunk.dst].get_morphs_surface()
            print("{}\t{}".format(noun, verb))
