# Reddit Posts — Spain Document Validator

---

## POST 1 — r/webdev (inglés)

**Título:**
I built a free REST API to validate Spanish NIF, NIE, CIF and IBAN — no setup required

**Cuerpo:**
Been working on a project that needed Spanish document validation and couldn't find a clean, well-documented API for it. So I built one.

**Spain Document Validator** — free for up to 500 requests/month:

- `/validate/nif` — validates NIF (individuals), including K/L/M special cases
- `/validate/nie` — validates NIE (foreign residents)
- `/validate/cif` — validates CIF (companies) and returns the entity type (S.A., S.L., Cooperative, etc.)
- `/validate/iban` — validates IBAN for 77 countries, returns bank name and branch code for Spanish accounts

Example response for a CIF:
```json
{
  "input": "A28015865",
  "valid": true,
  "type": "CIF",
  "entity_type": "Sociedad Anónima"
}
```

Available on RapidAPI: https://rapidapi.com/Validatorapi/api/spain-document-validator1

Happy to answer questions or add endpoints if something's missing.

---

## POST 2 — r/Spain y r/es (español)

**Título:**
Hice una API gratuita para validar NIF, NIE, CIF e IBAN españoles

**Cuerpo:**
Estaba trabajando en un proyecto que necesitaba validar documentos fiscales españoles y no encontré nada bien documentado y gratuito, así que lo construí.

**Spain Document Validator** — gratis hasta 500 peticiones al mes:

- Valida NIF (con casos especiales K, L, M)
- Valida NIE
- Valida CIF y devuelve el tipo de entidad (S.A., S.L., Cooperativa...)
- Valida IBAN de 77 países, con nombre del banco y código de sucursal para cuentas españolas

Ejemplo de respuesta para un IBAN español:
```json
{
  "input": "ES9121000418450200051332",
  "valid": true,
  "bank_name": "CaixaBank",
  "formatted": "ES91 2100 0418 4502 0005 1332"
}
```

Disponible en RapidAPI: https://rapidapi.com/Validatorapi/api/spain-document-validator1

Si alguien lo necesita para PHP, Python, JS... en la documentación hay ejemplos de código para cada lenguaje.

---

## POST 3 — r/learnprogramming (inglés)

**Título:**
How Spanish NIF/CIF validation works (algorithm explained) + free API if you just need it to work

**Cuerpo:**
A lot of people building apps for the Spanish market ask about this, so here's a quick breakdown.

**NIF validation algorithm:**
1. Take the first 8 digits of the NIF
2. Calculate: `number % 23`
3. Look up the result in this string: `TRWAGMYFPDXBNJZSQVHLCKE`
4. That's the expected control letter

```python
NIF_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

def validate_nif(nif):
    number = int(nif[:8])
    return nif[8] == NIF_LETTERS[number % 23]
```

**NIE** works the same but you replace X→0, Y→1, Z→2 first.

**CIF** is more complex — it uses separate odd/even position sums and the control can be either a digit or a letter depending on the entity type prefix.

If you just need it to work without implementing it yourself, there's a free API for all of these including IBAN: https://rapidapi.com/Validatorapi/api/spain-document-validator1

---

## POST 4 — r/Python (inglés)

**Título:**
Free API for Spanish NIF/NIE/CIF/IBAN validation — Python example included

**Cuerpo:**
Quick share — built a REST API for Spanish document validation, might be useful for anyone building fintech, HR, or e-commerce apps targeting Spain.

Python example:

```python
import requests

def validate_spanish_doc(doc_type, value, api_key):
    url = f"https://spain-document-validator1.p.rapidapi.com/validate/{doc_type}"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spain-document-validator1.p.rapidapi.com"
    }
    response = requests.get(url, params={"value": value}, headers=headers)
    return response.json()

# Examples
print(validate_spanish_doc("nif", "12345678Z", "YOUR_KEY"))
print(validate_spanish_doc("cif", "A28015865", "YOUR_KEY"))
print(validate_spanish_doc("iban", "ES9121000418450200051332", "YOUR_KEY"))
```

Free tier: 500 requests/month. API: https://rapidapi.com/Validatorapi/api/spain-document-validator1

---

## REGLAS IMPORTANTES AL PUBLICAR EN REDDIT

- Espera al menos 3-4 días entre posts en subreddits diferentes
- No publiques el mismo texto exacto en dos sitios — modifica ligeramente cada post
- En r/webdev y r/learnprogramming NO hagas spam — asegúrate de participar también en otros hilos del subreddit el mismo día
- El mejor horario para publicar: martes a jueves entre 9:00-11:00 hora del Este (15:00-17:00 España)
