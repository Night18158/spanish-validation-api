# 5 Common Mistakes When Validating Spanish Tax IDs (NIF, NIE, CIF)

If you're building software for the Spanish market, fiscal document validation is something you'll encounter sooner or later. Here are the most common mistakes developers make — and how to avoid them.

---

## Mistake 1: Treating NIE as just a "foreign NIF"

NIE and NIF use the same control letter algorithm, but NIE starts with X, Y or Z. A common mistake is forgetting the substitution step:

- X → 0
- Y → 1
- Z → 2

**Wrong:**
```python
def validate_nie(nie):
    return nie[8] == NIF_LETTERS[int(nie[:8]) % 23]  # FAILS — nie[:8] starts with X/Y/Z
```

**Correct:**
```python
def validate_nie(nie):
    nie = nie.strip().upper()
    substitution = {'X': '0', 'Y': '1', 'Z': '2'}
    nie_as_nif = substitution[nie[0]] + nie[1:]
    return nie[8] == NIF_LETTERS[int(nie_as_nif[:8]) % 23]
```

---

## Mistake 2: Forgetting special NIF prefixes (K, L, M)

Standard NIFs are 8 digits + 1 letter. But there are 3 special formats:

- **K** — Spanish citizens under 14 or foreigners without NIE
- **L** — Spanish citizens over 14 residing abroad
- **M** — Foreigners without permanent NIE

These also use the mod-23 algorithm, but the first character is a letter, not a digit.

If your regex is `^\d{8}[A-Z]$` you're silently rejecting valid documents.

---

## Mistake 3: Using the wrong control letter table

The control letter table for NIF/NIE is not alphabetical. It's:

```
TRWAGMYFPDXBNJZSQVHLCKE
```

Position 0 = T, position 1 = R, position 2 = W... Many developers hard-code this wrong after misreading a source.

Quick check: `12345678` % 23 = 22, so the expected letter is `E` (index 22 of the table). `12345678Z` is valid.

---

## Mistake 4: Assuming CIF control is always a digit

CIF validation has three cases:

- Entity types **P, Q, R, S, W** → control must be a **letter**
- Entity types **A, B, E, H** → control must be a **digit**
- All others → control can be **either**

Many implementations only check the numeric control and miss associations like Q28015865 (an organismo público).

The control letter table is: `JABCDEFGHI` (index 0 = J, index 1 = A...)

---

## Mistake 5: Not handling spaces and case

Users type IBANs with spaces: `ES91 2100 0418 4502 0005 1332`. Always normalize before validating:

```python
iban = iban.strip().upper().replace(' ', '').replace('-', '')
```

Same for NIF — users sometimes type lowercase. Always `.upper()` before processing.

---

## Avoiding all of this

If you don't want to maintain these edge cases yourself, there's a free API that handles all of them: [Spain Document Validator](https://rapidapi.com/Validatorapi/api/spain-document-validator1) — NIF, NIE, CIF and IBAN validation with a single GET request. It also returns `expected_letter` in the response, which is useful for debugging.

Free tier: 500 requests/month.

---

*Interactive playground: [spanish-validation-api.vercel.app/docs](https://spanish-validation-api.vercel.app/docs)*
