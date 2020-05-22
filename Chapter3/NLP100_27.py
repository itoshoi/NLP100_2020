'''
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ（参考: マークアップ早見表）．
'''

import NLP100_26
import re

def get_template_no_emphasis_markup():
    dict = NLP100_26.get_template_no_emphasis()
    p = re.compile(r'''
        \[\[            # [[からスタート
        (?!ファイル)    # ファイル以外の文字列
        (?:[^|]*?\|)??  # (|を含まない文字列)| の0か1回出現
        ([^|]*?)        # |を含まない文字列(非貪欲)
        \]\]            # ]]で終わり
    ''', re.MULTILINE + re.VERBOSE)
    for k, v in dict.items():
       dict[k] = p.sub(r'\1', v)
    return dict

if __name__ == "__main__":
    dict = get_template_no_emphasis_markup()
    for k, v in dict.items():
        print('{key}: {value}'.format(key=k, value=v))