with open("input.txt") as inp:
    lines = [line.strip() for line in inp]

scores = {                
              ')' : 3, 
              ']' : 57, 
              '}' : 1197, 
              '>' : 25137
              }

opening_partner = {                
              ')' : '(', 
              ']' : '[', 
              '}' : '{', 
              '>' : '<'
              }

score = 0
for line in lines:
    stack = []
    for char in line:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            if stack[-1] == opening_partner[char]:
                stack.pop()
            else:
                score += scores[char]
                break
            #closing character
            # if chunks[opening_partner[char]] == 0:
            #     score += scores[char]
            #     print(char, i, line)
            #     break
            # else:
            #     chunks[opening_partner[char]] -= 1

print(score)