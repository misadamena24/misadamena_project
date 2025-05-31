import os, json
from pathlib import Path

def get_folderin(username):
    folder = Path("data")
    if not folder.exists():
        folder.mkdir()
    path = folder / f"{username}.json"
    return path

def te_dhenat_e_studenteve(username): 
    
    path = get_folderin(username)
    if not path.exists():
        print(f"Nuk ka te dhena per {username}! ")
        data = {
            "Kurset": {},
            "Rekomandimet" : {"Titulli": "", "Url" :""}
        }
        return data
    permbajtja = path.read_text().strip()
    if len(permbajtja) == 0:
        print("File eshte bosh") 
        data = {
            "Kurset": {},
            "Rekomandimet" : {"Titulli": "", "Url" :""}
        }
        return data
    data = json.loads(permbajtja)
    return data

def ruaj_te_dhenat(username, data): 
    path = get_folderin(username)
    permbajtja = json.dumps(data, indent=4)
    path.write_text(permbajtja)
