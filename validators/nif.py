NIF_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

SPECIAL_PREFIX = {
    "K": "Spanish citizen under 14 or foreigner without NIE",
    "L": "Spanish citizen over 14 residing abroad",
    "M": "Foreigner without permanent NIE",
}


def validate_nif(value: str) -> dict:
    value = value.strip().upper()

    if len(value) != 9:
        return {"input": value, "valid": False, "error": "Must be exactly 9 characters"}

    if value[0] in SPECIAL_PREFIX:
        try:
            number = int(value[1:8])
        except ValueError:
            return {"input": value, "valid": False, "error": "Characters 2-8 must be digits"}
        expected = NIF_LETTERS[number % 23]
        return {
            "input": value,
            "valid": value[8] == expected,
            "type": "NIF_SPECIAL",
            "subtype": SPECIAL_PREFIX[value[0]],
            "expected_letter": expected,
        }

    try:
        number = int(value[:8])
    except ValueError:
        return {"input": value, "valid": False, "error": "First 8 characters must be digits"}

    if not value[8].isalpha():
        return {"input": value, "valid": False, "error": "Last character must be a letter"}

    expected = NIF_LETTERS[number % 23]
    return {
        "input": value,
        "valid": value[8] == expected,
        "type": "NIF",
        "expected_letter": expected,
    }


def validate_nie(value: str) -> dict:
    value = value.strip().upper()

    if len(value) != 9:
        return {"input": value, "valid": False, "error": "Must be exactly 9 characters"}

    if value[0] not in "XYZ":
        return {"input": value, "valid": False, "error": "NIE must start with X, Y or Z"}

    substitution = {"X": "0", "Y": "1", "Z": "2"}
    nie_as_nif = substitution[value[0]] + value[1:]

    try:
        number = int(nie_as_nif[:8])
    except ValueError:
        return {"input": value, "valid": False, "error": "Invalid format — characters 2-8 must be digits"}

    expected = NIF_LETTERS[number % 23]
    return {
        "input": value,
        "valid": value[8] == expected,
        "type": "NIE",
        "expected_letter": expected,
    }
