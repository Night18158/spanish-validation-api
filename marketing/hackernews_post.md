# Hacker News — Show HN Post

**Título:**
Show HN: Free REST API for Spanish NIF/NIE/CIF/IBAN validation (500 req/mo free)

**Cuerpo:**
I built a REST API for validating Spanish fiscal documents after struggling to find a clean solution for a project targeting the Spanish market.

It validates:
- NIF (individuals) — mod-23 algorithm with TRWAGMYFPDXBNJZSQVHLCKE table
- NIE (foreign residents) — X→0, Y→1, Z→2 substitution then NIF algorithm
- CIF (companies) — odd/even digit sums, returns entity type (S.A., S.L., Cooperative, etc.)
- IBAN (77 countries) — mod-97 check, returns bank name for Spanish accounts

Tech: Python + FastAPI deployed on Vercel serverless.

Available on RapidAPI: https://rapidapi.com/Validatorapi/api/spain-document-validator1
Live docs: https://spanish-validation-api.vercel.app

---

**CUÁNDO PUBLICAR:** Martes o miércoles por la mañana (hora del Este, 9-11am)
**SUBREDDIT equivalente:** news.ycombinator.com → Submit → Show HN
**NOTA:** Hacker News penaliza cuentas nuevas. Esperar a tener karma o usar cuenta existente.
