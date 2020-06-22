"""
41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import NLP100_40

class Chunk:
    morphs = []
    dst = -1
    srcs = []

    def __init__(self):
        self.morphs = []
        self.srcs = []
        # 係り先がないときは-1
        self.dst = -1

    def get_morphs_surface(self):
        return "".join([morph.surface for morph in self.morphs if morph.pos != '記号'])

def get_chunk_sentence_list(fname):
    result_list = []
    sentence = []
    with open(fname) as f:
        for line in f:
            # EOSが出てきたら1文とする
            # if line == "EOS\n" and 0 < len(sentence):
            if line == "EOS\n":
                # 係り元を設定
                for i in range(len(sentence)):
                    chunk = sentence[i]
                    if chunk.dst != -1:
                        sentence[chunk.dst].srcs.append(i)
                result_list.append(sentence[:])
                sentence.clear()
            # *が出てきたらchunkを新しくする
            elif line[0] == "*":
                chunk = Chunk()
                chunk.dst = int(line.split(' ')[2].replace('D', ''))
                sentence.append(chunk)
            # それ以外は形態素
            else:
                line_sp_tab = line.split('\t')
                if len(line_sp_tab) < 2:
                    continue
                line_sp_comma = line_sp_tab[1].split(',')
                morph = NLP100_40.Morph(line_sp_tab[0], line_sp_comma[6],
                            line_sp_comma[0], line_sp_comma[1])
                sentence[-1].morphs.append(morph)
    return result_list

if __name__ == "__main__":
    import sys
    from pprint import pprint
    fname = sys.argv[1]
    chunk_sentence_list = get_chunk_sentence_list(fname)
    # for chunk_sentence in chunk_sentence_list:
        # for chunk in chunk_sentence:
            # print("".join([morph.surface for morph in chunk.morphs]))
            # print("dst={}, srcs={}".format(chunk.dst, chunk.srcs))

    # for chunk in chunk_sentence_list[5]:
    for chunk in chunk_sentence_list[7]:
        print("".join([morph.surface for morph in chunk.morphs]))
        print("dst={}, srcs={}".format(chunk.dst, chunk.srcs))
        print()