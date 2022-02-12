#p95
#큰수의 법칙
#반복적 수열을 생각해서 풀기

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수
count = int(m/(k+1)) * k #반복되는 수열 -> 가장큰수 K번, 두번째 큰수 1번를 더한 수열을 m과 계산할 시, 반복되는 수열이 몇번 나눠지는지 알수있음
count += m % (k+1) # 반복되는 수열를 나눈 나머지느 자동으로 가장 큰 수를 더하는 횟수가 되는 것

result += 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second #두번째 큰 수 더하기

print(result)
