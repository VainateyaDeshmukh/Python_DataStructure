class Emp:
    def __init__(self):
        self.name = "akash"
        self.id = 36
    def display(self):
        print("from parent Class")

class Mgr1(Emp):
    def __init__(self):
        super().__init__()
        self.exp = 20

mgr1 = Mgr1()
mgr1.display()
print(mgr1.exp)
print(mgr1.id)