#그리디
#화폐의 종류: K/ 시간복잡도: O(K)
#시간복잡도는 거슬러줘야하는 금액과는 무관, 동전의 총 종류에만 영향

n = 1260

count = 0

a = [500,100,50,10]

for coin in a:
  count += n//coin #동전의 갯수
  n %= coin #나머지 값으로 총액 업데이트

print(count)
