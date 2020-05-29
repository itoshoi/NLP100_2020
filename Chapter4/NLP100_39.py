"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import NLP100_35
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

morpheme_freq_list = NLP100_35.get_morpheme_frequency()

words, counts = zip(*morpheme_freq_list)

plt.bar(range(1, 1001), counts[:1000])

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')

plt.savefig("NLP100_39_result.png")
# plt.show()