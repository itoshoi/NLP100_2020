'''
65. アナロジータスクでの正解率Permalink
64の実行結果を用い，意味的アナロジー（semantic analogy）と
文法的アナロジー（syntactic analogy）の正解率を測定せよ．
'''
import sys

# argv[1] = NLP100_64 result file path
fname = sys.argv[1]

SEMANTICALLY_KEY = 'semantic'
SYNTACTIC_KEY = 'syntactic'

# 意味的、文法的アナロジーの正解数と合計数
correct_count = {SEMANTICALLY_KEY:0, SYNTACTIC_KEY:0}
sum_count = {SEMANTICALLY_KEY:0, SYNTACTIC_KEY:0}

with open(fname) as f:
    # 現在処理中の行が意味的アナロジーか文法的アナロジーか
    target_analogy = SEMANTICALLY_KEY
    for l in f:
        l_sp = l.split()
        if l_sp[0] == ':':
            # gramで始まるカテゴリーは文法的アナロジーとする
            target_analogy = SYNTACTIC_KEY if l_sp[1].startswith('gram') else SEMANTICALLY_KEY
        else:
            sum_count[target_analogy] += 1
            correct_count[target_analogy] += 1 if l_sp[3] == l_sp[4] else 0

print('意味的アナロジー正解率 ' + str(correct_count[SEMANTICALLY_KEY] / sum_count[SEMANTICALLY_KEY]))
print('文法的アナロジー正解率 ' + str(correct_count[SYNTACTIC_KEY] / sum_count[SYNTACTIC_KEY]))
