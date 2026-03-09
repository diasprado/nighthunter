import requests
import shutil
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from tqdm import tqdm
import json

init(autoreset=True)

os.system("clear")

width = shutil.get_terminal_size().columns

def center(text):
    return text.center(width)

banner = f"""{Fore.RED}
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝
██╔██╗ ██║██║██║  ███╗███████║   ██║
██║╚██╗██║██║██║   ██║██╔══██║   ██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝
"""

print(center(banner))

print(center(Fore.CYAN + "NIGHTHUNTER v3"))
print(center("Advanced OSINT Recon Framework"))
print(center("─" * 32))
print()

print(center(Fore.GREEN + "Digite o username alvo"))
username = input(Fore.CYAN + "➤ ").strip()

print()

# carregar sites
try:
    with open("sites.txt") as f:
        sites = [line.strip() for line in f if line.strip()]
except:
    print(Fore.RED + center("Erro: sites.txt não encontrado"))
    exit()

threads = 20

print(center(f"Target        : {username}"))
print(center(f"Sites loaded  : {len(sites)}"))
print(center(f"Threads       : {threads}"))
print()
print(center(Fore.MAGENTA + "Scanning..."))
print()

found = []

def check(site):
    url = site.format(username)
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            found.append(url)
    except:
        pass

with ThreadPoolExecutor(max_workers=threads) as executor:
    list(tqdm(executor.map(check, sites), total=len(sites)))

print()
print(center(Fore.YELLOW + "Scan finalizado"))
print()

if found:
    print(center(Fore.GREEN + "User encontrado em:"))
    for f in found:
        print(center(f))
else:
    print(center(Fore.RED + "Nenhum resultado encontrado"))

# salvar relatório
report = {
    "username": username,
    "found": found
}

with open("resultado.json", "w") as f:
    json.dump(report, f, indent=4)

print()
print(center("Relatório salvo em resultado.json"))
