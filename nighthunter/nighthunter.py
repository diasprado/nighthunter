import requests
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import json
import os
import shutil

init(autoreset=True)

os.system("clear")

banner = f"""{Fore.RED}
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝██║  ██║██║   ██║████╗  ██║╚══██╔══╝
██╔██╗ ██║██║██║  ███╗███████║   ██║   ███████║██║   ██║██╔██╗ ██║   ██║
██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██╔══██║██║   ██║██║╚██╗██║   ██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║   ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝

{Fore.YELLOW}══════════════════════════════════════════════
            NIGHTHUNTER v3
        Advanced OSINT Recon Tool
══════════════════════════════════════════════
"""

largura = shutil.get_terminal_size().columns

if largura < 90:
    print(Fore.RED + "NIGHTHUNTER v3\n")
else:
    print(banner)

print(Fore.WHITE + "Ferramenta de busca de usernames em sites públicos\n")

username = input(Fore.CYAN + "Digite o username alvo ➤ ")

print(Fore.YELLOW + "\n[+] Preparando varredura...\n")

# variações simples
usernames = [
    username,
    username.lower(),
    username.replace(".", ""),
    username.replace("_", "")
]

# carregar sites
with open("sites.txt") as f:
    sites = [line.strip() for line in f]

headers = {
"User-Agent":"Mozilla/5.0"
}

results = []

def check(url):

    for user in usernames:

        link = url.format(user)

        try:

            r = requests.get(link, headers=headers, timeout=5)

            if r.status_code == 200:

                print(Fore.GREEN + f"[ENCONTRADO] {link}")

                results.append({
                    "username": user,
                    "url": link
                })

                return

        except:
            pass

print(Fore.MAGENTA + "[+] Iniciando scan OSINT...\n")

with ThreadPoolExecutor(max_workers=30) as executor:
    list(tqdm(executor.map(check, sites), total=len(sites)))

print(Fore.YELLOW + "\n[+] Salvando relatório...\n")

with open("resultado.json","w") as f:
    json.dump(results, f, indent=4)

print(Fore.CYAN + "✔ Scan finalizado")
print(Fore.CYAN + "✔ Relatório salvo em resultado.json\n")
