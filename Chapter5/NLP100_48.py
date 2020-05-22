import NLP100_41
import sys
from pprint import pprint


# [[[Chunk, Chunk, ..], [Chunk, Chunk, ..], ..], [[Chunk, Chunk, ..], [Chunk, Chunk, ..], ..], ..]という形で返す
def get_tree_sentence_list(fname):
    result = []
    sentence_list = NLP100_41.get_chunk_sentence_list(fname)
    for sentence in sentence_list:
        result_sentence = []
        for chunk in sentence:
            if '名詞' in [m.pos for m in chunk.morphs]:
                tree = [chunk]
                dst = chunk.dst
                while(dst != -1):
                    dst_chunk = sentence[dst]
                    tree.append(dst_chunk)
                    dst = dst_chunk.dst
                result_sentence.append(tree[:])
        result.append(result_sentence[:])
    return result

if __name__ == "__main__":
    fname = sys.argv[1]
    for tree_sentence in get_tree_sentence_list(fname):
        pprint([" -> ".join(chunk.get_morphs_surface() for chunk in tree) for tree in tree_sentence])