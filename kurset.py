from student_data import te_dhenat_e_studenteve, ruaj_te_dhenat
import requests
from rekomandime import perditeso_rekomandimin


def shto_kurs(username, emri_kursit, profesori, kredite):
    data = te_dhenat_e_studenteve(username) #load
    
    if emri_kursit in data["Kurset"]:
        print("Ky kurs eshte shtuar me pare! ")
        return
    data["Kurset"][emri_kursit] = {
        "Profesori" : profesori,
        "Kreditet" : kredite,
        "Notat" : []
    }
    ruaj_te_dhenat(username, data) #save
    print(f"Kursi '{emri_kursit}' u shtua me sukses per studentin '{username}'")

def listo_kurset(username):
    data = te_dhenat_e_studenteve(username)
    kurset = data.get("Kurset", {})
    if not kurset:
        print("Nuk ka kurse te rregjistruara! ")
        return
    print("Kurset e rregjistruara per studentin jane: ")
    for kurs, info in kurset.items():
        print(f"{kurs} \nProfesori: {info['Profesori']}\nKredit: {info['Kreditet']}\nNota:{info['Notat'] if info['Notat'] else 'Nuk ka akoma asnje note'}")

def shto_nota(username, emri_kursit, nota):
    data = te_dhenat_e_studenteve(username)
    kursi = data['Kurset'].get(emri_kursit)

    if not kursi:
        print("Kursi nuk u gjet!")
        return
    kursi["Notat"].append(nota)
    ruaj_te_dhenat(username, data)
    print("Nota u shtua me sukses! ")
    perditeso_rekomandimin(username)

def shiko_notat(username, emri_kursit):
    data = te_dhenat_e_studenteve(username)
    kursi = data["Kurset"].get(emri_kursit)
    if not kursi:
        print("Kursi nuk ekziston1")
        return
    Notat = kursi["Notat"]
    if not Notat:
        print("Nuk ka ende nota! ")
    else:
        print(f"Notat per '{emri_kursit}': {Notat}")

def update_notat(username, emri_kursit, index, nota_Re):
    data = te_dhenat_e_studenteve(username)
    kursi = data["Kurset"].get(emri_kursit)

    if not kursi:
        print("Ky kurs nuk ekziston")
        return
    if index < 0 or index >= len(kursi["Notat"]):
        print("Error, ky indeks nuk eshte i vlefshem")
        return
    nota_vjeter = kursi["Notat"][index]
    kursi["Notat"][index] = nota_Re
    ruaj_te_dhenat(username, data)
    print("Nota u ndryshua me sukses")
    perditeso_rekomandimin(username)
def shfaq_rekomandimin(username):
    data = te_dhenat_e_studenteve(username)
    rekomandimi = data.get("Rekomandimet", {})
    titulli = rekomandimi.get("Titulli", "Nuk ka rekomandime aktuale")
    url = rekomandimi.get("Url", "")
    print(f"Rekomandimi i librit: {titulli}\nLink: {url}")