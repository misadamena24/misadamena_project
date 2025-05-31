from auth import sign_up, log_in
from kurset import shto_kurs, listo_kurset, shto_nota,shiko_notat, update_notat, shfaq_rekomandimin
from statistika import statistika
from backup import back_up_file
print("Miresevini ne Student tracker!")
while True:
    zgjedhja = input("Login/SignUp: ").strip().lower()
    if zgjedhja == "login":
        username = log_in()
        if username:
             break
    elif zgjedhja == "signup":
        username = sign_up()
        if username:
            break
    else:
        print("LogIn/SignUp")

while True:
    print("\nZgjidhni nje opsion:")
    print("1. Shto kurs")
    print("2. Listo kurset")
    print("3. Shto note")
    print("4. Shiko notat")
    print("5. Ndrysho note")
    print("6. Shfaq rekomandime")
    print("7. Shiko statistika")
    print("8. Dil")
    opsion = input("Zgjidh opsionin: ").strip()

    if opsion == "1":
        emri = input("Emri i kursit: ")
        profesori = input("Emri i profesorit: ")
        kredite = int(input("Kreditet: "))
        shto_kurs(username, emri, profesori, kredite)
    elif opsion == "2":
        listo_kurset(username)
    elif opsion == "3":
        emri = input("Emri i kursit: ")
        nota = float(input("Nota: "))
        shto_nota(username, emri, nota)
    elif opsion == "4":
        emri = input("Emri i kursit: ")
        shiko_notat(username, emri)
    elif opsion == "5":
        emri = input("Emri i kursit: ")
        index = int(input("Indeksi i notes (fillon nga 0): "))
        nota_re = float(input("Nota e re: "))
        update_notat(username, emri, index, nota_re)
    elif opsion == "6":
        shfaq_rekomandimin(username)
    elif opsion == "7":
        statistika(username)
    elif opsion == "8":
        print("Duke u dale nga programi. Mirupafshim!")
        break
    else:
        print("Provo perseri.")

back_up_file()