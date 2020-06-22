'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

import NLP100_41
import sys
import re

sentence_list = NLP100_41.get_chunk_sentence_list(sys.argv[1])

for sentence in sentence_list:
    for chunk in sentence:
        word = chunk.get_morphs_surface()
        src_words = ",".join([sentence[i].get_morphs_surface() for i in chunk.srcs])
        dst_word = sentence[chunk.dst].get_morphs_surface()
        print("{chunk}\t{srcs}\t{dst}".format(chunk=word, srcs=src_words, dst=dst_word))