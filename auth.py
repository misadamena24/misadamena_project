import os, json
from pathlib import Path

data = "data"
file = Path(data)/"users.json"

def check_folder():
    if not os.path.exists(data):
        os.mkdir(data)

def ruaj_user(users):
    file.write_text(json.dumps(users, indent=4))

def sign_up():
    users = {}
    if file.exists():
        users = json.loads(file.read_text())
    while True:
        username = input("Username: ").strip()
        if username in users:
            print("Ky username ekziston, provo nje tjeter. ")
        else:
            break
    password = input("Password: ").strip()
    users[username] = {"password" : password}
    check_folder()
    ruaj_user(users)
    print("Rregjistrimi u krye me sukses! ")
    return username

def log_in():
    if not file.exists():
        print("Ky perdorues nuk ekziston! ")
        return None
    users = json.loads(file.read_text())

    username = input("Username: ").strip()
    if username not in users:
        print("Nuk ekziston ky username.")
        return None
    max = 3
    i = 0
    while i < max:
        password = input("Password: ").strip()
        if users[username]["password"] == password:
            print(f"Mirseerdhe, {username}!")
            return username
        else: 
            i += 1
            print("Provo perseri!")
    print("Error provo perseri me vone.")
    return None