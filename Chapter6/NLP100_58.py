'''
58. 正則化パラメータの変更Permalink
ロジスティック回帰モデルを学習するとき，正則化パラメータを調整することで，
学習時の過学習（overfitting）の度合いを制御できる．
異なる正則化パラメータでロジスティック回帰モデルを学習し，
学習データ，検証データ，および評価データ上の正解率を求めよ．
実験の結果は，正則化パラメータを横軸，正解率を縦軸としたグラフにまとめよ．
'''

import matplotlib.pyplot as plt
import numpy as np
import NLP100_5x_util as myutil
from tqdm import tqdm

def show_C_graph():
    Cs = np.arange(0.1, 1.1, 0.1)
    lrs = [myutil.learn('train', C) for C in tqdm(Cs)]

    valid_accs = [myutil.accuracy(lr, 'valid') for lr in lrs]
    test_accs = [myutil.accuracy(lr, 'test') for lr in lrs]
    train_accs = [myutil.accuracy(lr, 'train') for lr in lrs]

    plt.plot(Cs, valid_accs, label='Valid')
    plt.plot(Cs, test_accs, label='Test')
    plt.plot(Cs, train_accs, label='Train')
    
    plt.savefig('NLP100_58_result.png')
    # test_accs = lrs


if __name__ == "__main__":
    show_C_graph()