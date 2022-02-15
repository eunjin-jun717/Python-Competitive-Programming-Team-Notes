#p321
#럭키스트레이트

n = input()
mid = int(len(n)/2) #짝수 입력값만 들어오기 때문에 나눌 위치는 반으로 나눔

array1 = n[:mid]
array2 = n[mid:]

array1_sum, array2_sum = 0, 0

for i in range(len(array1)): # 양쪽 같은 길이를 가지므로 한개의 배열길이만 사용
  array1_sum += int(array1[i])
  array2_sum += int(array2[i])

if array1_sum == array2_sum:
  print('LUCKY')
else:
  print('READY')
