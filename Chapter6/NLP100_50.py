import sys
import random
import collections

fname = sys.argv[1]

data = []
PUBLISHERS = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
with open(fname) as f:
    data = [l.split('\t')[4] + '\t' + l.split('\t')[1] for l in f if l.split('\t')[3] in PUBLISHERS]
random.shuffle(data)

data_len = len(data)
train_data = data[:int(data_len * 0.8)]
valid_data = data[int(data_len * 0.8) : int(data_len * 0.9)]
test_data = data[int(data_len * 0.9) : ]

with open('train.txt', mode='w') as w1, \
    open('valid.txt', mode='w') as w2, \
        open('test.txt', mode='w') as w3:
    w1.write("\n".join(train_data))
    w2.write("\n".join(valid_data))
    w3.write("\n".join(test_data))

# print("train {}".format(collections.Counter([l.split('\t')[4] for l in train_data])))
# print("valid {}".format(collections.Counter([l.split('\t')[4] for l in valid_data])))
# print("test {}".format(collections.Counter([l.split('\t')[4] for l in valid_data])))

# pandasを使うともっと簡単にできる
# sklearnを使うともっと簡単にできる