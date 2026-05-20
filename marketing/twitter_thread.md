# Twitter/X Thread — Spain Document Validator

## Thread 1 — Educativo (algoritmo NIF)

1/ Did you know Spanish NIF validation uses a mod-23 algorithm?

Here's how it works in 4 lines of Python: 🧵

2/ Take the 8-digit number from the NIF, calculate number % 23, and look up the result in this string:

TRWAGMYFPDXBNJZSQVHLCKE

That index is the expected control letter.

3/ Example: NIF 12345678Z
- 12345678 % 23 = 22
- TRWAGMYFPDXBNJZSQVHLCK**E** → index 22 = E ✓

4/ NIE works the same but replace X→0, Y→1, Z→2 first.

CIF is more complex — uses odd/even position digit sums. 

5/ If you need NIF, NIE, CIF and IBAN validation without implementing it yourself, I built a free API:
https://rapidapi.com/Validatorapi/api/spain-document-validator1

500 req/month free. Works in any language.

---

## Thread 2 — Lanzamiento (en español)

1/ Acabo de lanzar una API gratuita para validar documentos españoles: NIF, NIE, CIF e IBAN 🇪🇸

Gratis hasta 500 peticiones/mes. Hilo 🧵

2/ ¿Por qué la construí?

Estaba trabajando en un proyecto para el mercado español y no encontré ninguna API bien documentada y gratuita para esto.

3/ Lo que devuelve:
- NIF/NIE: válido/inválido + letra esperada
- CIF: tipo de entidad (S.A., S.L., Cooperativa...)
- IBAN: nombre del banco (CaixaBank, Santander, BBVA...)

4/ Ejemplo para un IBAN español:

{"bank_name": "CaixaBank", "valid": true, "formatted": "ES91 2100 0418 4502 0005 1332"}

5/ Disponible en RapidAPI:
https://rapidapi.com/Validatorapi/api/spain-document-validator1

Documentación interactiva:
https://spanish-validation-api.vercel.app

---

## NOTAS
- Publicar Thread 1 en inglés primero (más alcance)
- Publicar Thread 2 en español una semana después
- Interactuar con tweets que hablen de "validar NIF", "Spain fintech", "Spanish market API"
- Hashtags: #webdev #python #api #spain #fintech
