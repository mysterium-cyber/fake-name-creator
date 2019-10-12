import random

#countries

def german():
    de_nach = ["Mueller", "Schmidt", "Lange", "Meyer", "Schröder", "Ahlers", "Schäfer", "Hartmann", "Groß", "Klein", "Seifert", "Riedel", "Eckert", "Weber", "Krause", "Schmitz"]
    de_vor = ["Patrizia ", "Marie ", "Paul ", "Sophie ", "Alexander ", "Maria ", "Maximilian ", "Sofia ", "Elias ", "Emilia ", "Ben ", "Emma ", "Louis ", "Hanna ", "Leon ", "Mia ", "Noah ", "Anna ", "Henry ", "Johanna ", "Felix ", "Katharina ", "David ", "Lena ", "Tim ", "Lea ", "Alexander ", "Laura ", "Jan ", "Lisa ", "Dominik ", "Vanessa ", "Phillip ", "Sara ", "Florian ", "Maria ", "Christian ", "Sabrina ", "Patrick ", "Julia ", "Matthias ", "Nadine ", "Markus ", "Nicole ", "Moritz ", "Greta ", "Paul ", "Charlotte ", "Felix "]

    vorname = random.choice(de_vor)
    nachname = random.choice(de_nach)

    return(vorname + nachname)

#agreement

print("The creator accepts no liability for crimes committed with the help of this program.")
print("This program is intended for jurnalists / reporters who want to protect their sources with fake names")
print("Do you accept that you will not use the fake names for illegal activities? (y/n)")

accept = input("")
if accept == "y":

#select country
    print("fake name creator")
    print("")
    print("1. Germany")
    print("")

    choice = input("Enter the number of the country where your fake name should come from:")

    if choice == str(1):
       print("")
       print("Your German fake name is:")
       print(german())
