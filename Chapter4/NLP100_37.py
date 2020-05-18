"""
37. 「猫」と共起頻度の高い上位10語
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import NLP100_30
import pyfpgrowth
import matplotlib.pyplot as plt
from pprint import pprint

# pyfpgrowthを使って共起頻度を求める
def get_co_occurrence_words_by_pyfpgrowth(target):
    # 共起語に含める語の品詞
    TARGET_POS = ['名詞', '動詞']
    sentence_list = NLP100_30.get_morpheme()
    # タプルのリストから、語(表層形)のリストのリストに変換 (ここで品詞も選別)
    sentence_surface_list = [[morpheme['surface'] for morpheme in s if morpheme['pos'] in TARGET_POS] for s in sentence_list]
    co_sentence_list = []
    for sentence in sentence_surface_list:
        if target in sentence:
            set_sentence = set(sentence)
            set_sentence.remove(target)
            co_sentence_list.append(set_sentence)
    patterns = pyfpgrowth.find_frequent_patterns(co_sentence_list, 10)
    sorted_patterns = sorted(patterns.items(), reverse=True, key=lambda x: x[1])
    return sorted_patterns

if __name__ == "__main__":
    # [((共起語1, 共起語2, ...), 出現数), ...] という形で共起語が得られる
    co_occ_words = get_co_occurrence_words_by_pyfpgrowth("猫")
    words = [",".join(map(str, w[0])) for w in co_occ_words]
    counts = [w[1] for w in co_occ_words]
    plt.bar(words[:10], counts[:10])
    plt.show()