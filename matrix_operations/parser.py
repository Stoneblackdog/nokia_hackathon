class Node:
    def __init__(self, value: str, left, right=None):
        self.value = value
        self.left = left
        self.right = right


class Parser:
    def __init__(self, operation):
        self.operation = operation
        self.current = 0

    def parse_expression(self):
        return self.parse_term()

    def parse_term(self):
        expr = self.parse_factor()
        while not self.is_at_end() and self.operation[self.current] == '+':
            self.current += 1
            right = self.parse_factor()

            expr = Node('+', expr, right)

        return expr

    def parse_factor(self):
        expr = self.parse_primary()
        while not self.is_at_end() and self.operation[self.current] == '*':
            self.current += 1
            right = self.parse_primary()

            expr = Node('*', expr, right)

        return expr

    def parse_primary(self):
        value = self.operation[self.current]
        self.current += 1

        return Node(value, None, None)

    def is_at_end(self):
        return self.current >= len(self.operation)


# grammar
#
# expression -> term
# term -> factor ( '+' factor )*
# factor -> primary ( '*' primary )*
# primary -> MATRIX
