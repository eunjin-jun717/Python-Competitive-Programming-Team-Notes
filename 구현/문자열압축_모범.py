#p323
#문자열압축_모범답안

def solution(s):
  # step 압축단위 한개씩 늘려가며 확인
  for step in range(1,len(s)//2+1):
    compressed =""
    prev = s[0:step]
    count = 1
    # step만큼 늘려가며 이전 문자열과 비교
    for j in range(step, len(s), step):
      # 이전 상태와 동일하다면 압축 횟수 증가
      if prev == s[j:j+step]:
        count += 1
      # 다른 문자열이 나왔다면
      else:
        compressed += str(count) + prev if count >=2 else prev
        count = 1
    # 남아있는 문자열에 대해서 처리
    compressed += str(count) + prev if count>=2 else prev
    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compressed))
return answer
  
  
  
    
      
      

