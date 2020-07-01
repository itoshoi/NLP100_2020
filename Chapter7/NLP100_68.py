'''
68. Ward法によるクラスタリング
国名に関する単語ベクトルに対し，Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''
import NLP100_67
import sys
from scipy.cluster.hierarchy import linkage, dendrogram
from gensim.models import KeyedVectors
from matplotlib import pyplot as plt

def ward_clusturing(model, countries):
    # 国に関する語の特徴量リスト
    country_vecs = [model[country] for country in countries]

    # Ward法によるクラスタリング
    plt.figure(figsize=(30, 10))
    z = linkage(country_vecs, method='ward')
    # デンドログラムの作成
    dendrogram(z, labels=countries)
    
    plt.savefig('NLP100_68_result.png')
    plt.show()


if __name__ == "__main__":
    # argv[1] = model file path, argv[2] = questions-words file path
    model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=True)
    countries = NLP100_67.get_counties(sys.argv[2])
    ward_clusturing(model, countries)