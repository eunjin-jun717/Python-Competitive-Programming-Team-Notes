#p313
#문자열뒤집기
#0에서 1로, 1에서 0으로 바뀌는 경우만 볼 것

data = input()

group0 = 0 #0으로 바꾸는 경우
group1 = 0 #1로 바꾸는 경우

if data[0] == '0': #첫번째 원소가 0일 때 '0으로 바꾸는 경우' 1증가
  group0 += 1
else: #첫번째 원소가 1일 경우
  group1 += 1
  
# 두번째 원소부터 모든원소 확인
for i in range(len(data)-1):
  if data[i] != data[i+1]: #현재수와 다음에 올 수가 다르지 않을 때
    # 다음의 수에서 1로 바뀌는 경우
    if data[i+1] == '1':
      group1 += 1
    else: #0으로 바뀌는 경우
      group0 += 1

print(min(group0, group1))
    
    

