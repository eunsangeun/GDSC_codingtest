n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0 #현재 그룹에 포함된 모험가 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)