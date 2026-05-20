# How to Validate Spanish NIF, NIE, CIF and IBAN in Any Programming Language (2026)

If you're building software for the Spanish market, sooner or later you'll need to validate fiscal documents. This guide covers everything: how the algorithms work, code examples in 4 languages, and the fastest way to add validation to any project.

---

## What are NIF, NIE and CIF?

- **NIF** — Tax ID for Spanish individuals (8 digits + 1 letter, e.g. `12345678Z`)
- **NIE** — Tax ID for foreign residents in Spain (X/Y/Z + 7 digits + letter, e.g. `X1234567L`)
- **CIF** — Tax ID for Spanish companies (1 letter + 7 digits + 1 control char, e.g. `A28015865`). Also returns the company type: S.A., S.L., Cooperative, etc.
- **IBAN** — Bank account number, 24 characters for Spanish accounts (e.g. `ES9121000418450200051332`)

---

## Option 1: Implement it yourself

### NIF validation (JavaScript)

```javascript
const NIF_LETTERS = 'TRWAGMYFPDXBNJZSQVHLCKE';

function validateNIF(nif) {
  nif = nif.trim().toUpperCase();
  if (nif.length !== 9) return false;
  const number = parseInt(nif.slice(0, 8), 10);
  if (isNaN(number)) return false;
  return nif[8] === NIF_LETTERS[number % 23];
}

console.log(validateNIF('12345678Z')); // true
console.log(validateNIF('12345678A')); // false
```

### NIF validation (Python)

```python
NIF_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

def validate_nif(nif: str) -> bool:
    nif = nif.strip().upper()
    if len(nif) != 9:
        return False
    try:
        number = int(nif[:8])
    except ValueError:
        return False
    return nif[8] == NIF_LETTERS[number % 23]

print(validate_nif("12345678Z"))  # True
```

### NIF validation (PHP)

```php
function validateNIF(string $nif): bool {
    $letters = 'TRWAGMYFPDXBNJZSQVHLCKE';
    $nif = strtoupper(trim($nif));
    if (strlen($nif) !== 9) return false;
    $number = intval(substr($nif, 0, 8));
    return $nif[8] === $letters[$number % 23];
}

var_dump(validateNIF('12345678Z')); // bool(true)
```

---

## Option 2: Use an API (3 lines of code, any language)

If you don't want to implement and maintain the algorithms yourself — especially for CIF which is significantly more complex — you can use the [Spain Document Validator API](https://rapidapi.com/Validatorapi/api/spain-document-validator1) on RapidAPI. It's free for up to 500 requests/month.

### JavaScript (fetch)

```javascript
const response = await fetch(
  'https://spain-document-validator1.p.rapidapi.com/validate/nif?value=12345678Z',
  {
    headers: {
      'X-RapidAPI-Key': 'YOUR_API_KEY',
      'X-RapidAPI-Host': 'spain-document-validator1.p.rapidapi.com'
    }
  }
);
const data = await response.json();
console.log(data);
// { input: '12345678Z', valid: true, type: 'NIF' }
```

### Python (requests)

```python
import requests

response = requests.get(
    'https://spain-document-validator1.p.rapidapi.com/validate/cif',
    params={'value': 'A28015865'},
    headers={
        'X-RapidAPI-Key': 'YOUR_API_KEY',
        'X-RapidAPI-Host': 'spain-document-validator1.p.rapidapi.com'
    }
)
print(response.json())
# {'input': 'A28015865', 'valid': True, 'type': 'CIF', 'entity_type': 'Sociedad Anónima'}
```

### PHP (cURL)

```php
$curl = curl_init();
curl_setopt_array($curl, [
    CURLOPT_URL => 'https://spain-document-validator1.p.rapidapi.com/validate/iban?value=ES9121000418450200051332',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'X-RapidAPI-Key: YOUR_API_KEY',
        'X-RapidAPI-Host: spain-document-validator1.p.rapidapi.com'
    ],
]);
$response = json_decode(curl_exec($curl));
// $response->bank_name = "CaixaBank"
```

---

## API response examples

**NIF:**
```json
{ "input": "12345678Z", "valid": true, "type": "NIF" }
```

**CIF:**
```json
{
  "input": "A28015865",
  "valid": true,
  "type": "CIF",
  "entity_type": "Sociedad Anónima"
}
```

**IBAN:**
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

---

## When to use the API vs implementing it yourself

| | DIY | API |
|---|---|---|
| Setup time | 2-4 hours | 5 minutes |
| Works in any language | Requires separate lib per lang | Yes |
| CIF entity type info | Extra work | Included |
| IBAN bank name lookup | Very complex | Included |
| Maintenance when rules change | Your problem | Automatic |

The [free tier (500 req/month)](https://rapidapi.com/Validatorapi/api/spain-document-validator1) is enough for most small projects. Paid plans start at $9/month for 15,000 requests.

---

*The full API documentation and interactive playground is available at [spanish-validation-api.vercel.app/docs](https://spanish-validation-api.vercel.app/docs).*
