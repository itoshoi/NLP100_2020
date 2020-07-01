'''
67. k-meansクラスタリング
国名に関する単語ベクトルを抽出し，k-meansクラスタリングをクラスタ数k=5として実行せよ．
'''
import sys
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np


def get_counties(fname):
    # 国名に関する語の集合
    countries = set()

    # 国名に関する語を抽出
    with open(fname) as f:
        # 現在処理中のカテゴリー
        target_category = ''
        for l in f:
            l_sp = l.split()
            if l_sp[0] == ':':
                target_category = l_sp[1]
            else:
                # カテゴリーにcapitalが含まれる場合は国名に関係することにする
                if 'capital' in target_category:
                    # countries.add(l_sp[0])
                    countries.add(l_sp[1])
                    # countries.add(l_sp[2])
                    countries.add(l_sp[3])

    # k-meansでインデックスが大事になるのでsetからlistにしておく
    countries = list(countries)
    return countries

def kmeans_clustering(model, coutries):
    # 国に関する語の特徴量リスト
    country_vecs = [model[country] for country in countries]

    # k-means法
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(country_vecs)

    # 出力
    for i in range(5):
        cluster_indices = np.where(kmeans.labels_ == i)[0]
        print('cluster ' + str(i))
        print(' '.join([countries[ci] for ci in cluster_indices]))

if __name__ == "__main__":
    # argv[1] = model file path, argv[2] = questions-words file path
    model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=True)
    countries = get_counties(sys.argv[2])
    kmeans_clustering(model, countries)