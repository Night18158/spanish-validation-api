# Product Hunt Launch Kit

## Cuándo lanzar
- Esperar a tener al menos 5-10 suscriptores en RapidAPI
- Lanzar martes o miércoles (más tráfico en Product Hunt)
- Hora: 12:01 AM PST (las 9:01 de la mañana en España)

## Título
Spain Document Validator

## Tagline (60 chars max)
Free API for Spanish NIF, NIE, CIF and IBAN validation

## Descripción corta
```
Validate Spanish fiscal documents with a single API call.

✅ NIF validation (individuals) — includes K/L/M special cases
✅ NIE validation (foreign residents)
✅ CIF validation (companies) — returns entity type: S.A., S.L., Cooperative...
✅ IBAN validation (77 countries) — returns bank name for Spanish accounts
✅ Auto-detect endpoint — pass any document, type is detected automatically

Free tier: 500 requests/month. No credit card required.
Works in JavaScript, Python, PHP, Ruby, Go, or any language with HTTP.
```

## Topics a seleccionar en Product Hunt
- Developer Tools
- APIs
- Finance
- Spain

## Primer comentario (tuyo, al lanzar)
```
Hi Product Hunt! 👋

I built this after struggling to find a clean Spanish document validation API for a project.

The algorithms themselves are well-documented but surprisingly annoying to implement correctly — especially CIF (which has three different control character modes depending on entity type) and NIE (which requires a letter substitution step before applying the NIF algorithm).

The auto-detect endpoint (/validate/detect) is my favorite feature — you pass any document and it figures out the type automatically. Useful for forms where users can enter different document types.

Happy to answer questions about the algorithms or the API!
```

## Qué necesitas antes de lanzar
- [ ] Tener la cuenta de Product Hunt con al menos 1 semana de antigüedad
- [ ] Conseguir que al menos 5 personas voten en las primeras 2 horas (pídelo en Indie Hackers, r/webdev, etc.)
- [ ] Preparar 3-4 imágenes/screenshots para la galería del producto
- [ ] Subir el logo (usar logo.png del proyecto)
