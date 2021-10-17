data = []
count = 0
with open("reviews.txt" ,'r', encoding = 'utf-8') as f:
    for line in f:
        data.append(line)
        count+=1
        if count % 1000 == 0:
            print(len(data))


print(len(data))