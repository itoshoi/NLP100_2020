'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）
を除去してテキストに変換せよ（参考: マークアップ早見表）．
'''

import re
import NLP100_25


def get_template_no_emphasis():
    dict = NLP100_25.get_template_dict()
    for k, v in dict.items():
        p = re.compile(r'\'{2,5}', re.MULTILINE)
        dict[k] = p.sub('', v)
    return dict


if __name__ == "__main__":
    dict = get_template_no_emphasis()
    for k, v in dict.items():
        print('{key}: {value}'.format(key=k, value=v))
