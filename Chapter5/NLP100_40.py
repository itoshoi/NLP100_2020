"""
40. 係り受け解析結果の読み込み（形態素）Permalink
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

fname = "neko.txt.cabocha"


class Morph:
    surface = ""
    base = ""
    pos = ""
    pos1 = ""

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def get_sentence_list():
    with open(fname) as f:
        result_list = []
        sentence = []
        for line in f:
            if line == "EOS\n" and 0 < len(sentence):
                result_list.append(sentence[:])
                sentence.clear()
                continue
            line_sp_tab = line.split('\t')
            if len(line_sp_tab) < 2:
                continue
            line_sp_comma = line_sp_tab[1].split(',')
            morph = Morph(line_sp_tab[0], line_sp_comma[6],
                          line_sp_comma[0], line_sp_comma[1])
            sentence.append(morph)
    return result_list

if __name__ == "__main__":
    morphList = get_sentence_list()
    for morph in morphList[2]:
        print(morph.surface)