import NLP100_20
import re

def get_template_dict():
    data = NLP100_20.load()

    # p = re.compile(r'基礎情報.*?\|(.+?)\s*=\s*(.+?)\n\|', re.DOTALL)
    p = re.compile(r'\{\{基礎情報.*?\n(.+?\n)\}\}', re.DOTALL)
    template = p.findall(data)[0]

    p = re.compile(r'\|(.+?)\s*=\s*(.+?(\n\*.+?)*)\n', re.DOTALL)

    dict = {}
    for l in p.findall(template):
        dict[l[0]] = l[1]
    
    return dict

if __name__ == "__main__":
    dict = get_template_dict()
    for k, v in dict.items():
        print('{key}: {value}'.format(key=k, value=v))