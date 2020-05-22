import NLP100_41
import sys
import re

fname = sys.argv[1]

sentence_list = NLP100_41.get_chunk_sentence_list(fname)

p = re.compile(r"。|、|\s")
for sentence in sentence_list:
    for chunk in sentence:
        if chunk.dst == -1:
            continue
        if "名詞" in [morph.pos for morph in chunk.morphs]\
        and "動詞" in [morph.pos for morph in sentence[chunk.dst].morphs]:
            noun = p.sub("", chunk.get_morphs_surface())
            verb = p.sub("", sentence[chunk.dst].get_morphs_surface())
            print("{}\t{}".format(noun, verb))
