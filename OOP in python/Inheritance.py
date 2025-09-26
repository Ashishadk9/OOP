class X:
    def whoami(self):
        print("X")

class Y(X):
    def whoami(self):
        print("Y")
        super().whoami()

class Z(X):
    def whoami(self):
        print("Z")
        super().whoami()

class A(Y, Z):
    def whoami(self):
        print("A")
        super().whoami()
a=A()
a.whoami()