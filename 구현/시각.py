#p114
#시각
#이 문제의 포인트는 시간을 1씩 올려서 확인해도 시,분,초 모든 경우의 수가 24*60*60 =86,400번 밖에 수행되지 않으므로 빠른 계산이 가능하다는 점이다. 파이썬은 1초에 천만번 수행이 가능하기 때문에 
# 굉장히 안정적인 범위 안에 들어와있다느 점이다
# if 문자 in 문자열 을 사용하면 문자열에'문자'가 포함되어있는 경우르 뜻한다. 

h = int(input())

count =0
# 00시 00분 00초 부터 23시 59분 59초까지 1초씩 늘려서 확인하는 것!
for i in range(h+1): # hour
  for j in range(60): # min
    for k in range(60): # second
      # 만약 문자열에 '3'이 포함되어 있다면 count를 1씩 증가시킨다
      if '3' in str(i) + str(j) + str(k):
        count+=1
print(count)
      
