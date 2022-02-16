#p323
#문자열압축
#카카오_프로그래머스 풀이 참고

def compress(text, tok_len):
  words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)] #단어 단위마다 자른 배열
  res = []
  cur_word = words[0]
  cur_cnt = 1
  for a,b in zip(words, words[1:]+['']):
    if a==b:
      cur_cnt += 1
    else: #다른 단어가 나오면
      res.append([cur_word, cur_cnt])
      cur_word = b
      cur_cnt =1 
  return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
