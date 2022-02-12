#p315
#볼링공 고르기

N,M = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0 #볼링공 조합
s = 1 #이미 계산했던 경우 제외하기 위해 start변수를 만듦

for i in range(N): 
  for j in range(s,N): #계산 했던 경우 제외고 시작
    if data[i] != data[j]: #현재 볼링공과 다음 볼링공의 무게가 다를 때
      cnt += 1 #볼링공의 조합 1씩 올림
  s += 1 #계산한 경우 제외하기 위해 1씩올림

print(cnt)
    
