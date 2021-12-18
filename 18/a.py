class SnailfishNumber:
    def __init__(self, value, parent):
        self.parent = parent
        if isinstance(value, list):
            self.left = SnailfishNumber(value[0], self)
            self.right = SnailfishNumber(value[1], self)
            self.value = None
        elif isinstance(value, SnailfishNumber):
            self.value = value.value
            if self.value is None:
                self.left = SnailfishNumber(value.left, self)
                self.right = SnailfishNumber(value.right, self)
            else:
                self.left = self.right = None
        else:
            self.value = value
            self.left = None
            self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return str([self.left, self.right])

    def magnitude(self):
        if self.value is not None:
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def add(self, other):
        if self.value is not None:
            self.left = self.value
        else:
            self.left = SnailfishNumber([self.left, self.right], self)
        self.right = other
        other.parent = self
        self.value = None
        while self.reduce(): continue

    def reduce(self):
        if self.explosion_check(0)[0]:
            return True
        if self.split_check():
            return True
        return False

    def explosion_check(self, parent_levels): # returns (bool, bool) meaning (explosion triggered, explosion carried out)
        if self.value is not None:
            return (False, False)
        if self.left.value is not None and self.right.value is not None and parent_levels >= 4:
            return (True, False)
        else:
            left_check = self.left.explosion_check(parent_levels + 1)
            if left_check[1]:
                return left_check
            if left_check[0]:
                exploding_pair = self.left
                self.left = SnailfishNumber(0, self)
                self.right.add_to_leftmost(exploding_pair.right.value)
                #go up and left until we can't anymore
                parent = self.parent
                node = self
                while parent is not None and parent.left is node:
                    node = parent
                    parent = parent.parent
                if parent is not None:
                    parent.left.add_to_rightmost(exploding_pair.left.value)
                return (True, True)

            right_check = self.right.explosion_check(parent_levels + 1)
            if right_check[1]:
                return right_check
            if right_check[0]:
                exploding_pair = self.right
                self.right = SnailfishNumber(0, self)
                self.left.add_to_rightmost(exploding_pair.left.value)
                #go up and right until we can't anymore
                parent = self.parent
                node = self
                while parent is not None and parent.right is node:
                    node = parent
                    parent = parent.parent
                if parent is not None:
                    parent.right.add_to_leftmost(exploding_pair.right.value)
                return (True, True)
        return (False, False)


    def split_check(self):
        if self.value is not None and self.value >= 10:
            self.left = SnailfishNumber(self.value // 2, self)
            self.right = SnailfishNumber(self.value // 2 + (self.value % 2), self)
            self.value = None
            return True
        elif self.left is not None and self.right is not None:
            if self.left.split_check():
                return True
            return self.right.split_check()
        else:
            return False

    def add_to_rightmost(self, num):
        if self.value is not None:
            self.value += num
        elif self.right is not None:
            self.right.add_to_rightmost(num)


    def add_to_leftmost(self, num):
        if self.value is not None:
            self.value += num
        elif self.left is not None:
            self.left.add_to_leftmost(num)

with open("input.txt") as inp:
    import ast
    numbers = [SnailfishNumber(ast.literal_eval(line), None) for line in inp]

top_num = numbers[0]
for num in numbers[1:]:
    top_num.add(num)

print(top_num.magnitude())