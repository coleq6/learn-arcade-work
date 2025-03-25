class Star():
    def __init__(self):
        self.name = ""
    def is_born(self):
        print("\"A star is born!\"")

def main():
    star = Star()
    star.name = star
    star.is_born()

main()