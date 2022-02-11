#p312
#곱하기혹은더하기
#모범답안

data = input()

result = int(data[0]) # 첫번째 문자 숫자로 변경하여 대입

for i in range(1, len(data)):
  # 다음값과 현재의결과값 하나라도 0 혹은 1인 경우, 곱하기 보다는 더하기 수행
  num = int(data[i]) # 배열의 2번째부터 시작
  if num <= 1 or result <= 1:
    result += num
  else:
    result += num
    
print(result)
