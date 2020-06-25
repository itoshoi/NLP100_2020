'''
69. t-SNEによる可視化
ベクトル空間上の国名に関する単語ベクトルをt-SNEで可視化せよ．
'''
import NLP100_67
import sys
from gensim.models import KeyedVectors
import bhtsne
from matplotlib import pyplot as plt
import numpy as np

def show_tSNE(vecs, labels):
    # vecsをtnseでfit_transform
    embedded = bhtsne.tsne(np.array(vecs).astype(np.float64), dimensions=2)
    # グラフを作成(20x20インチ)
    plt.figure(figsize=(20, 20))
    # 散布図を作成 (embdeddedは2次元ベクトルのリスト)
    plt.scatter(embedded[:, 0], embedded[:, 1])
    # アノテーションを作成
    for i, country in enumerate(countries):
        plt.annotate(country, (embedded[i, 0], embedded[i, 1]))
    # グラフの保存
    plt.savefig('NLP100_69_result.png')
    plt.show()

if __name__ == "__main__":
    # argv[1] = model file path, argv[2] = questions-words file path
    model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=True)
    countries = NLP100_67.get_counties(sys.argv[2])

    # 国に関する語の特徴量リスト
    country_vecs = [model[country] for country in countries]
    # t-SNEによる可視化
    show_tSNE(country_vecs, countries)
