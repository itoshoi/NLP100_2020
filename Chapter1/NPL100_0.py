'''
00. 文字列の逆順Permalink
文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''

string = "stressed"
print(''.join(list(reversed(string))))

result = ''
for i in range(len(string)):
    result += (string[-i - 1])
    
print(result)

# print(string[::-1])でも可能