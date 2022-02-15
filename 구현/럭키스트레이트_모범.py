#p321
#럭키스트레이트
#모범답안
#포인트는 한 배열로 해결한 점, 나는 따로 배열을 만들어서 썼지만 이 답안에서는 한 배열에서 오른쪽부분과 왼쪽부분을 빼며 0 이된다는 식을 사용함

n = input()
length = len(n) # 값의 총 자릿수
summary = 0

#왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
  summary += int(n[i])

#왼쪽부분 자릿수값 더한 결과값에서 오른쪽부분 자릿수값 더한 결과 뺴기
for i in range(length//2, length):
  summary -= int(n[i])

# 결과값이 0이면 둘은 같은 자릿수의 합을 가졌다는 의미
if summary == 0:
  print('LUCKY')
else:
  print('READY')


