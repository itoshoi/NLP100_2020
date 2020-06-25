'''
66. WordSimilarity-353での評価Permalink
The WordSimilarity-353 Test Collectionの評価データをダウンロードし，
単語ベクトルにより計算される類似度のランキングと，人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''
import sys
from tqdm import tqdm
import pandas as pd
from gensim.models import KeyedVectors
from scipy.stats import spearmanr

# argv[1] = model file path, argv[2] = human word similarity file path
model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=True)
df = pd.read_csv(sys.argv[2])

# 新しくカラムを追加
col_name = 'W2V Similarity'
df[col_name] = 0.0

# 類似度を計算
for i in range(df.count()[0]):
    df[col_name][i] = model.similarity(df['Word 1'][i], df['Word 2'][i])

# dfを出力
print(df)
df.to_csv('NLP100_66_df.csv', index=False, sep='\t')

# スピアマン相関係数を計算
print(spearmanr(df['Human (mean)'], df[col_name]))
