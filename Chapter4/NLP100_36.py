"""
36. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import NLP100_35
import matplotlib.pyplot as plt

morpheme_list = NLP100_35.get_morpheme_frequency()

x, y = zip(*morpheme_list)

plt.bar(x[:10], y[:10])
plt.show()

# matplotlibの日本語フォントはmatplotlibrcのfontfamilyを書き換えることで対応した