from operator import itemgetter

def solution(food_times, k):
    foods = [] #음식 시간과 음식 번호를 함께 저장할 list 생성
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1)) #tuple: 음식시간, 음식번호

    foods.sort() #tuple을 정렬할 때 첫번째 값부터 오름차순함 따라서 음식시간 양 순서로 정렬되게 함

    pretime = 0
    for i, food in enumerate(foods):
        diff = food[0] - pretime #첫번째 음식을 먹는데 필요한 시간 #food[0]은 튜플에서 첫번째 음식시간에 해당
        if diff != 0: #차이가 있다면
            spend = diff * n #높이*가로 
            if spend <= k: #k보다 소비되 시간이 작으면
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k][1] #sublist의 k번째에서 '음식번호' 리턴
        n -= 1

    return -1
