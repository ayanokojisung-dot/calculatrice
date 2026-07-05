def main():
   while True:
    n= int(input("entrez le premier nombre :"))
    m= int(input("entrez le second nombre :"))
    print("==========MENU=========")
    print("1.Addition")
    print("2.Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    choix= input("entrez le choix :")

    if choix == "1":
        a= n+m
        print("Le résultat est :", a)
    elif choix == "2":
        b= n-m
        print("Le resultat est :",b)
    elif choix == "3":
        c= n*m
        print("Le résultat est :", c)
    elif choix == "4":
        d= n/m
        print("Le resultat est :", d)
    elif choix == "5":
        print("Au revoir !")
        break
if __name__ == "__main__":
    main()
