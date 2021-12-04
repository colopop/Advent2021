class Board:
    def __init__(self, numbers):
        self.board = [[[n, False] for n in line] for line in numbers]
        self.numbers = set()
        for line in numbers:
            self.numbers &= set(line)

    def mark_number(self, number):
        for line in self.board:
            for pair in line:
                if pair[0] == number:
                    pair[1] = True
                    #print("marked {}".format(number))

    def check_victory(self):
        #check rows
        for row in self.board:
            if all(pair[1] for pair in row):
                return True
        #check columns
        for i in range(len(row[0])):
            if all(pair[1] for pair in [row[i] for row in self.board]):
                return True
        return False

    def score(self):
        ans = 0
        for row in self.board:
            for pair in row:
                if not pair[1]:
                    ans += pair[0]
        return ans

with open("input.txt") as inp:
    numbers = [int(num) for num in inp.readline().split(",")]
    boards = []
    while inp.readline():
        boards.append(Board([[int(i) for i in inp.readline().split()] for _ in range(5)]))

for number in numbers:
    for board in boards:
        #print(number, board.board)
        board.mark_number(number)
        if board.check_victory():
            print(board.score() * number)
            break