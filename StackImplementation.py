#Javascript code screener

import stack 

class Linter:
    def __init__(self):
        self.stack = stack.Stack()
    def lint(self, text):
        while self.stack.read():
            self.stack.pop()

        matching_braces = {"(":")", "[": "]", "{":"}"} #å dict

        for char in text:
            if char in matching_braces.keys():
                self.stack.push(char)
            elif char in matching_braces.values():
                if not self.stack.read():
                    return char + "does not have opening brace"
                else: 
                    popped_opening_brace = self.stack.pop()

                    if char != matching_braces.get(popped_opening_brace):
                        return char + "has mismathed opening brace"
                    
        if self.stack.read():
            return self.stack.read() + "does not have closing brace"
        
        return True #given no errors