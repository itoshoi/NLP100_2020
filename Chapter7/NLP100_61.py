from gensim.models import word2vec
import sys

# モデルファイルの指定
fname = sys.argv[1]
# モデルの読み込み
model = word2vec.Word2Vec.load(fname)

