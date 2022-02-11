#문제 3-6
#N이 1이 될 때까지
#내답안

N,K = map(int, input().split())

cnt = 0 # 결과값 초기화
 
while N!=1: #N이 1이되며 탈출
  if N%K==0: #나머지가 0이며 1을 빼는 계산 하지 않아도 됨
    N = N//K #N,K의 몫을 다시 N에 넣음
  else: #나머지가 0이 아닐땐 1을 빼줌
    N -= 1
  cnt+=1 # 결과 수행 횟수 1번 올리기

print(cnt)
