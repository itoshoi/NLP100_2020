'''
53. 予測Permalink
52で学習したロジスティック回帰モデルを用い，与えられた記事見出しからカテゴリと
その予測確率を計算するプログラムを実装せよ．
'''
# import NLP100_52
import sys
import pandas as pd
import pickle
import NLP100_5x_util as myutil

def predict(lr, predict_fname):
    # feature_df = pd.read_csv(predict_fname + NLP100_52.FEATURE_EXTENSION)
    feature_df = myutil.load_features(predict_fname)
    # 確率の予測
    out = lr.predict_proba(feature_df)
    preds = out.argmax(axis=1)
    probs = out.max(axis=1)
    return preds, probs

if __name__ == "__main__":
    # argv[1] = pickle file name, argv[2] = predict file name
    with open(sys.argv[1], mode='rb') as fp:
        clf = pickle.load(fp)
    preds, prods = predict(clf, sys.argv[2])

    # 結果の表示
    result_df = pd.DataFrame([[y, p] for y, p in zip(preds, prods)], columns = ['予測', '確率'])
    result_df.to_csv('NLP100_53_result.csv', sep='\t', index=None)
