#p96
#숫자카드게임
#min()함수를 이용하는 방법

n,m = map(int, input().split())

result = 0 #

#한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  min_value=min(data) #현재 줄에서 가장 작은 수 찾기
  result =max(result, min_value) #'가장 작은수'들 중에서 가장 큰 수 찾기

print(result)
