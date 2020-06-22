import NLP100_41
import sys
import pydotplus

fname = sys.argv[1]
sentence_list = NLP100_41.get_chunk_sentence_list(fname)

# 全部の行でやると9000枚くらいの画像ファイルができるからさすがにやめた
# for sentence in sentence_list:
sentence = sentence_list[7]
edges = []
for chunk in sentence:
    if chunk.dst != -1:
        edges.append((chunk.get_morphs_surface(), sentence[chunk.dst].get_morphs_surface()))
graph = pydotplus.graph_from_edges(edges, directed=True)
graph.write("NLP100_44_result.png", format='png')
