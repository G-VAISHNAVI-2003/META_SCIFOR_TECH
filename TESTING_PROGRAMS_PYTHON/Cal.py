import math

class Cal:
    def adds(self,a,b):
        try:
            res = a + b
            print(f"Addition of {a} and {b}:{res}")
            return res
        except TypeError:
            print("Please give correct input values to add")
            return None
    def subs(self,a,b):
        try:
            res = a - b
            print(f"Subtraction of {a} and {b}:{res}")
            return res
        except TypeError:
            print("Please give correct input values to subtract")
            return None
    def mul(self,a,b):
        try:
            res = a * b
            print(f"Mulitiplication of {a} and {b}:{res}")
            return res
        except TypeError:
            print("Please give correct input values to multiply")
            return None
    def div(self,a,b):
        try:
            res = a / b
            print(f"Division of {a} and {b}:{res}")
            return res
        except ZeroDivisionError:
            print("Please give correct input values to divide")
            return None
    def power(self,a,b):
        try:
            res = math.pow(a,b)
            print(f"Raising {a} to the power of {b}:{res}")
            return res
        except TypeError:
            print("Please give valid inputs to calculate")
            return None
        
if __name__ == "__main__":
    c = Cal()

    print(c.adds(1,3))
    print(c.subs(9,4))
    print(c.mul(2,4))
    print(c.div(19,8))
    print(c.power(2,3))