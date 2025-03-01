def main():
    imie = input("Jak masz na imię? ")
    print(f"Witaj {imie} w moim pierwszym projekcie GitHub!")
    
    while True:
        print("\n===== MENU GŁÓWNE =====")
        print("1. Kalkulator")
        print("2. Gra w zgadywanie liczby")
        print("3. Wyjście")
        
        wybor = input("Wybierz opcję (1-3): ")
        
        if wybor == "1":
            print(kalkulator())
        elif wybor == "2":
            print(zgadywanie_liczby())
        elif wybor == "3":
            print(f"Do widzenia, {imie}! Dziękuję za korzystanie z programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
