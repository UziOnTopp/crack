import os
import subprocess

def lire_urls(fichier):
    with open(fichier, 'r') as f:
        urls = f.readlines()
    return [url.strip() for url in urls]

def lancer_dumper(url):
    cmd = f"py dumper.py --url {url}"
    subprocess.run(cmd, shell=True, check=True)

def ajouter_a_history(url):
    with open("history.txt", "a") as f:
        f.write(f"{url}\n")

def main():
    fichier_urls = "urls.txt"
    urls = lire_urls(fichier_urls)
    
    for url in urls:
        print(f"Traitement de l'URL: {url}")
        lancer_dumper(url)
        print(f"URL traitée avec succès: {url}")
        ajouter_a_history(url)

if __name__ == "__main__":
    main()
