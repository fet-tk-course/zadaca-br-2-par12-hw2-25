[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

[Ovdje ukratko opišite domenu vaše aplikacije i njenu svrhu]

## Tim

- **Student A**: Fatima Salić - resurs: `/directors`
- **Student B**: [Ime Prezime] - resurs: `/resursi_b`

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

### Resurs B: `/resursi_b`

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

## Opis zadataka sa odbrane zadace 

- **zadatak 1a:** u ovom dijelu dodana je provjera u modelu DirectorCreate koja osigurava da polje name u klasi ne smije biti prazno i da nije sastavljeno od razmaka
- **zadatak 1b:**  u ovom dijelu u metodi post dodana je provjera da koja vraca statusni kod 409 ako reziser sa odredenim imenom vec postoji.
- **Zadatak 2:** Dodani endpoint je @router.get("/statistics) koji vraća prosječni rejting svih rezisera u bazi.
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/directors/statistika/' \
  -H 'accept: application/json'
```

**Očekivani odgovor:**
```json
{
    "Prosjek_rejtinga": 8.77
}
```