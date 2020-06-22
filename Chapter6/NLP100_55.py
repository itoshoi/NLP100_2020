'''
55. 混同行列の作成Permalink
52で学習したロジスティック回帰モデルの混同行列（confusion matrix）を，学習データおよび評価データ上で作成せよ．
'''

import numpy as np
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import NLP100_5x_util as myutil
from sklearn.metrics import confusion_matrix

def make_confusion_matrix(lr, fname):
    feature_df = myutil.load_features(fname)
    label_ds = myutil.load_labels(fname)
    predict_labels = lr.predict(feature_df)
    
    # sklearnのconfusion_matrixを使っても良いけど、なんかつまらないので。
    mat = np.zeros((4, 4), dtype=np.int32)
    for pl, tl in zip(predict_labels, label_ds):
        mat[pl, tl] += 1
    
    return mat

if __name__ == "__main__":
    # argv[1] = pickle file name, argv[2] = predict file name
    clf = myutil.load_clf(sys.argv[1])
    cm = make_confusion_matrix(clf, sys.argv[2])

    # ヒートマップの表示 
    ticklabels = ['b', 'e', 'm', 't']
    sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=ticklabels, yticklabels=ticklabels)
    plt.savefig('NLP100_55_result_' + sys.argv[2] + '.png')
    plt.show()