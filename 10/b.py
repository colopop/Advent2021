with open("input.txt") as inp:
    lines = [line.strip() for line in inp]

scores = {                
          ')' : 1, 
          ']' : 2, 
          '}' : 3, 
          '>' : 4
         }

opening_partner = {                
              ')' : '(', 
              ']' : '[', 
              '}' : '{', 
              '>' : '<'
              }

closing_partner = {                
              '(' : ')', 
              '[' : ']', 
              '{' : '}', 
              '<' : '>'
              }

score_list = []
for line in lines:
    line_score = 0
    stack = []
    corrupted = False
    for char in line:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            if stack[-1] == opening_partner[char]:
                stack.pop()
            else:
                corrupted = True
                break
    if not corrupted:
        for char in reversed(stack):
            line_score *= 5
            line_score += scores[closing_partner[char]]
        score_list.append(line_score)

score_list.sort()
print(score_list[len(score_list) // 2])