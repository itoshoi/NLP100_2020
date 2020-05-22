import NLP100_20
'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''

import re

def get_template_dict():
    data = NLP100_20.load()

    # p = re.compile(r'基礎情報.*?\|(.+?)\s*=\s*(.+?)\n\|', re.DOTALL)
    p = re.compile(r'\{\{基礎情報.*?\n(.+?\n)\}\}', re.DOTALL)
    template = p.findall(data)[0]

    p = re.compile(r'\|(.+?)\s*=\s*(.+?(\n\*.+?)*)\n', re.DOTALL)

    dictionary = {}
    for l in p.findall(template):
        dictionary[l[0]] = l[1]
    
    return dictionary

if __name__ == "__main__":
    dictionary = get_template_dict()
    for k, v in dictionary.items():
        print('{key}: {value}'.format(key=k, value=v))