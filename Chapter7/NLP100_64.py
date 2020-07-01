'''64. アナロジーデータでの実験Permalink
単語アナロジーの評価データをダウンロードし，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
'''
from gensim.models import KeyedVectors
from gensim.similarities.index import AnnoyIndexer
import sys
from tqdm import tqdm
import os

# argv[1] = model file name, argv[2] = Analogy data file name
# w2vのモデルを読み込む
model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=True)
annoy_indexer = AnnoyIndexer(model, 2)

# fr = Analogy data file, fw = outut file
with open(sys.argv[2], mode='r') as fr, open('NLP100_64_result.txt', mode='w') as fw:
    with tqdm(total=os.path.getsize(sys.argv[2])) as pbar:
        for l in fr:
            l_sp = l.split()
            if l[0] == ':':
                fw.write(l)
            else:
                try:
                    # word, cos = model.most_similar(positive=[l_sp[1], l_sp[2]], negative=[l_sp[0]], topn=1)[0]
                    word, cos = model.most_similar(positive=[l_sp[1], l_sp[2]], negative=[l_sp[0]], topn=1, indexer=annoy_indexer)[0]
                    fw.write(l.replace('\n', '') + ' ' + word + ' ' + str(cos) + '\n')
                except KeyError as error:
                    fw.write(l)
                    print(error)

            pbar.update(len(l.encode('utf-8')))

# なんと1時間40分かかった