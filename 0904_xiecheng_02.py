def AUC(label, pre):

    pos = [i for i in range(len(label)) if label[i] == 1]
    neg = [i for i in range(len(label)) if label[i] == 0]

    auc = 0
    for i in pos:
     for j in neg:
        if pre[i] > pre[j]:
            auc += 1
        elif pre[i] == pre[j]:
            auc += 0.5
    return auc / (len(pos) * len(neg))

n = int(input())
data = []
for _ in range(n):
    data.append(list(input().strip().split()))

label = []
pre = []
for i in range(len(data)):
    a = int(data[i][0])
    label.append(a)
    b = float(data[i][1])
    pre.append(b)

print(AUC(label,pre))