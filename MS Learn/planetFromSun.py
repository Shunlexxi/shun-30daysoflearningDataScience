planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

user_planet = input("Please, enter name of Planet beginning with a capital letter only: ")

#finding thr location of the planet entered by user
planets_index = planets.index(user_planet)

show = planets[0 : planets_index]

print("Here are the Planets closer than " + user_planet)

print(show)

#farther
print("Here are the planets further than " + user_planet)

print(planets[planets_index + 1 :])
