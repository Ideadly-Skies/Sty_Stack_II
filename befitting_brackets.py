def befitting_brackets(string):
    # initialization
    bracket_dict = {')': '(', '}': '{', ']': '['}
    stack = []

    # O(n) iteration
    for s in string:
        if s == '(' or s == '{' or s == '[':
           stack.append(s)
        else:
            # something went wrong
            if stack == []:
                return False

            # pop match from stack 
            if bracket_dict[s] == stack[-1]:
                stack.pop()

    # check length of stack equals 0
    return len(stack) == 0

if __name__ == "__main__":
  print(befitting_brackets('(){}[](())')) # -> True