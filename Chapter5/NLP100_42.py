import NLP100_41
import sys
import re

sentence_list = NLP100_41.get_chunk_sentence_list(sys.argv[1])

p = re.compile("。|、")
for sentence in sentence_list:
    for chunk in sentence:
        word = chunk.get_morphs_surface()
        word = p.sub("", word)
        src_words = ",".join([sentence[i].get_morphs_surface() for i in chunk.srcs])
        src_words = p.sub("", src_words)
        dst_word = sentence[chunk.dst].get_morphs_surface()
        dst_word = p.sub("", dst_word)
        print("{chunk}\t{srcs}\t{dst}".format(chunk=word, srcs=src_words, dst=dst_word))