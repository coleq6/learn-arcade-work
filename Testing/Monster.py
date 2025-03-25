class Monster():
    def __init__(self):
        self.name = ""
        self.health = 100
    def decrease_health(self, damage):
        self.health -= damage
        if self.health < 1:
            print("gorp is dead")
        elif self.health > 0:
            print(self.name + " is now at " + str(self.health) + " health")
def main():
    gorp = Monster()
    gorp.name = "gorp"
    gorp.decrease_health(100)

main()


