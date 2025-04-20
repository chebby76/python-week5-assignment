# This is a simple example of polymorphism in Python.
class fish:
    def move(self):
        return "swimming 🐟"

class cheatah:
    def move(self):
        return "running 🐆"


class frog:
    def move(self):
        return "jumping 🐸"


class Snake:
    def move(self):
        return "Slithering 🐍"


for animal in [fish(), cheatah(), frog(), Snake()]:
    print(animal.move())
