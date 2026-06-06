#Javascript code screener

import stack 

class Linter:
    def __init__(self):
        self.stack = stack.Stack()
    def lint(self, text):
        while self.stack.read():
            self.stack.pop()

        matching_braces = {"(":")", "[": "]", "{":"}"} #å dict
        