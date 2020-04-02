string1 = "パトカー"
string2 = "タクシー"
result = ''
for i in range(len(string1 + string2)):
    result += string1[int(i / 2)] if i % 2 == 0 else string2[int(i / 2)]
print(result)

result2 = ''
for i in range(len(string1)):
    result2 += string1[i] + string2[i]
print(result2)