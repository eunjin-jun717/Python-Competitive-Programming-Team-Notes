#p322
#문자열 재정렬
#이 문제를 풀기위해서는 isalpha 함수와 최종결과를 출력하기위해 리스트 문자열을 합치는 함수인 'join'을 알아야함
 
data = input()
result = [] # 문자열을 담을 리스트
value = 0 # 숫자의 합을 담을 변수

# 입력의 문자를 하나씩 확인함
for x in data:
  if x.isalpha(): # 알파벳일 경우
    result.append(x)
  else: # 숫자인 경우 합 계산
    value += int(x)

# 알파벳 오름차순
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

#최종결과를 출력(리스트->문자열)
print(''.join(result)) #공백없이 문자열 리스트를 쭉 일렬로 나열해서 출력
