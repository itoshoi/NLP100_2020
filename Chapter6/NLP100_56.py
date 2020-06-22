'''
56. 適合率，再現率，F1スコアの計測
52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，評価データ上で計測せよ．
カテゴリごとに適合率，再現率，F1スコアを求め，カテゴリごとの性能をマイクロ平均（micro-average）と
マクロ平均（macro-average）で統合せよ．
'''

import NLP100_55
import sys
import NLP100_5x_util as myutil
import numpy as np
import pandas as pd

def score(cm):
    tp = cm.diagonal()
    fn = cm.sum(axis=1) - tp
    fp = cm.sum(axis=0) - tp

    # 適合率
    precision = tp / (tp + fp)
    # 再現率
    recall = tp / (tp + fn)
    # F1値
    F1 = 2 * precision * recall / (precision + recall)

    # マイクロ平均
    micro_p = tp.sum() / (tp + fp).sum()
    micro_r = tp.sum() / (tp + fn).sum()
    micoro_F1 = 2 * micro_p * micro_r / (micro_p + micro_r)
    micro_ave = np.array([micro_p, micro_r, micoro_F1])

    # マクロ平均
    macro_p = precision.mean()
    macro_r = recall.mean()
    macro_F1 = 2 * macro_p * macro_r / (macro_p + macro_r)
    macro_ave = np.array([macro_p, macro_r, macro_F1])

    data = np.array([precision, recall, F1]).T
    data = np.vstack([data, micro_ave, macro_ave])
    print(pd.DataFrame(data, index = ['b', 'e', 'm', 't', 'マイクロ平均', 'マクロ平均'], columns = ['再現率', '適合率', 'F1スコア']))


if __name__ == "__main__":
    # argv[1] = pickle file name, argv[2] = predict file name
    clf = myutil.load_clf(sys.argv[1])
    cm = NLP100_55.make_confusion_matrix(clf, sys.argv[2])
    score(cm)