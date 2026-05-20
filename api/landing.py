LANDING_HTML = """<!DOCTYPE html>
<html lang="en" id="html-root">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spain Document Validator API — NIF, NIE, CIF, IBAN Validation</title>
  <meta name="description" content="Free REST API to validate Spanish NIF, NIE, CIF and IBAN. 500 requests/month free. Works in JavaScript, Python, PHP and any language. No setup required.">
  <meta name="keywords" content="NIF validation API, NIE validation, CIF validation, IBAN validation Spain, validate NIF JavaScript, validate CIF Python, Spanish tax ID API">
  <meta property="og:title" content="Spain Document Validator API">
  <meta property="og:description" content="Free REST API to validate Spanish NIF, NIE, CIF and IBAN. 500 req/month free.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://spanish-validation-api.vercel.app">
  <link rel="canonical" href="https://spanish-validation-api.vercel.app">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Spain Document Validator API",
    "description": "REST API for validating Spanish fiscal documents: NIF, NIE, CIF and IBAN",
    "url": "https://spanish-validation-api.vercel.app",
    "applicationCategory": "DeveloperApplication",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD",
      "description": "Free tier: 500 requests/month"
    }
  }
  </script>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #1a1a2e; line-height: 1.6; }
    a { color: #0066cc; text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* ── Language toggle ── */
    .es-content { display: none; }
    #html-root.es .es-content { display: revert; }
    #html-root.es .en-content { display: none; }
    .lang-switcher { position: absolute; top: 18px; right: 20px; display: flex; gap: 6px; }
    .lang-btn { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.45); color: white;
                padding: 5px 13px; border-radius: 6px; cursor: pointer; font-size: 0.82rem; font-weight: 600;
                transition: background 0.2s; }
    .lang-btn:hover { background: rgba(255,255,255,0.22); }
    .lang-btn.active { background: rgba(255,255,255,0.28); border-color: white; }

    .hero { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color: white; padding: 80px 20px 72px; text-align: center; position: relative; }
    .hero h1 { font-size: 2.8rem; font-weight: 800; margin-bottom: 16px; }
    .hero h1 span { color: #c8aa6e; }
    .hero p { font-size: 1.2rem; color: #a0aec0; max-width: 600px; margin: 0 auto 32px; }
    .badge { display: inline-block; background: #22c55e; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 24px; }
    .btn { display: inline-block; background: #c8aa6e; color: #1a1a2e; padding: 14px 32px; border-radius: 8px; font-weight: 700; font-size: 1rem; margin: 8px; transition: opacity 0.2s; }
    .btn:hover { opacity: 0.9; text-decoration: none; }
    .btn-outline { background: transparent; color: white; border: 2px solid #a0aec0; }

    .section { padding: 64px 20px; max-width: 960px; margin: 0 auto; }
    .section h2 { font-size: 1.8rem; font-weight: 700; margin-bottom: 32px; text-align: center; }

    .endpoints { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 48px; }
    .endpoint { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; text-align: center; }
    .endpoint .method { background: #3b82f6; color: white; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }
    .endpoint .path { font-family: monospace; font-size: 0.95rem; font-weight: 600; color: #1a1a2e; display: block; margin-bottom: 8px; }
    .endpoint p { font-size: 0.85rem; color: #64748b; }

    .code-block { background: #1e293b; border-radius: 12px; padding: 24px; margin: 16px 0; overflow-x: auto; }
    .code-block pre { color: #e2e8f0; font-family: 'Courier New', monospace; font-size: 0.9rem; line-height: 1.6; }

    .pricing { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; }
    .plan { border: 2px solid #e2e8f0; border-radius: 12px; padding: 32px 24px; text-align: center; }
    .plan.featured { border-color: #3b82f6; position: relative; }
    .plan.featured::before { content: "Recommended"; background: #3b82f6; color: white; font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 20px; position: absolute; top: -14px; left: 50%; transform: translateX(-50%); }
    #html-root.es .plan.featured::before { content: "Recomendado"; }
    .plan h3 { font-size: 1.2rem; font-weight: 700; margin-bottom: 8px; }
    .plan .price { font-size: 2.5rem; font-weight: 800; color: #1a1a2e; }
    .plan .price span { font-size: 1rem; color: #64748b; }
    .plan .requests { color: #64748b; margin: 8px 0 24px; font-size: 0.95rem; }
    .plan .cta { display: block; background: #1a1a2e; color: white; padding: 12px; border-radius: 8px; font-weight: 600; }
    .plan.featured .cta { background: #3b82f6; }

    .response-example { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 24px; margin: 16px 0; }
    .response-example h4 { color: #166534; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-bottom: 12px; }
    .response-example pre { font-family: monospace; font-size: 0.9rem; color: #1a1a2e; }

    .faq { max-width: 720px; margin: 0 auto; }
    .faq-item { border-bottom: 1px solid #e2e8f0; padding: 24px 0; }
    .faq-item h3 { font-size: 1.05rem; font-weight: 600; margin-bottom: 8px; }
    .faq-item p { color: #64748b; }

    /* ── Cross-promo ── */
    .crosspromo { background: #f8fafc; border-top: 1px solid #e2e8f0; padding: 56px 20px; text-align: center; }
    .crosspromo-inner { max-width: 640px; margin: 0 auto; }
    .crosspromo-label { font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: #94a3b8; margin-bottom: 20px; }
    .crosspromo-card { background: white; border: 2px solid #012169; border-radius: 16px; padding: 28px 32px; display: flex; align-items: center; gap: 24px; text-align: left; }
    .crosspromo-flag { font-size: 3rem; flex-shrink: 0; line-height: 1; }
    .crosspromo-card h3 { font-size: 1.15rem; font-weight: 700; color: #012169; margin-bottom: 8px; }
    .crosspromo-card p { color: #64748b; font-size: 0.92rem; margin-bottom: 16px; }
    .crosspromo-btn { display: inline-block; background: #012169; color: white; padding: 10px 22px; border-radius: 8px; font-weight: 600; font-size: 0.9rem; }
    .crosspromo-btn:hover { opacity: 0.88; text-decoration: none; }
    @media (max-width: 520px) { .crosspromo-card { flex-direction: column; text-align: center; } }

    footer { background: #1a1a2e; color: #a0aec0; text-align: center; padding: 32px 20px; font-size: 0.9rem; }
    footer a { color: #c8aa6e; }

    @media (max-width: 640px) { .hero h1 { font-size: 1.8rem; } }
  </style>
</head>
<body>

<!-- ═══════════════ HERO ═══════════════ -->
<section class="hero">

  <!-- Language toggle -->
  <div class="lang-switcher">
    <button class="lang-btn active" id="btn-en" onclick="setLang('en')">🇬🇧 EN</button>
    <button class="lang-btn" id="btn-es" onclick="setLang('es')">🇪🇸 ES</button>
  </div>

  <div class="badge">
    <span class="en-content">Free tier available</span>
    <span class="es-content">Tier gratuito disponible</span>
  </div>

  <h1>
    <span class="en-content">Spanish Document <span style="color:#c8aa6e">Validator API</span></span>
    <span class="es-content">API Validadora de <span style="color:#c8aa6e">Documentos Españoles</span></span>
  </h1>

  <p>
    <span class="en-content">Validate NIF, NIE, CIF and IBAN with a single API call. Works in any programming language. No setup required.</span>
    <span class="es-content">Valida NIF, NIE, CIF e IBAN con una sola llamada API. Compatible con cualquier lenguaje de programación. Sin configuración.</span>
  </p>

  <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="btn">
    <span class="en-content">Get Free API Key</span>
    <span class="es-content">Obtener API Key Gratis</span>
  </a>
  <a href="/docs" class="btn btn-outline">
    <span class="en-content">Interactive Docs</span>
    <span class="es-content">Documentación Interactiva</span>
  </a>
</section>

<!-- ═══════════════ ENDPOINTS ═══════════════ -->
<div class="section">
  <h2>
    <span class="en-content">4 Endpoints. Everything you need.</span>
    <span class="es-content">4 Endpoints. Todo lo que necesitas.</span>
  </h2>
  <div class="endpoints">
    <div class="endpoint" style="border-color:#c8aa6e; background:#fffbf0;">
      <span class="method" style="background:#c8aa6e; color:#1a1a2e;">GET</span>
      <span class="path">/validate/detect</span>
      <p>
        <span class="en-content"><strong>New.</strong> Pass any document — type is detected automatically.</span>
        <span class="es-content"><strong>Nuevo.</strong> Pasa cualquier documento — el tipo se detecta automáticamente.</span>
      </p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/nif</span>
      <p>
        <span class="en-content">Validate Spanish NIF for individuals. Handles K, L, M special cases.</span>
        <span class="es-content">Valida el NIF español para personas físicas. Gestiona los casos especiales K, L, M.</span>
      </p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/nie</span>
      <p>
        <span class="en-content">Validate NIE for foreign residents. X, Y, Z prefix support.</span>
        <span class="es-content">Valida el NIE para residentes extranjeros. Soporta prefijos X, Y, Z.</span>
      </p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/cif</span>
      <p>
        <span class="en-content">Validate company CIF. Returns entity type: S.A., S.L., Cooperative...</span>
        <span class="es-content">Valida el CIF de empresa. Devuelve el tipo de entidad: S.A., S.L., Cooperativa...</span>
      </p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/iban</span>
      <p>
        <span class="en-content">Validate IBAN for 77 countries. Returns bank name for Spanish accounts.</span>
        <span class="es-content">Valida IBAN de 77 países. Devuelve el nombre del banco para cuentas españolas.</span>
      </p>
    </div>
  </div>

  <h2>
    <span class="en-content">Quick Start</span>
    <span class="es-content">Inicio Rápido</span>
  </h2>
  <div class="code-block">
    <pre><code># Python
import requests

r = requests.get(
    "https://spain-document-validator1.p.rapidapi.com/validate/cif",
    params={"value": "A28015865"},
    headers={
        "X-RapidAPI-Key": "YOUR_KEY",
        "X-RapidAPI-Host": "spain-document-validator1.p.rapidapi.com"
    }
)
print(r.json())
# {'valid': True, 'type': 'CIF', 'entity_type': 'Sociedad Anonima'}</code></pre>
  </div>

  <div class="response-example">
    <h4>
      <span class="en-content">IBAN Response example</span>
      <span class="es-content">Ejemplo de respuesta IBAN</span>
    </h4>
    <pre>{
  "input": "ES9121000418450200051332",
  "valid": true,
  "type": "IBAN",
  "country": "ES",
  "formatted": "ES91 2100 0418 4502 0005 1332",
  "bank_code": "2100",
  "branch_code": "0418",
  "bank_name": "CaixaBank"
}</pre>
  </div>
</div>

<!-- ═══════════════ PRICING ═══════════════ -->
<div style="background:#f8fafc; padding: 64px 20px;">
  <div style="max-width:960px; margin:0 auto;">
    <h2 style="font-size:1.8rem; font-weight:700; text-align:center; margin-bottom:32px;">
      <span class="en-content">Pricing</span>
      <span class="es-content">Precios</span>
    </h2>
    <div class="pricing">
      <div class="plan">
        <h3><span class="en-content">Basic</span><span class="es-content">Básico</span></h3>
        <div class="price">$0<span>/mo</span></div>
        <div class="requests">
          <span class="en-content">500 requests / month</span>
          <span class="es-content">500 peticiones / mes</span>
        </div>
        <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="cta">
          <span class="en-content">Get Started Free</span>
          <span class="es-content">Empezar Gratis</span>
        </a>
      </div>
      <div class="plan featured">
        <h3>Pro</h3>
        <div class="price">$9<span>/mo</span></div>
        <div class="requests">
          <span class="en-content">15,000 requests / month</span>
          <span class="es-content">15.000 peticiones / mes</span>
        </div>
        <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="cta">
          <span class="en-content">Subscribe</span>
          <span class="es-content">Suscribirse</span>
        </a>
      </div>
      <div class="plan">
        <h3>Ultra</h3>
        <div class="price">$29<span>/mo</span></div>
        <div class="requests">
          <span class="en-content">100,000 requests / month</span>
          <span class="es-content">100.000 peticiones / mes</span>
        </div>
        <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="cta">
          <span class="en-content">Subscribe</span>
          <span class="es-content">Suscribirse</span>
        </a>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════ FAQ ═══════════════ -->
<div class="section">
  <h2>
    <span class="en-content">Frequently Asked Questions</span>
    <span class="es-content">Preguntas Frecuentes</span>
  </h2>
  <div class="faq">
    <div class="faq-item">
      <h3>
        <span class="en-content">What is a NIF?</span>
        <span class="es-content">¿Qué es un NIF?</span>
      </h3>
      <p>
        <span class="en-content">NIF (Número de Identificación Fiscal) is the tax ID for Spanish individuals. Format: 8 digits + 1 control letter (e.g. 12345678Z).</span>
        <span class="es-content">El NIF (Número de Identificación Fiscal) es el identificador fiscal de los particulares españoles. Formato: 8 dígitos + 1 letra de control (ej. 12345678Z).</span>
      </p>
    </div>
    <div class="faq-item">
      <h3>
        <span class="en-content">What is a CIF?</span>
        <span class="es-content">¿Qué es un CIF?</span>
      </h3>
      <p>
        <span class="en-content">CIF (Código de Identificación Fiscal) is the tax ID for Spanish companies. The API also returns the entity type: S.A., S.L., Cooperative, etc.</span>
        <span class="es-content">El CIF (Código de Identificación Fiscal) es el identificador fiscal de las empresas españolas. La API también devuelve el tipo de entidad: S.A., S.L., Cooperativa, etc.</span>
      </p>
    </div>
    <div class="faq-item">
      <h3>
        <span class="en-content">Does it work for non-Spanish IBANs?</span>
        <span class="es-content">¿Funciona con IBANs de otros países?</span>
      </h3>
      <p>
        <span class="en-content">Yes. The IBAN validator supports 77 countries using the standard mod-97 algorithm. Bank name lookup is only available for Spanish accounts.</span>
        <span class="es-content">Sí. El validador de IBAN soporta 77 países mediante el algoritmo mod-97 estándar. El nombre del banco solo está disponible para cuentas españolas.</span>
      </p>
    </div>
    <div class="faq-item">
      <h3>
        <span class="en-content">Do I need to sign up?</span>
        <span class="es-content">¿Necesito registrarme?</span>
      </h3>
      <p>
        <span class="en-content">Yes, a free RapidAPI account is required to get your API key. The free tier includes 500 requests/month with no credit card needed.</span>
        <span class="es-content">Sí, se requiere una cuenta gratuita de RapidAPI para obtener tu API key. El tier gratuito incluye 500 peticiones/mes sin tarjeta de crédito.</span>
      </p>
    </div>
    <div class="faq-item">
      <h3>
        <span class="en-content">What programming languages are supported?</span>
        <span class="es-content">¿Qué lenguajes de programación son compatibles?</span>
      </h3>
      <p>
        <span class="en-content">Any language that can make HTTP GET requests. RapidAPI provides code snippets for JavaScript, Python, PHP, Ruby, Go, Java, Swift and more.</span>
        <span class="es-content">Cualquier lenguaje que pueda hacer peticiones HTTP GET. RapidAPI proporciona snippets de código para JavaScript, Python, PHP, Ruby, Go, Java, Swift y más.</span>
      </p>
    </div>
  </div>
</div>

<!-- ═══════════════ CROSS-PROMO: UK ═══════════════ -->
<div class="crosspromo">
  <div class="crosspromo-inner">
    <div class="crosspromo-label">
      <span class="en-content">Also available</span>
      <span class="es-content">También disponible</span>
    </div>
    <div class="crosspromo-card">
      <div class="crosspromo-flag">🇬🇧</div>
      <div>
        <h3>UK Document Validator API</h3>
        <p>
          <span class="en-content">Need to validate UK documents too? VAT numbers, NINO, Company Numbers and UTR — same free tier, same simple API.</span>
          <span class="es-content">¿También necesitas validar documentos del Reino Unido? IVA (VAT), NINO, números de empresa y UTR — mismo tier gratuito, misma API sencilla.</span>
        </p>
        <a href="https://uk-validation-api.vercel.app" class="crosspromo-btn">
          <span class="en-content">View UK Validator →</span>
          <span class="es-content">Ver validador UK →</span>
        </a>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════ FOOTER ═══════════════ -->
<footer>
  <p>Spain Document Validator API &mdash; <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1">RapidAPI</a> &mdash; <a href="/docs">API Docs</a></p>
</footer>

<script>
  function setLang(lang) {
    var root = document.getElementById('html-root');
    if (lang === 'es') {
      root.classList.add('es');
      root.setAttribute('lang', 'es');
    } else {
      root.classList.remove('es');
      root.setAttribute('lang', 'en');
    }
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');
    document.getElementById('btn-es').classList.toggle('active', lang === 'es');
    try { localStorage.setItem('validator_lang', lang); } catch(e) {}
  }
  (function() {
    try {
      var saved = localStorage.getItem('validator_lang');
      if (saved === 'es') setLang('es');
    } catch(e) {}
  })();
</script>

</body>
</html>"""
