#p118
#게임개발_모범답안
#포인트는 현재 포인트가 보는 방향과 n*m배열을 따로 설정하는 거/ 왼쪽방향으로 도는 함수를 따로 만드는 것

n,m = map(int,input().split())# nxm 행렬
d = [[0]*m for _ in range(n)]

x, y, direction = map(int,input().split()) # (a,b):현재위치, d:바라보는 방향(북동남서:0123)
d[x][y] = 1 #현재위치 방문 처리 

#전체 맵 정보 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전하는 함수
def turn_left():
  global direction
  direction -= 1 # 반시계 방향 회전
  if direction == -1: # 북쪽 방향(0)인 경우
    direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0 
while True:
  # 왼쪽으로 회전 (1단계)
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  #회전한 이후 정면에 가보지 않은 칸이 존재하면 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0: #현재 위치의 왼쪽 방향에 가보지 않은 곳이면서 입력받은 맵의 정보에서 가보지 않은 곳이라면 감
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  #네 방향 모두 갈 수 없는 곳이라면 
  if turn_time == 4: # 4방향 모두 돌아봤는다는 뜻이므로 갈 수 없다는 뜻
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다일 경우
    else:
      break
    trun_time = 0

print(count)
