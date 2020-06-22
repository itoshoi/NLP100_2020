'''
54. 正解率の計測Permalink
52で学習したロジスティック回帰モデルの正解率を，学習データおよび評価データ上で計測せよ．
'''

import sys
import pickle
import pandas as pd
from statistics import mean
import NLP100_5x_util as myutil

DATA_EXTENSION = '.txt'
FEATURE_EXTENSION = '.feature.txt'
LABEL_EXTENSION = '.label.txt'

def accuracy(clf, fname):
    # feature_df = pd.read_csv(fname + FEATURE_EXTENSION)
    # label_ds = pd.read_csv(fname + LABEL_EXTENSION, header=None)[0]
    feature_df = myutil.load_features(fname)
    label_ds = myutil.load_labels(fname)
    predict_labels = clf.predict(feature_df)
    return (predict_labels == label_ds).mean()


if __name__ == "__main__":
    # argv[1] = pickle file name, argv[2] = predict file name
    with open(sys.argv[1], mode='rb') as fp:
        clf = pickle.load(fp)
    print(accuracy(clf, sys.argv[2]))


'''result 
min_df = 1
train 0.9965
test 0.9064
valid 0.8997

min_df = 2
train 0.9926
test 0.9079
valid 0.9012
'''