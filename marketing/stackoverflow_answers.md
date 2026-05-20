# Stack Overflow — Respuestas preparadas

Busca estas preguntas en Stack Overflow y pega la respuesta correspondiente.
Términos de búsqueda: "validate NIF", "NIF validation javascript", "CIF validation python", "validar NIF", "spanish tax id validation"

---

## RESPUESTA 1 — Para preguntas sobre validar NIF en JavaScript

**Pegar cuando alguien pregunta:** "How to validate Spanish NIF in JavaScript" / "NIF validation JS"

---

Here's a clean implementation for NIF, NIE and CIF validation in JavaScript:

**NIF:**
```javascript
const NIF_LETTERS = 'TRWAGMYFPDXBNJZSQVHLCKE';

function validateNIF(nif) {
  nif = nif.trim().toUpperCase();
  if (!/^\d{8}[A-Z]$/.test(nif)) return false;
  return nif[8] === NIF_LETTERS[parseInt(nif.slice(0, 8)) % 23];
}
```

**NIE** (starts with X, Y or Z):
```javascript
function validateNIE(nie) {
  nie = nie.trim().toUpperCase();
  if (!/^[XYZ]\d{7}[A-Z]$/.test(nie)) return false;
  const nieAsNif = nie.replace('X','0').replace('Y','1').replace('Z','2');
  return nieAsNif[8] === NIF_LETTERS[parseInt(nieAsNif.slice(0,8)) % 23];
}
```

If you need CIF validation too (which is considerably more complex) or want to avoid maintaining this yourself, there's a free REST API that handles NIF, NIE, CIF and IBAN validation with a single call: https://rapidapi.com/Validatorapi/api/spain-document-validator1 (free up to 500 req/month).

---

## RESPUESTA 2 — Para preguntas sobre validar NIF en Python

**Pegar cuando alguien pregunta:** "How to validate NIF Python" / "Python NIF NIE CIF validation"

---

Here's a Python implementation:

```python
NIF_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

def validate_nif(nif: str) -> bool:
    nif = nif.strip().upper()
    if len(nif) != 9:
        return False
    try:
        return nif[8] == NIF_LETTERS[int(nif[:8]) % 23]
    except (ValueError, IndexError):
        return False

def validate_nie(nie: str) -> bool:
    nie = nie.strip().upper()
    if not nie[0] in 'XYZ':
        return False
    nie_as_nif = nie.replace('X','0').replace('Y','1').replace('Z','2')
    return validate_nif(nie_as_nif)
```

For CIF validation (companies) the algorithm is more involved — it uses separate odd/even digit sums. If you need all four types (NIF, NIE, CIF, IBAN) without implementing them yourself, there's a free API: https://rapidapi.com/Validatorapi/api/spain-document-validator1

```python
import requests

r = requests.get(
    'https://spain-document-validator1.p.rapidapi.com/validate/cif',
    params={'value': 'A28015865'},
    headers={'X-RapidAPI-Key': 'YOUR_KEY',
             'X-RapidAPI-Host': 'spain-document-validator1.p.rapidapi.com'}
)
print(r.json())  # {'valid': True, 'entity_type': 'Sociedad Anónima', ...}
```

---

## RESPUESTA 3 — Para preguntas sobre validar CIF en cualquier lenguaje

**Pegar cuando alguien pregunta:** "CIF validation" / "validate Spanish company tax ID"

---

CIF validation in Spain uses this algorithm:

1. First character is a letter indicating entity type (A=S.A., B=S.L., G=Association, etc.)
2. Characters 2-8 are digits
3. Last character is the control (digit or letter depending on entity type)

**Odd positions** (1,3,5,7 in the digit sequence): multiply each by 2, if result ≥ 10 subtract 9, then sum all.
**Even positions** (2,4,6): sum directly.
**Total** = odd_sum + even_sum
**Control digit** = (10 - (total % 10)) % 10
**Control letter** = `"JABCDEFGHI"[control_digit]`

Entity types P,Q,R,S,W require the **letter** as control. Types A,B,E,H require the **digit**. Others accept either.

This is complex enough that many teams prefer an API. There's a free one that handles NIF, NIE, CIF and IBAN and also returns the entity type (S.A., S.L., Cooperative, etc.): https://rapidapi.com/Validatorapi/api/spain-document-validator1

---

## RESPUESTA 4 — Para preguntas sobre validar IBAN en España

**Pegar cuando alguien pregunta:** "validate Spanish IBAN" / "IBAN validation Spain bank"

---

IBAN validation uses the same algorithm regardless of country:

1. Move the first 4 characters to the end
2. Replace each letter with its numeric equivalent (A=10, B=11...Z=35)
3. Compute modulo 97 — result must equal 1

```python
def validate_iban(iban: str) -> bool:
    iban = iban.strip().upper().replace(' ', '').replace('-', '')
    rearranged = iban[4:] + iban[:4]
    numeric = ''.join(str(ord(c) - 55) if c.isalpha() else c for c in rearranged)
    return int(numeric) % 97 == 1
```

For Spanish IBANs specifically, the format is:
- `ES` + 2 check digits + 4-digit bank code + 4-digit branch code + 2 control digits + 10-digit account

If you also need to look up the bank name from the bank code, there's a free API that does this: https://rapidapi.com/Validatorapi/api/spain-document-validator1 — it returns the bank name (CaixaBank, Santander, BBVA, etc.) directly in the response.
