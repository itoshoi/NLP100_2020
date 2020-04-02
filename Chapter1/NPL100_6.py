import NPL100_5

test_str1 = "paraparaparadise"
test_str2 = "paragraph"

X = NPL100_5.string_bi_gram(test_str1)
Y = NPL100_5.string_bi_gram(test_str2)
set_X = set(X)
set_Y = set(Y)

print("X")
print(X)
print("Y")
print(Y)

print("Set X")
print(set_X)
print("Set Y")
print(set_Y)

print("Union")
print(set_X | set_Y)
print("Intersection")
print(set_X & set_Y)
print("Difference")
print(set_X - set_Y)

print("'se' in X ?")
print('se' in set_X)
print("'se' in Y ?")
print('se' in set_Y)

print("Omake")
print(set(['se']) <= set_X)