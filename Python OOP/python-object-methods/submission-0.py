class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        self.hunger -= 1
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        print(f"{self.name} has been fed.")
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
print(f"Fluffy's hunger level: {my_pet.hunger}")

my_pet.feed()
print(f"Fluffy's hunger level: {my_pet.hunger}")

my_pet.feed()
print(f"Fluffy's hunger level: {my_pet.hunger}")

