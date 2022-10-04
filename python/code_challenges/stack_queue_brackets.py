from data_structures.queue import Queue

opening = ["[","{","("]
closing = ["]","}",")"]

def multi_bracket_validation(myStr):
        stack = []
        for i in myStr:
            if i in opening:
                stack.append(i)
            elif i in closing:
                pos = closing.index(i)
                if ((len(stack) > 0) and
                        (opening[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
