import requests
import time
import json
from rich.progress import track
from colorama import Fore, Style

print("""
███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗
████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝
██╔██╗ ██║██║██║  ███╗███████║   ██║
██║╚██╗██║██║██║   ██║██╔══██║   ██║
██║ ╚████║██║╚██████╔╝██║  ██║   ██║
╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝

NIGHTHUNTER v3
Advanced OSINT Recon Framework
Feito Por Dias
Use com Cuidado e Responsabilidade
""")

username = input("Digite o username alvo ➤ ")

# carregar sites
with open("sites.txt", "r") as f:
    lista_sites = list(set(f.read().splitlines()))

print(f"\nTarget : {username}")
print(f"Sites  : {len(lista_sites)}")
print("\nScanning...\n")

encontrados = []
inicio = time.time()

headers = {
    "User-Agent": "Mozilla/5.0"
}

for site in track(lista_sites, description="Escaneando..."):
    url = site.format(username)

    try:
        r = requests.get(url, headers=headers, timeout=5)

        if r.status_code == 200:
            encontrados.append(url)

    except:
        pass

fim = time.time()

print("\nScan finalizado\n")

if encontrados:
    print(Fore.GREEN + "User encontrado em:\n" + Style.RESET_ALL)
    for u in encontrados:
        print(u)
else:
    print(Fore.RED + "Nenhum perfil encontrado" + Style.RESET_ALL)

# salvar resultado
resultado = {
    "username": username,
    "perfis": encontrados
}

with open("resultado.json", "w") as f:
    json.dump(resultado, f, indent=4)

print("\nRelatório salvo em resultado.json")

# estatísticas
print("\n--- Estatísticas ---")
print(f"Sites verificados: {len(lista_sites)}")
print(f"Perfis encontrados: {len(encontrados)}")
print(f"Tempo total: {round(fim - inicio, 2)} segundos")
