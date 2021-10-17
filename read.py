data = []
count = 0
with open("reviews.txt" ,'r', encoding = 'utf-8') as f:
    for line in f:
        data.append(line)
        count += 1


print('讀取完了總共有', len(data), '筆資料')
total = 0
for i in range(len(data)):
    total += len(data[i])
print(total)
print("留言平均長度為：", total / len(data))
