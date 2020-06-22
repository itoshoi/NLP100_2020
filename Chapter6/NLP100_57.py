'''
57. 特徴量の重みの確認Permalink
52で学習したロジスティック回帰モデルの中で，重みの高い特徴量トップ10と，重みの低い特徴量トップ10を確認せよ．
'''

import NLP100_5x_util as myutil
import pandas as pd
import sys

def top_weight(lr, feature_names, N, order = -1):
    for i in range(4):
        # 説明変数の係数を大きい順にソート (coef = coefficient)
        sorted_coef = lr.coef_[i].argsort()
        indices = sorted_coef[::order][:N]
        print(myutil.CATEGORY_NAMES[i])
        print(pd.DataFrame([feature_names[indices], lr.coef_[i][indices]], index=['特徴量', '重み']))
        print()

if __name__ == "__main__":
    # argv[1] = pickle file name
    clf = myutil.load_clf(sys.argv[1])
    feature = myutil.load_feature_names('test')
    # 重みの高い特徴量トップ10
    print('Top10 High Scores')
    top_weight(clf, feature, 10, -1)
    # 重みの低い特徴量トップ10
    print('Top10 Low Scores')
    top_weight(clf, feature, 10, 1)
