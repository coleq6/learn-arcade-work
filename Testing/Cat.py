class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print(self.name + " says \"meow\"")

def main():
    my_cat = Cat()
    my_cat.name = "Jimbo"
    my_cat.color = "Brown"
    my_cat.weight = 4
    my_cat.meow()

main()
