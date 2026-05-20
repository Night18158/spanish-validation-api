from validators.nif import validate_nif, validate_nie
from validators.cif import validate_cif
from validators.iban import validate_iban


def detect_and_validate(value: str) -> dict:
    v = value.strip().upper().replace(" ", "").replace("-", "")

    # IBAN: starts with 2 letters + 2 digits, length >= 15
    if len(v) >= 4 and v[:2].isalpha() and v[2:4].isdigit() and len(v) >= 15:
        result = validate_iban(value)
        result["detected_as"] = "IBAN"
        return result

    if len(v) == 9:
        # NIE: starts with X, Y or Z
        if v[0] in "XYZ":
            result = validate_nie(value)
            result["detected_as"] = "NIE"
            return result

        # CIF: starts with a letter that is a valid CIF entity type
        cif_prefixes = set("ABCDEFGHJNPQRSTUVW")
        if v[0] in cif_prefixes and v[1:8].isdigit():
            result = validate_cif(value)
            result["detected_as"] = "CIF"
            return result

        # NIF: 8 digits + letter, or K/L/M prefix
        if v[0] in "KLM" or (v[:8].isdigit() and v[8].isalpha()):
            result = validate_nif(value)
            result["detected_as"] = "NIF"
            return result

    return {
        "input": value,
        "valid": False,
        "detected_as": None,
        "error": "Could not identify document type. Expected NIF (8 digits + letter), NIE (X/Y/Z + 7 digits + letter), CIF (letter + 7 digits + control), or IBAN.",
    }
