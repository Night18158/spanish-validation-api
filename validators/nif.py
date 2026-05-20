NIF_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

SPECIAL_PREFIX = {
    "K": "Español menor de 14 años o extranjero sin NIE",
    "L": "Español mayor de 14 años residente en el extranjero",
    "M": "Extranjero sin NIE permanente",
}


def validate_nif(value: str) -> dict:
    value = value.strip().upper()

    if len(value) != 9:
        return {"input": value, "valid": False, "error": "Debe tener exactamente 9 caracteres"}

    if value[0] in SPECIAL_PREFIX:
        try:
            number = int(value[1:8])
        except ValueError:
            return {"input": value, "valid": False, "error": "Los caracteres 2-8 deben ser dígitos"}
        expected = NIF_LETTERS[number % 23]
        return {
            "input": value,
            "valid": value[8] == expected,
            "type": "NIF_ESPECIAL",
            "subtype": SPECIAL_PREFIX[value[0]],
        }

    try:
        number = int(value[:8])
    except ValueError:
        return {"input": value, "valid": False, "error": "Los primeros 8 caracteres deben ser dígitos"}

    if not value[8].isalpha():
        return {"input": value, "valid": False, "error": "El último carácter debe ser una letra"}

    expected = NIF_LETTERS[number % 23]
    return {
        "input": value,
        "valid": value[8] == expected,
        "type": "NIF",
    }


def validate_nie(value: str) -> dict:
    value = value.strip().upper()

    if len(value) != 9:
        return {"input": value, "valid": False, "error": "Debe tener exactamente 9 caracteres"}

    if value[0] not in "XYZ":
        return {"input": value, "valid": False, "error": "El NIE debe comenzar con X, Y o Z"}

    substitution = {"X": "0", "Y": "1", "Z": "2"}
    nie_as_nif = substitution[value[0]] + value[1:]

    try:
        number = int(nie_as_nif[:8])
    except ValueError:
        return {"input": value, "valid": False, "error": "Formato inválido — los caracteres 2-8 deben ser dígitos"}

    expected = NIF_LETTERS[number % 23]
    return {
        "input": value,
        "valid": value[8] == expected,
        "type": "NIE",
    }
