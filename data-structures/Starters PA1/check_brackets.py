# python3
import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        return self.bracket_type == '(' and c == ')'


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    result = True

    for i, next in enumerate(text):
        if next in ["(", "[", "{"]:
            opening_brackets_stack.append(Bracket(next, i))
        elif next in [")", "]", "}"]:
            if not opening_brackets_stack:
                result = i + 1
                break
            else:
                bracket = opening_brackets_stack[-1]
                result = bracket.Match(next)
                if result:
                    del opening_brackets_stack[-1]
                else:
                    result = i + 1
                    break

    if result and isinstance(result, type(
            True)) and not opening_brackets_stack:
        print("Success")
    elif result and isinstance(result, type(True)):
        print(opening_brackets_stack[-1].position + 1)
    else:
        print(result)
