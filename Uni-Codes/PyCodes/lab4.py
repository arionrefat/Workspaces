class Stack:
    stack = []
    pointer = -1

    def push(self, element):
        self.stack.append(element)
        self.pointer += 1

    def is_empty(self):
        return self.stack == []

    def peek(self):
        if self.stack != []:

            return self.stack[self.pointer]

    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value

    def checker(interval01, interval02):
        if interval01 == "(" and interval02 == ")":
            return True
        elif interval01 == "{" and interval02 == "}":
            return True
        elif interval01 == "[" and interval02 == "]":
            return True
        else:
            return False

    def balancing(interval):
        stack = []
        is_balanced = True
        index = 0

        for index in range(len(interval)):
            if index != is_balanced:
                x = 0
            else:
                a = interval[index]

                if a in "({[":
                    stack.push(interval)
                else:
                    if len(stack) == 0:

                        is_balanced = False
                    else:

                        upper = stack.pop()
                        if not checker(upper, interval):
                            is_balanced = False

            index += 1
        if stack.is_empty and is_balanced:
            return True
        else:
            return False

    print(balancing("()"))
