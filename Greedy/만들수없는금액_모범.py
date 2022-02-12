#p314
#만들수없는금액
#화폐단위 기준으로 오름차순으로 정렬한 뒤 1부터 차례대로 특정한 금액을 만들 수 있는지 확인하며 됨

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1 #가장 작은 화폐 단위 1부터 시작

for new in data:
  #새로운 화폐단위가 가장 작은 화폐 단위라고 가정하는 target보다 작다면 가지고 있는 화폐단위로는 만들 수 없다는 뜻이므로 반복을 종료하게 된다
  if target < new: 
    break 
  target += new

print(target)
