import requests
import subprocess
import os
import tempfile
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--test", required=False)
args = ap.parse_args()
url = "https://raw.githubusercontent.com/Raphi9999/Test/refs/heads/main/githubtest.py"

# Temporäre Datei erzeugen – wird nicht im Projekt gespeichert
with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
    tmp.write(requests.get(url).content)
    tmp_path = tmp.name

# Ausführen
if args.test:
    subprocess.run(["python", tmp_path, "--test", args.test])
else:
    subprocess.run(["python", tmp_path])

# Temp-Datei löschen
os.remove(tmp_path)
