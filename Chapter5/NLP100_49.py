import NLP100_48
import sys
import re
import itertools

fname = sys.argv[1]
tree_sentence_list = NLP100_48.get_tree_sentence_list(fname)

# ネスト深すぎ問題
for tree_sentence in tree_sentence_list:
    for i in range(len(tree_sentence) - 1):
        for j in range(i + 1, len(tree_sentence)):
            # 文節iはsentence[i][0]で表される
        
            for k, l in itertools.product(range(len(tree_sentence[i])), range(len(tree_sentence[j]))):
                if tree_sentence[i][k].get_morphs_surface() == tree_sentence[j][l].get_morphs_surface():
                    # 名詞句が2つ以上ない前提になっている。
                    chunk_i_noun = "".join([m.surface for m in tree_sentence[i][0].morphs if m.pos == "名詞"])
                    chunk_j_noun = "".join([m.surface for m in tree_sentence[j][0].morphs if m.pos == "名詞"])

                    # l == 0 のときは、文節iと文節jが同じとき
                    if l == 0:
                        tree_text = " -> ".join([c.get_morphs_surface() for c in tree_sentence[i][0:k+1]])
                        tree_text = tree_text.replace(chunk_i_noun, "X")
                        tree_text = tree_text.replace(chunk_j_noun, "Y")
                        print(tree_text)
                    else:
                        tree_text = " -> ".join([c.get_morphs_surface() for c in tree_sentence[i][0:k]])
                        tree_text += " | " + " -> ".join([c.get_morphs_surface() for c in tree_sentence[j][0:l]])
                        tree_text += " | " + tree_sentence[i][k].get_morphs_surface()
                        tree_text = tree_text.replace(chunk_i_noun, "X")
                        tree_text = tree_text.replace(chunk_j_noun, "Y")
                        print(tree_text)
                    break
    print()
