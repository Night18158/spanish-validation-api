IBAN_LENGTHS = {
    "AD": 24, "AE": 23, "AL": 28, "AT": 20, "AZ": 28,
    "BA": 20, "BE": 16, "BG": 22, "BH": 22, "BR": 29,
    "BY": 28, "CH": 21, "CR": 22, "CY": 28, "CZ": 24,
    "DE": 22, "DK": 18, "DO": 28, "EE": 20, "EG": 29,
    "ES": 24, "FI": 18, "FK": 18, "FO": 18, "FR": 27,
    "GB": 22, "GE": 22, "GI": 23, "GL": 18, "GR": 27,
    "GT": 28, "HR": 21, "HU": 28, "IE": 22, "IL": 23,
    "IQ": 23, "IS": 26, "IT": 27, "JO": 30, "KW": 30,
    "KZ": 20, "LB": 28, "LC": 32, "LI": 21, "LT": 20,
    "LU": 20, "LV": 21, "LY": 25, "MC": 27, "MD": 24,
    "ME": 22, "MK": 19, "MR": 27, "MT": 31, "MU": 30,
    "MZ": 25, "NL": 18, "NO": 15, "PK": 24, "PL": 28,
    "PS": 29, "PT": 25, "QA": 29, "RO": 24, "RS": 22,
    "SA": 24, "SC": 31, "SD": 18, "SE": 24, "SI": 19,
    "SK": 24, "SM": 27, "ST": 25, "SV": 28, "TL": 23,
    "TN": 24, "TR": 26, "UA": 29, "VA": 22, "VG": 24,
    "XK": 20,
}

SPANISH_BANKS = {
    "0049": "Santander",
    "0075": "Banco Popular",
    "0081": "Banco Sabadell",
    "0128": "Bankinter",
    "0182": "BBVA",
    "2038": "Bankia / CaixaBank",
    "2100": "CaixaBank",
    "3025": "Ibercaja",
    "3035": "Banco Caminos",
    "3058": "Cajamar",
    "3183": "Caja Rural del Sur",
    "6016": "Openbank",
    "6038": "WiZink",
    "0073": "Openbank (Santander Digital)",
}


def validate_iban(value: str) -> dict:
    iban = value.strip().upper().replace(" ", "").replace("-", "")

    if len(iban) < 5:
        return {"input": value, "valid": False, "error": "IBAN demasiado corto"}

    country = iban[:2]
    if not country.isalpha():
        return {"input": value, "valid": False, "error": "Los primeros 2 caracteres deben ser el código de país (ej: ES, DE)"}

    expected_length = IBAN_LENGTHS.get(country)
    if expected_length is None:
        return {"input": value, "valid": False, "error": f"Código de país no reconocido: {country}"}

    if len(iban) != expected_length:
        return {
            "input": value,
            "valid": False,
            "error": f"El IBAN de {country} debe tener {expected_length} caracteres (recibidos: {len(iban)})",
        }

    # Rearrange: move first 4 chars to the end
    rearranged = iban[4:] + iban[:4]

    # Replace each letter with its numeric equivalent (A=10, B=11, ...)
    numeric_str = ""
    for char in rearranged:
        if char.isalpha():
            numeric_str += str(ord(char) - ord("A") + 10)
        else:
            numeric_str += char

    valid = int(numeric_str) % 97 == 1

    result = {
        "input": value,
        "valid": valid,
        "type": "IBAN",
        "country": country,
        "formatted": " ".join(iban[i:i+4] for i in range(0, len(iban), 4)),
    }

    if country == "ES" and len(iban) == 24:
        bank_code = iban[4:8]
        result["bank_code"] = bank_code
        result["branch_code"] = iban[8:12]
        result["bank_name"] = SPANISH_BANKS.get(bank_code, "Entidad no identificada")

    return result
