# To-Do Flask aplikacija

Jednostavna web aplikacija za upravljanje zadacima izrađena u Pythonu korištenjem Flask web okvira.  
Projekt je izrađen u edukativne svrhe kao primjer objektno orijentiranog programiranja.

Aplikacija je dostupna javno na:
https://demo.krizak.net

## Funkcionalnosti
- dodavanje zadataka
- uređivanje zadataka
- brisanje zadataka
- označavanje zadataka kao završenih
- vraćanje zadataka u stanje nezavršenosti
- postavljanje prioriteta zadatka

## Korištene tehnologije
- Python 3
- Flask
- Bootstrap
- Git
- Cloudflare Tunnel

## Arhitektura i hosting

Aplikacija je **self-hostana** u sljedećem okruženju:

- Proxmox virtualizacija
- Debian Linux virtualna mašina
- vlastita domena (`demo.krizak.net`)
- Cloudflare Tunnel za siguran pristup bez izravnog izlaganja VM-a internetu

Python aplikacija i Cloudflare Tunnel konfigurirani su kao **systemd servisi**,  
što znači da se automatski pokreću nakon restarta virtualne mašine bez potrebe za ručnom intervencijom.

## Instalacija i lokalno pokretanje

Potrebno je imati instaliran Python 3 i Git.

```bash
git clone https://github.com/David-Krizak/todo.git
cd todo
chmod +x setup.sh
./setup.sh
source venv/bin/activate
python app.py
