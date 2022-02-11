#문제 3-6
#모범답안

N,K = map(int, input().split())

result=0

while True:
  #N이 K로 나누어 떨어지는 수가 될때 까지 빼기
  target = (N//K) * K #나머지가 0이되도록하는 가장 가까운 값을 target으로 잡음
  result += (N-target) #1 빼는 횟수를 한번에 더해줌
  N = target
  # N이 K보다 작을 때(더이상 나눌수 없을때) 반복문 탈출
  if N<K:
    break
  result += 1 #K를 나누는 연산
  N //= K

#마지막으로 남은 수에 대하여 1씩 빼기
result += (N-1)
print(result)
