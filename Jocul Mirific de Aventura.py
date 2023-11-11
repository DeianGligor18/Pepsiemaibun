import time

def introduction():
    print("Bine ai venit la Aventura Secolului!")
    time.sleep(1)
    print("Te-ai trezit si nu stii ce s-a intamplat. In fata ta este o pestera din care se vede o lumina.")
    time.sleep(1)
    print("Vrei sa intri in pestera? da/nu ")

def choose_path():
    choice = input().lower()
    if choice == "da":
        print("ai intrat in pestera.. sa vedem ce este acolo..")
        time.sleep(1)
        cave_path()
    elif choice == "nu":
        print("Nu prea vrei sa te incumeti si iti place viata totusi..")
        time.sleep(1)
        print("Game over.. Teoretic traiesti.. deci mna..")
    else:
        print("Alege da sau nu..")
        choose_path()

def cave_path():
    print("Ai mers vreo 68 de metri in pestera si vezi ca se fac doua drumuri.")
    time.sleep(1)
    print("Drumul continua in stanga sau in dreapta")
    time.sleep(1)
    print("Pe unde o iei cumetre? stanga/dreapta ")

    choice = input().lower()
    if choice == "stanga":
        print("Ai ales calea mirifica din stanga..")
        time.sleep(1)
        treasure_room()
    elif choice == "dreapta":
        print("ai ales calea dubioasa din dreapta.")
        time.sleep(1)
        maghiar_room()
    else:
        print("Nu ai cum sa o iei inapoi sau in sus sau in jos...")
        cave_path()

def treasure_room():
    print("Ai intrat intr-o camera plina de comori nemaivazute si plina de aur/argint (depinde de tine acuma..)")
    time.sleep(1)
    print("Bravo totusi, ai gasit comoara cea mare, poti sa ti iei shaorama aia de la Dristor.")
    time.sleep(1)
    print("Multumesc ca ai jucat jocul Mirific de aventura")

def maghiar_room():
    print("Ai mai mers vreo 43 de metri si 21 de centimetri si ai dat de un Maghiar.")
    time.sleep(1)
    print("Ce vrei sa faci? bataie/fuga")

    choice = input().lower()
    if choice == "bataie":
        print("Ai ales sa arati ca ai bicepsu' mare...")
        time.sleep(1)
        print("Din pacate, Maghiarul avea Kurtos Kolacs la el.. ")
        time.sleep(1)
        print("Game over. Iti era foame..")
    elif choice == "fuga":
        print("Ai ales sa fugi de Maghiar cand ai vazut ca a scos din sacosa Kurtos Kolacs..")
        time.sleep(1)
        print("Ai reust sa scapi dand cu fuga in Maghiar.. Ai ajuns inapoi de unde ai venit..")
        time.sleep(1)
        print("Game Over. Iti multumesc pentru joaca!!")
    else:
        print("Alege bataie sau fuga.")
        maghiar_room()

introduction()
choose_path()
