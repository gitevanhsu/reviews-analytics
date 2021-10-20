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

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

good = []
for g in data:
    if 'good' in g:
        good.append(g)
print('一共有', len(good), '筆留言提到good')
print(good[0])

# 文字計數
wc = {} # word_count

for d in data:
    words = d.split()
    for word in words:
        if  word in wc :
            wc[word] += 1
        else:
            wc[word] = 1

while True:
    word = input('請問你想查什麼字:')
    if word == 'q': 
        break
    if word in wc:
        print(word, '共出現', wc[word], '次。')
    else:
        print('查無此字。')

print('感謝使用本查詢功能。')

