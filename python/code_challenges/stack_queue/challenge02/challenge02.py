# Write here the code challenge solution

class Paranthesese:
    ''' This class contain 2 method which is responsible to implement stack as list '''
    def __init__(self):
        self.stack = []
        self.dictu = {'{': '}', '[': ']', '(': ')'}
        
    def isValid(self, s: str):
        ''' this method determone if the given expression inside paranthesese is valid or not '''
        if len(s) == 1:
            return False
        for i in s:
            if i in self.dictu.keys():
                self.stack.append(i)
            if i in self.dictu.values():
                if not self.stack:
                    return False
                elif i != self.dictu[self.stack.pop()]:
                    return False
        return self.stack == []
 

if __name__ == "__main__":
    p1 = Paranthesese()
    p2 = Paranthesese()
    p3 = Paranthesese()
    p4 = Paranthesese()
    p5 = Paranthesese()
    p6 = Paranthesese()
    print(p1.isValid("()"))
    print(p2.isValid("()[]{}"))
    print(p3.isValid("[({}]"))
    print(p4.isValid("[(hello)()]"))
    print(p5.isValid("[{(())}]"))
    