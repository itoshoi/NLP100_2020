'''
59. ハイパーパラメータの探索Permalink
学習アルゴリズムや学習パラメータを変えながら，カテゴリ分類モデルを学習せよ．
検証データ上の正解率が最も高くなる学習アルゴリズム・パラメータを求めよ．
また，その学習アルゴリズム・パラメータを用いたときの評価データ上の正解率を求めよ．
'''

import NLP100_5x_util as myutil
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def search_hyper_params(fname):
    tols = np.logspace(0, 2, 10)
    lrs = [myutil.learn(fname, tol=tol) for tol in tqdm(tols)]

    valid_accs = [myutil.accuracy(lr, 'valid') for lr in lrs]
    test_accs = [myutil.accuracy(lr, 'test') for lr in lrs]
    train_accs = [myutil.accuracy(lr, 'train') for lr in lrs]

    plt.plot(tols, train_accs, label = '学習')
    plt.plot(tols, valid_accs, label = '検証')
    plt.plot(tols, test_accs, label = '評価')
    plt.xscale('log')
    plt.legend()
    plt.savefig('NLP100_59_result.png')
    plt.show()

if __name__ == "__main__":
    search_hyper_params('train')