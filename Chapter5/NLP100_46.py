'''
46. 動詞の格フレーム情報の抽出Permalink
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． 
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
'''

import NLP100_41
import sys

fname = sys.argv[1]
sentence_list = NLP100_41.get_chunk_sentence_list(fname)

for sentence in sentence_list:
    for chunk in sentence:
        for morph in chunk.morphs:
            if morph.pos == "動詞":
                result = morph.base + "\t"
                # 雑実装
                # 係り元の文節に含まれる助詞を抽出 (文節中に助詞がないと空文字になるためfilterで除去)
                result += " ".join(filter(lambda l: l != "", ["".join(
                    [m.surface for m in sentence[i].morphs if m.pos == "助詞"]) for i in chunk.srcs]))
                result += "\t"
                # 同様に文節ごと抽出
                result += " ".join(filter(lambda l: l != "", ["".join(
                    set([sentence[i].get_morphs_surface() for m in sentence[i].morphs if m.pos == "助詞"])) for i in chunk.srcs]))
                print(result)
