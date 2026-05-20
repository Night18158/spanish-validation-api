# Spain Document Validator API

REST API for validating Spanish fiscal and identification documents: **NIF, NIE, CIF and IBAN**.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Spain%20Document%20Validator-blue)](https://rapidapi.com/Validatorapi/api/spain-document-validator1)
[![Live Docs](https://img.shields.io/badge/Docs-Interactive%20Playground-green)](https://spanish-validation-api.vercel.app/docs)

## Available on RapidAPI

**Free tier: 500 requests/month** — [Subscribe here](https://rapidapi.com/Validatorapi/api/spain-document-validator1)

| Plan | Requests/month | Price |
|------|---------------|-------|
| Basic | 500 | Free |
| Pro | 15,000 | $9/mo |
| Ultra | 100,000 | $29/mo |

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/validate/nif` | Validate a Spanish NIF |
| GET | `/validate/nie` | Validate a Spanish NIE |
| GET | `/validate/cif` | Validate a Spanish CIF + entity type |
| GET | `/validate/iban` | Validate IBAN (77 countries) + bank name |

All endpoints accept a single query parameter: `value`

---

## Quick Start

### JavaScript

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
// { input: '12345678Z', valid: true, type: 'NIF' }
```

### Python

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

### PHP

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
// $response->bank_name = 'CaixaBank'
```

---

## Response Examples

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

## Tech Stack

- **Python** + **FastAPI**
- Deployed on **Vercel** (serverless)
- Hosted on **RapidAPI** marketplace

## Interactive Docs

Full API documentation and playground: [spanish-validation-api.vercel.app/docs](https://spanish-validation-api.vercel.app/docs)
