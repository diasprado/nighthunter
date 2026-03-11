![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![OSINT](https://img.shields.io/badge/type-OSINT-red)

# NIGHTHUNTER v3

**Advanced OSINT Recon Framework**

NIGHTHUNTER é uma ferramenta OSINT desenvolvida em Python para buscar **usernames em centenas de sites públicos da internet** e coletar informações abertas.

O objetivo do projeto é facilitar **investigações OSINT educacionais e pesquisa de perfis públicos online**.

---

# Funcionalidades

*  Scan de usernames em múltiplos sites
*  Scanner rápido
*  Estatísticas de resultados
*  Exportação de relatório
*  Ferramenta OSINT open-source

---

# Instalação

Clone o repositório:

```
git clone https://github.com/diasprado/nighthunter.git
cd nighthunter
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

# Uso

Execute o programa:

```
python3 nighthunter.py
```

Digite o username alvo e o NIGHTHUNTER irá procurar perfis públicos em diversos sites.

---

# Exemplo

```
Digite o username alvo ➤ dias
Scanning...

User encontrado em:
https://github.com/dias
https://twitter.com/dias
https://reddit.com/user/dias
```

---

# Estrutura do projeto

```
nighthunter
│
├── nighthunter.py
├── sites.txt
├── requirements.txt
├── resultado.json
└── README.md
```

---

# Aviso

Esta ferramenta foi criada **apenas para fins educacionais e pesquisa OSINT**.

Não utilize para atividades ilegais ou violação de privacidade.

---

# Licença

Este projeto está licenciado sob a **MIT License**.
