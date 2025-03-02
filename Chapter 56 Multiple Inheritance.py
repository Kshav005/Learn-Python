# We can inherit more than one parent classes in the child class

class Human : 
    def __init__(self, name) :
        self.name = name 
    def show(self) : 
        print(f"Human class is running!")

class Inhuman : 
    def __init__(self, type1) :
        self.type1 = type1
    def info(self) : 
        print(f"The Inhuman class is running")

class Hero(Inhuman, Human) : 
    def __init__(self, type1):
        self.type1 = type1
        
    def __call__(self) :
        return super().info()
    
a = Hero("Villain")   
a()
a.show()

