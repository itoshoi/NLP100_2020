'''
52. 学習Permalink
51で構築した学習データを用いて，ロジスティック回帰モデルを学習せよ．
'''

import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import NLP100_5x_util as myutil

DATA_EXTENSION = '.txt'
FEATURE_EXTENSION = '.feature.txt'
LABEL_EXTENSION = '.label.txt'

def learn(fname, C=1.0, tol=1e-4):
    # data_df = pd.read_table(fname + , header=None)
    # label_ds = pd.read_csv(fname + LABEL_EXTENSION, header=None)[0]
    # feature_df = pd.read_csv(fname + FEATURE_EXTENSION)
    label_ds = myutil.load_labels(fname)
    feature_df = myutil.load_features(fname)

    lr = LogisticRegression(max_iter=1000, C=C, tol=tol)
    # b=0, e=1, m=2, t=3 になるみたい
    lr.fit(feature_df, label_ds)
    return lr


if __name__ == "__main__":
    # argv[1] = learn file, argv[2] = output pickle file name
    with open(sys.argv[2], mode='wb') as fp:
        pickle.dump(learn(sys.argv[1]), fp)

# def make_feature_dict(fname):
#     feature_dict = {}
#     i = 0
#     with open(fname) as f:
#         for l in f:
#             words = l.strip('\n').split(' ')
#             # feature_dict = {word: 0 for word in words}
#             # feature_dict = {word: i for word, i in zip(feature_dict.keys(), range(len(feature_dict.keys())))}
#             for word in words:
#                 if word not in feature_dict.keys():
#                     feature_dict[word] = i
#                     i = i + 1
#     return feature_dict


# if __name__ == "__main__":
#     import sys
#     fname = sys.argv[1]
#     feature_dict = make_feature_dict(fname)
#     print(feature_dict)