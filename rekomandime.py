import requests
from student_data import te_dhenat_e_studenteve, ruaj_te_dhenat

def kursi_me_ulet(username):
    data = te_dhenat_e_studenteve(username)
    kurset = data.get("Kurset", {})
    notat = []
    for kurs, info in kurset.items():
        for nota in info.get("Notat", []):
            notat.append((nota, kurs))
    if not nota:
         return None, None
    min_nota = notat[0]
    for note in notat[1:]:
        if note[0]<min_nota[0]:
            min_nota = note
    return min_nota
def merr_rekomandim(kurs):
    url = f"https://gutendex.com/books?topic={kurs.lower()}"
    response = requests.get(url)
    data =response.json()
    results = data.get("results", [])
    if not results:
        return "Nuk u gjet liber me kete teme.", ""
    
    libri = results[0]
    titulli = libri.get("title", "")
    url_libri= libri.get("formats", {}).get("text/html", "")
    return titulli, url_libri

def perditeso_rekomandimin(username):
    nota, kurs = kursi_me_ulet(username)

    titulli, url_libri = merr_rekomandim(kurs)
    data = te_dhenat_e_studenteve(username)
    data["Rekomandimet"] = {"Titulli": titulli, "Url": url_libri}
    ruaj_te_dhenat(username, data)
