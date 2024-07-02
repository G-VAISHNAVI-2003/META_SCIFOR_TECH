def cal(func):
    def wrapper(*args, **kwargs):
        print("CALCULATING !!")
        result = func(*args, **kwargs)
        print("NOT CALCULATING!!")
        return result
    return wrapper

class A:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def show_num(self):
        print(f"Numbers: {self.n1}, {self.n2}")

class B:
    def __init__(self, n3, n4):
        self.n3 = n3
        self.n4 = n4
    
    def disp_num(self):
        print(f"Numbers: {self.n3}, {self.n4}")

class C(A, B):
    def __init__(self, n1, n2, n3, n4):
        A.__init__(self, n1, n2)
        B.__init__(self, n3, n4)

    @cal
    def res(self, num):
        return self.n1 + self.n2 + num

    calculate = lambda self, n5: self.n3 * self.n4 + n5

X = C(1, 2, 3, 4)
X.show_num()
X.disp_num()
print("Result:", X.res(3))
print("Result of lambda function:", X.calculate(5))