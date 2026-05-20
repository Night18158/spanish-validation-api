# How to Validate Spanish IBAN and Look Up Bank Names (2026)

If you're building a fintech, e-commerce or HR app for the Spanish market, you'll eventually need to validate IBANs — and often you'll also want to show the user the bank name associated with their account. This guide covers both.

---

## Spanish IBAN format

A Spanish IBAN has exactly 24 characters:

```
ES + 2 check digits + 4-digit bank code + 4-digit branch code + 2 control digits + 10-digit account
```

Example: `ES91 2100 0418 4502 0005 1332`
- `ES` — country code
- `91` — check digits
- `2100` — bank code (CaixaBank)
- `0418` — branch code
- `45` — control digits
- `0200051332` — account number

---

## The validation algorithm

IBAN validation is the same for all countries:

1. Move the first 4 characters to the end
2. Replace each letter with its numeric value (A=10, B=11...Z=35)
3. Calculate modulo 97 — result must equal 1

```python
def validate_iban(iban: str) -> bool:
    iban = iban.strip().upper().replace(' ', '').replace('-', '')
    if len(iban) != 24:  # Spanish IBANs are always 24 chars
        return False
    rearranged = iban[4:] + iban[:4]
    numeric = ''.join(str(ord(c) - 55) if c.isalpha() else c for c in rearranged)
    return int(numeric) % 97 == 1
```

```javascript
function validateIBAN(iban) {
  iban = iban.replace(/\s+/g, '').toUpperCase();
  const rearranged = iban.slice(4) + iban.slice(0, 4);
  const numeric = rearranged.split('').map(c =>
    isNaN(c) ? (c.charCodeAt(0) - 55).toString() : c
  ).join('');
  return BigInt(numeric) % 97n === 1n;
}
```

---

## Getting the bank name from the bank code

The bank code is characters 5-8 of the IBAN (positions 4-7, zero-indexed). Some common Spanish banks:

| Bank code | Bank |
|-----------|------|
| 2100 | CaixaBank |
| 0049 | Santander |
| 0075 | Banco Popular |
| 0182 | BBVA |
| 1465 | ING |
| 0487 | Bankinter |
| 2085 | Ibercaja |
| 0081 | Banco Sabadell |

There are over 200 registered Spanish bank codes. Maintaining a complete list is complex — it changes as banks merge and new ones appear.

---

## Option 2: Use an API (bank name included automatically)

If you need a complete, up-to-date bank name lookup without maintaining the list yourself, the [Spain Document Validator API](https://rapidapi.com/Validatorapi/api/spain-document-validator1) returns the bank name directly in the response:

```python
import requests

r = requests.get(
    'https://spain-document-validator1.p.rapidapi.com/validate/iban',
    params={'value': 'ES9121000418450200051332'},
    headers={
        'X-RapidAPI-Key': 'YOUR_KEY',
        'X-RapidAPI-Host': 'spain-document-validator1.p.rapidapi.com'
    }
)
print(r.json())
```

Response:
```json
{
  "input": "ES9121000418450200051332",
  "valid": true,
  "type": "IBAN",
  "country": "ES",
  "formatted": "ES91 2100 0418 4502 0005 1332",
  "bank_code": "2100",
  "branch_code": "0418",
  "bank_name": "CaixaBank"
}
```

Free tier: 500 requests/month. No credit card required.

---

## When to implement it yourself vs. use an API

| | DIY | API |
|---|---|---|
| IBAN validation | 10 lines of code | 3 lines |
| Bank name lookup | Maintain 200+ bank codes | Included |
| Handles bank mergers | Manual updates | Automatic |
| Works in any language | One implementation per lang | Yes |

For pure IBAN validation, the DIY approach is simple enough. For bank name lookup, the API saves significant maintenance effort.

---

*Full API docs and interactive playground: [spanish-validation-api.vercel.app/docs](https://spanish-validation-api.vercel.app/docs)*
