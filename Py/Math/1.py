# done by RIYOMA
# done by RIYOMA

def main():
    print("Entre a:")
    a = float(input())

    print("Entre b:")
    b = float(input())

    print("Entre f(a):")
    A = float(input())

    print("Entre f(b):")
    B = float(input())

    alt = int(input("\nEntrer l'altitude souhaitée: "))

    if alt <= 0:
        print("\nL'altitude doit être un entier positif.")
        return

    if A * B >= 0:
        print("A * B > 0, aucune solution dans l'intervalle.")
        return

    for i in range(alt):
        c = (a + b) / 2
        print(f"\nLe centre c est : {c}")
        C = float(input("Donner l'image de c f(c): "))

        if A * C < 0:
            b = c
        elif B * C < 0:
            a = c
        else:
            print(f"La solution est {C}")
            return

        print(f"\nL'intervalle est : [{a}, {b}]")

    print("\nCalcul terminé.")

if __name__ == "__main__":
    main()
# done by RIYOMA
# done by RIYOMA