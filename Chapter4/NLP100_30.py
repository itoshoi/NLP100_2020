"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab

fname = "neko.txt.mecab"

def get_morpheme():
    with open(fname) as f:
        result_list = []
        for line in f:
            line_sp_tab = line.split('\t')
            if len(line_sp_tab) < 2:
                continue
            line_sp_comma = line_sp_tab[1].split(',')
            morpheme = {
                'surface':line_sp_tab[0],
                'base':line_sp_comma[6],
                'pos':line_sp_comma[0],
                'pos1':line_sp_comma[1]
            }
            result_list.append(morpheme)
        return result_list

if __name__ == "__main__":
    for morpheme in get_morpheme():
        print(morpheme)