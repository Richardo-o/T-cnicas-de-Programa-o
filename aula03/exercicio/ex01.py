letra = input("Coloque uma letra: ")

match letra.lower():
    case 'a':
        print("Essa letra é uma vogal")
    case 'e':
        print("Essa letra é uma vogal")
    case 'i':
        print("Essa letra é uma vogal")
    case 'o':
        print("Essa letra é uma vogal")
    case 'u':
        print("Essa letra é uma vogal")
    case _:
        print("Essa é uma consoante")
