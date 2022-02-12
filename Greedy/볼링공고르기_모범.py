#p315
#볼링공 고르기
#모범 답안
# 1)무게마다 볼링공이 몇개있는지르 먼저 계산한다.
# 2)A를 기준으로 무게가 낮은 볼링공부터 무게가 높은 볼링공까지 순서대로 하나씩 확인한다

n, m = map(int, input().split())
data = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 List 생성
array = [0]*11

for x in data:
  # 각 무게에 해당하는 볼링공의 개수 카운트
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
  n -= array[i] #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += array[i]*n #B가 선택하는 경우의 수와 곱하기

print(result)
