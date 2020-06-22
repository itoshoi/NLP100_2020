'''
51. 特徴量抽出
学習データ，検証データ，評価データから特徴量を抽出し，
それぞれtrain.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ． 
なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう
'''

import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle

DATA_EXTENSION = '.txt'
FEATURE_EXTENSION = '.feature.txt'
LABEL_EXTENSION = '.label.txt'

def make_feature(fname, clf = None, min_df=2):
    data = pd.read_table(fname + DATA_EXTENSION, header=None)
    labels = data[0]
    titles = data[1]

    # print(labels.map(lambda l: '0' if l == 'e' else l))
    labels = labels.replace({'b': 0, 'e':1, 'm':2, 't':3})

    # 特徴量の抽出
    if clf == None:
        # min_df=1だと12784次元, 2だと7579次元, 3だと5521次元だった 
        clf = CountVectorizer(min_df=min_df)
        clf.fit(titles)

    X = clf.transform(titles)
    df = pd.DataFrame(X.toarray(), columns=clf.get_feature_names())
    df.to_csv(fname + FEATURE_EXTENSION, index=False)

    print('feature count = ' + str(len(clf.get_feature_names())))

    # 正解ラベルのファイルも作成
    labels.to_csv(fname + LABEL_EXTENSION, header=False, index=False)

    return clf

if __name__ == "__main__":
    clf = make_feature('train', min_df=int(sys.argv[1]))
    make_feature('test', clf)
    make_feature('valid', clf)




# import re
# from collections import Counter
# with open(fname) as f:
    # coupus = [l for l in f ]

# p = re.compile(r'[^a-zA-Z0-9\s]')
# with open(fname) as f, \
#     open(wname, mode='w') as w:
#     # トークンの抽出
#     tokens = [token for l in f for token in p.sub('', l.split('\t')[1])]
#     # 出現頻度を数える
#     conuter = Counter(tokens)
#     vocab = conuter.most_common()
#     w.write(''.join(vocab))

    # 
    # counter = Counter()
    # for l in f:
    #     line_sp = l.split('\t')
    #     tokens = p.sub('', line_sp[1])
    #     category = line_sp[4]


    # count vectorizer