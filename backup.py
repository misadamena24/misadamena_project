import os
from pathlib import Path
import zipfile

def back_up_file():
    folder = Path("data")
    zipFile_Path = folder/ "backup.zip"

    zipf = zipfile.ZipFile(zipFile_Path, "w")
    for file in folder.glob("*.json"):
        zipf.write(file)
    zipf.close()

    print("Backup u krijua")