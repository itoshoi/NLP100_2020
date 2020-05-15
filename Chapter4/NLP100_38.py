"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import NLP100_35
import matplotlib.pyplot as plt

morpheme_freq_list = NLP100_35.get_morpheme_frequency()
counts = [m[1] for m in morpheme_freq_list]

plt.hist(counts, range=(10, 100))
plt.show()

# 37の場合
# import NLP100_37

# co_occ_words = NLP100_37.get_co_occurrence_words_by_pyfpgrowth("猫")
# co_occ_counts = [w[1] for w in co_occ_words]

# plt.hist(co_occ_counts, range=(10, 100))
# plt.show()