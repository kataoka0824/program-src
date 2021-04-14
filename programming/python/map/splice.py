def toprove(a):
    c = {}
    for x in a:
        if x in c:
            c[x] = c[x] + 1
        else:
            c[x] = 1
    best = 0
    bestn = 0
    for x in c.keys():
        if c[x] > bestn:
            best = x
            bestn = c[x]
    return best

import csv
with open("splice.data") as fp:
    table = list(csv.reader(fp))

for row in table:
    # 2列目の空白を除去。
    row[2] = row[2].strip()

# シャッフル後、訓練データとテストデータを作成。
import random
random.shuffle(table)
train = table[:-1000]
test = table[-1000:]

# 2種類の素性の組み合わせをすべて試す。
i1=0
j1=0
score1=0
for i in range(59):
    for j in range(59):
        if i < j:
            # i文字目とj文字目の素性を使った決定木を作成。
            c = {}
            for row in train:
                answer = row[0]  # 回答
                seq = row[2]     # 塩基配列
                f1 = seq[i:i+2]  # i文字目の素性
                f2 = seq[j:j+2]  # j文字目の素性
                f = f1+","+f2    # 連結した素性
                if not (f in c):
                    c[f] = []
                c[f].append(answer)
            rule = {}
            for f in c.keys():
                rule[f] = toprove(c[f])

            score = 0
            for row in test:
                answer = row[0]  # 回答
                seq = row[2]     # 塩基配列
                f1 = seq[i:i+2]  # i文字目の素性
                f2 = seq[j:j+2]  # j文字目の素性
                f = f1+","+f2    # 連結した素性                        
                if (f in rule) and (rule[f] == answer):
                    score = score + 1
            print("使った素性: {} {} スコア:{}".format(i+1,j+1,score))
            if score1<score:
                score1=score
                i1=i+1
                j1=j+1
print("max使った素性: {} {} maxスコア:{}".format(i1,j1,score1))

