#문제 3-6
#모범답안

N,K = map(int, input().split())

result=0

while True:
  #N이 K로 나누어 떨어지는 수가 될때 까지 빼기
  target = (N//K) * K
  result += (N-target)
  N = target
  # N이 K보다 작을 때(더이상 나눌수 없을때) 반복문 탈출
  if N<K:
    break
  result += 1
  N //= K

#마지막으로 남은 수에 대하여 1씩 빼기
result += (N-1)
print(result)
