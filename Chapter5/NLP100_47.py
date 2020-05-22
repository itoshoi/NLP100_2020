'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
'''

import NLP100_41
import sys

fname = sys.argv[1]
sentence_list = NLP100_41.get_chunk_sentence_list(fname)

for sentence in sentence_list:
    for chunk in sentence:
        for mIndex in range(len(chunk.morphs) - 1):
            morph0 = chunk.morphs[mIndex]
            morph1 = chunk.morphs[mIndex+1]

            if morph0.pos1 == "サ変接続" and morph1.surface == "を":
                for morph in sentence[chunk.dst].morphs:
                    if morph.pos == "動詞":
                        verb_chunk = sentence[chunk.dst]
                        result = morph0.surface + morph1.surface + morph.base + "\t"
                        # 雑実装
                        # 係り元の文節に含まれる助詞を抽出 (文節中に助詞がないと空文字になるためfilterで除去)
                        result += " ".join(filter(lambda l: l != "", ["".join(
                            [m.surface for m in sentence[i].morphs if m.pos == "助詞"]) for i in verb_chunk.srcs]))
                        result += "\t"
                        # 同様に文節ごと抽出
                        result += " ".join(filter(lambda l: l != "", ["".join(
                            set([sentence[i].get_morphs_surface() for m in sentence[i].morphs if m.pos == "助詞"])) for i in verb_chunk.srcs]))
                        print(result)
