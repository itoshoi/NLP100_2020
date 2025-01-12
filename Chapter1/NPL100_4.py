'''
04. 元素記号
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

import re

string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
string_sp = re.findall('[^,. ]+', string)
string_dict = {}

for i in range(len(string_sp)):
    if i == 0 or 4 <= i <= 8 or 14 <= i <= 15 or i== 18:
        string_dict[string_sp[i][0]] = i + 1
    else:
        string_dict[string_sp[i][0:2]] = i + 1

print(string_dict)