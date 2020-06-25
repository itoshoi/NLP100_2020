from gensim.models import KeyedVectors
import sys
from pprint import pprint

'''
60. 単語ベクトルの読み込みと表示Permalink
Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ，300次元）を
ダウンロードし，”United States”の単語ベクトルを表示せよ．
ただし，”United States”は内部的には”United_States”と表現されていることに注意せよ．
'''
# argv[1] = model file name
fname = sys.argv[1]
model = KeyedVectors.load_word2vec_format(fname, binary=True)
print("United_Statesの単語ベクトル")
pprint(model['United_States'])
print()


'''
61. 単語の類似度Permalink
“United States”と”U.S.”のコサイン類似度を計算せよ．
'''
print("United_StatesとU.S.の類似度")
print(model.similarity('United_States', 'U.S.'))
print()


'''
62. 類似度の高い単語10件
“United States”とコサイン類似度が高い10語と，その類似度を出力せよ．
'''
print("United States”とコサイン類似度が高い10語")
pprint(model.most_similar('United_States', topn=10))
print()


'''
63. 加法構成性によるアナロジーPermalink
“Spain”の単語ベクトルから”Madrid”のベクトルを引き，
”Athens”のベクトルを足したベクトルを計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''
# vec = model['Spain'] - model['Madrid'] + model['Athens']
print('Spain - Madrid + Athens と類似度の高い10語')
pprint(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid']))
print()