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