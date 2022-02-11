# p312
# 곱하기 혹은 더하기

n = input()

a = list(map(int, n)) #int변환

result = a[0] #처음 값을 result에 저장한 뒤 시작

for i in range(len(n)-1): 
  if a[i+1]<=1 or result<= 1: #다음값과 현재 결과값이 0 혹은 1이라면, 더하기 수행
    result += a[i+1]
  else:
    result *= a[i+1]

print(result)
