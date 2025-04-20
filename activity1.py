class Superhero:
    def __init__(self, name, superpower, weakness, team):
        self.name = name
        self.superpower = superpower
        self.weakness = weakness
        self.team = team

    def introduce(self):
        return f"I am {self.name}! My superpower is {self.superpower}."

# Subclass: Flyer (inherits from Superhero)
class Flyer(Superhero):
    def __init__(self, name, superpower, weakness, team, flight_speed):
        super().__init__(name, superpower, weakness, team)
        self.flight_speed = flight_speed

    def introduce(self):
        return f"I am {self.name}, and I can fly at {self.flight_speed} km/h!"

# Subclass: Speedster (inherits from Superhero)
class Speedster(Superhero):
    def __init__(self, name, superpower, weakness, team, run_speed):
        super().__init__(name, superpower, weakness, team)
        self.run_speed = run_speed

    def introduce(self):
        return f"I am {self.name}, the fastest on the ground with a speed of {self.run_speed} km/h!"

# Subclass: SuperheroWoman (inherits from Superhero)
class SuperheroWoman(Superhero):
    def __init__(self, name, superpower, weakness, team, emblem):
        super().__init__(name, superpower, weakness, team)
        self.emblem = emblem

    def introduce(self):
        return f"I am {self.name}, a fearless superhero! My emblem symbolizes {self.emblem}."

# Example usage
hero1 = Flyer("Skyhawk", "Flight", "Thunderstorms", "Avian Allies", 300)
hero2 = Speedster("FlashDash", "Super Speed", "Rough Terrain", "Ground Force", 400)
hero3 = SuperheroWoman("Aurora", "Healing", "Overexertion", "Light Guardians", "Hope")
hero4 = SuperheroWoman("ShadowDancer", "Stealth", "Bright Light", "Night Watch", "Resilience")

print(hero1.introduce())
print(hero2.introduce())
print(hero3.introduce())
print(hero4.introduce())
