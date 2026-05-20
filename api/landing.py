LANDING_HTML = """<!DOCTYPE html>
<html lang="en">
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

    .hero { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color: white; padding: 80px 20px; text-align: center; }
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
    .tabs { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
    .tab { padding: 6px 16px; border-radius: 6px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: 2px solid #e2e8f0; color: #64748b; background: white; }
    .tab.active { border-color: #3b82f6; color: #3b82f6; background: #eff6ff; }

    .pricing { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; }
    .plan { border: 2px solid #e2e8f0; border-radius: 12px; padding: 32px 24px; text-align: center; }
    .plan.featured { border-color: #3b82f6; position: relative; }
    .plan.featured::before { content: "Recommended"; background: #3b82f6; color: white; font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 20px; position: absolute; top: -14px; left: 50%; transform: translateX(-50%); }
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

    footer { background: #1a1a2e; color: #a0aec0; text-align: center; padding: 32px 20px; font-size: 0.9rem; }
    footer a { color: #c8aa6e; }

    @media (max-width: 640px) {
      .hero h1 { font-size: 1.8rem; }
    }
  </style>
</head>
<body>

<section class="hero">
  <div class="badge">Free tier available</div>
  <h1>Spanish Document <span>Validator API</span></h1>
  <p>Validate NIF, NIE, CIF and IBAN with a single API call. Works in any programming language. No setup required.</p>
  <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="btn">Get Free API Key</a>
  <a href="/docs" class="btn btn-outline">Interactive Docs</a>
</section>

<div class="section">
  <h2>4 Endpoints. Everything you need.</h2>
  <div class="endpoints">
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/nif</span>
      <p>Validate Spanish NIF for individuals. Handles K, L, M special cases.</p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/nie</span>
      <p>Validate NIE for foreign residents. X, Y, Z prefix support.</p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/cif</span>
      <p>Validate company CIF. Returns entity type: S.A., S.L., Cooperative...</p>
    </div>
    <div class="endpoint">
      <span class="method">GET</span>
      <span class="path">/validate/iban</span>
      <p>Validate IBAN for 77 countries. Returns bank name for Spanish accounts.</p>
    </div>
  </div>

  <h2>Quick Start</h2>
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
    <h4>IBAN Response example</h4>
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

<div style="background:#f8fafc; padding: 64px 20px;">
  <div style="max-width:960px; margin:0 auto;">
    <h2 style="font-size:1.8rem; font-weight:700; text-align:center; margin-bottom:32px;">Pricing</h2>
    <div class="pricing">
      <div class="plan">
        <h3>Basic</h3>
        <div class="price">$0<span>/mo</span></div>
        <div class="requests">500 requests / month</div>
        <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="cta">Get Started Free</a>
      </div>
      <div class="plan featured">
        <h3>Pro</h3>
        <div class="price">$9<span>/mo</span></div>
        <div class="requests">15,000 requests / month</div>
        <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="cta">Subscribe</a>
      </div>
      <div class="plan">
        <h3>Ultra</h3>
        <div class="price">$29<span>/mo</span></div>
        <div class="requests">100,000 requests / month</div>
        <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1" class="cta">Subscribe</a>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <h2>Frequently Asked Questions</h2>
  <div class="faq">
    <div class="faq-item">
      <h3>What is a NIF?</h3>
      <p>NIF (Número de Identificación Fiscal) is the tax ID for Spanish individuals. Format: 8 digits + 1 control letter (e.g. 12345678Z).</p>
    </div>
    <div class="faq-item">
      <h3>What is a CIF?</h3>
      <p>CIF (Código de Identificación Fiscal) is the tax ID for Spanish companies. The API also returns the entity type: S.A., S.L., Cooperative, etc.</p>
    </div>
    <div class="faq-item">
      <h3>Does it work for non-Spanish IBANs?</h3>
      <p>Yes. The IBAN validator supports 77 countries using the standard mod-97 algorithm. Bank name lookup is only available for Spanish accounts.</p>
    </div>
    <div class="faq-item">
      <h3>Do I need to sign up?</h3>
      <p>Yes, a free RapidAPI account is required to get your API key. The free tier includes 500 requests/month with no credit card needed.</p>
    </div>
    <div class="faq-item">
      <h3>What programming languages are supported?</h3>
      <p>Any language that can make HTTP GET requests. RapidAPI provides code snippets for JavaScript, Python, PHP, Ruby, Go, Java, Swift and more.</p>
    </div>
  </div>
</div>

<footer>
  <p>Spain Document Validator API &mdash; Available on <a href="https://rapidapi.com/Validatorapi/api/spain-document-validator1">RapidAPI</a> &mdash; <a href="/docs">API Docs</a></p>
</footer>

</body>
</html>"""
