#p93
#큰수의 법칙
#단순하게 푸는 방법

n,m,k= map(int,input().split())
data = list(map(int, input().split()))

data.sort() #오름차순 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

result = 0 #결과값

while True:
  for i in range(k): #가장 큰 수 K번 더하기
    if m == 0: #m이 0이면 반복문 탈출
      break
    result += first #가자 큰 수 더해주기
    m -= 1 #한 번 더한거 빼기
  if m==0:
    break
  result += second #두번째 큰 수는 한번 빼주기
  m -= 1
  
print(result)
