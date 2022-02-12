#p311
#모험가 길드
#모범 답안

n = int(input())
data = list(map(int, input().split()))
data.sort()

num_group = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data:
  count+=1 #현재 그룹부터 해당 모험가를 포함시키기
  if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹을 결성
    num_group += 1 #총 그룹 수 증가시킴
    count = 0 #현재 그룹의 모험가 수 초기화
print(num_group)
