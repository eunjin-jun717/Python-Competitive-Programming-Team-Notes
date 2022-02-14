#p115
#왕실의나이트
#상하좌우와 비슷한 문제
# 여기서 포인트는 문자로 입력받은 것을 아스키코드로 변환해서 'a'의 아스키코드 숫자로 변환 뒤 빼서 1을 더한다.
# 해당 위치의 범위 안에 있늕 확인만 한다면 다 된 문제!

#현재 나이트의 위치 입력받기
input_data = input() #ex) c2
row = int(input_data[1]) #행: 숫자
column = int(ord(input_data[0])- int(ord('a')))+1 # 아스키코드로 변환후 'a'의 아스키코드로 빼면된다

# 나이트가 이동할 수 있는 8가지 steps
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] #(row, column)

result =0
for step in steps:
  # 나이트가 이동가능한 좌표들(8방향) 하나씩 갈 수 있는지 확인해봄
  next_row = row+step[0]
  next_column = column + step[1]
  #해당위치로 이동이 가능하다면 카운트 증가
  if next_row >=1 and next_row <=8 and next_column >=1 and next_column<= 8:
    result += 1
print(result)
