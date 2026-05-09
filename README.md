[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Domena: Digitalna baza podataka o filmovima i kinematografiji.

Svrha: Aplikacija služi kao centralni sistem za evidenciju filmova. Omogućava korisnicima da pretražuju filmske naslove, prate njihove ocjene na platformama poput IMDB-a, bilježe godine izdanja i prate uspjehe na prestižnim nagradama (Oskari). Cilj je pružiti brz i efikasan način za upravljanje podacima o filmovima kroz REST API operacije.
## Tim 12


- **Student A**: Fatima Salić - resurs: `/directors`
- **Student B**: Elma Đonlić - resurs: `/movies`


## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/directors`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/directors` | Lista svih režisera (filter po nationality) |
| GET | `/directors/{id}` | Dohvatanje režisera po ID-u |
| POST | `/directors` | Kreiranje novog režisera |
| PUT | `/directors/{id}` | Potpuna zamjena režisera |
| PATCH | `/directors/{id}` | Djelimično ažuriranje režisera |
| DELETE | `/directors/{id}` | Brisanje režisera |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/directors" \
  -H "Content-Type: application/json" \
  -d '{"name": "Christopher Nolan", "nationality": "British", "birth_year": 1970, "awards": 5, "active": true, "rating": 9.0}'
```

### Resurs B: `/movies`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/movies` | Vraća listu svih filmova. Podržava filtriranje po godini |
| GET | `/movies/{id}` |Vraća detaljne informacije o  filmu na osnovu njegovog ID-a |
| POST | `/resursi_a` | Kreira novi zapis o filmu |
| PUT | `/movies/{id}` | Potpuna zamjena postojeceg filma |
| PATCH | `/movies/{id}` | Djelimično ažuriranje filma |
| DELETE | `/movies/{id}` | Brisanje filma |

curl -X POST "http://localhost:8000/movies" \
  -H "Content-Type: application/json" \
  -d '{"title": "Inception", "year": 2010, "rating": 9, "is_oscar_winner": true, "description": "Film o snovima unutar snova."}'

[Analogno kao za Resurs A]

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** [GPT-4, Copilot model, ...]

**Primjer 1:**
- **Prompt:** Imam SQLModel klasu Director sa poljima id, name i nationality. Dodaj još polja da ih ukupno bude minimum 6 različitih tipova (str, int, float, bool, Optional). Polja trebaju biti logički smislena za reditelja filmova. Ažuriraj i DirectorCreate i DirectorUpdate sheme sa istim poljima.
- **Kako je pomoglo:** Claude je generisao dodatna polja (birth_year, awards, rating, active) sa odgovarajućim tipovima i automatski ažurirao sve tri klase (Director, DirectorCreate, DirectorUpdate).
- **Prilagodbe:** Nisu bile potrebne značajne prilagodbe, kod je bio direktno upotrebljiv.

**Primjer 2:**
- **Prompt:** [Npr. "Implementiraj PATCH endpoint sa exclude_unset=True"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Opis]

## Napomene

[Dodatne napomene specifične za vašu implementaciju]