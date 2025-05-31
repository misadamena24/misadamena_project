from student_data import te_dhenat_e_studenteve

def statistika(username):
    data = te_dhenat_e_studenteve(username)
    kurset = data.get("Kurset", {})
    
    if not kurset:
        print("Nuk keni ende asnje kurs!")
        return

    notat = []
    for kurs, info in kurset.items():
        for nota in info.get("Notat", []):
            notat.append((nota, kurs))  

    if not notat:
        print("Nuk ka nota te regjistruara!")
        return

   
    nota_me_e_ulte = notat[0]
    nota_me_e_larte = notat[0]
    totali = nota_me_e_ulte[0]

    for nota_kursi in notat[1:]:
        if nota_kursi[0] < nota_me_e_ulte[0]:
            nota_me_e_ulte = nota_kursi
        if nota_kursi[0] > nota_me_e_larte[0]:
            nota_me_e_larte = nota_kursi
        totali += nota_kursi[0]

    mesatarja = totali / len(notat)

    print(f"Nota me e ulet: {nota_me_e_ulte[0]} ne kursin '{nota_me_e_ulte[1]}'")
    print(f"Nota me e lart: {nota_me_e_larte[0]} ne kursin '{nota_me_e_larte[1]}'")
    print(f"Nota mesatare për te gjitha kurset esht: {mesatarja:.2f}")
