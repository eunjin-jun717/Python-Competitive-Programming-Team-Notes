#p110
#상하좌우_모범답안
## 여기서 나의 문제점은 LRUD에 따른 좌표 움직임을 따로 담지 않고 바로 적용시켰기 때문에 배열 공간을 벗어나는 걸 확인하기가 어려웠다. 따라서 느낀점은 if continue를 잘 활용하자

n = int(input())
x ,y = 1, 1 # 현재 위치
plans = input().split() # 경로

# L, R, U, D
dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]
# move types
move_types = ['L','R','U','D']

for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]: #move type에 따른 좌표 움직임
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n: # 1~n 배열 공간을 벗어나는 경우 무시
    continue
  x, y = nx, ny 
print(x, y)
