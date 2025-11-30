import requests
import subprocess
import os
import sys
import tempfile
import argparse

args = sys.argv[1:]
url = "https://raw.githubusercontent.com/Raphi9999/Test/refs/heads/main/githubtest.py"

# Temporäre Datei erzeugen – wird nicht im Projekt gespeichert
with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
    tmp.write(requests.get(url).content)
    tmp_path = tmp.name

# Ausführen
subprocess.run(["python", "githubtest.py", *args])

# Temp-Datei löschen
os.remove(tmp_path)
