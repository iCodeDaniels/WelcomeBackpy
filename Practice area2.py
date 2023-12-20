class Person:
    def __init__(self, a, b):
        self.a = a
        self.b = b

point = Person("Daniel", "Ifeoluwa")
point.a = "Akinloye"
print(point.b, point.a)
