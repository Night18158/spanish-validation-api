CIF_CONTROL_LETTERS = "JABCDEFGHI"

CIF_ENTITY_TYPES = {
    "A": "Sociedad Anónima",
    "B": "Sociedad de Responsabilidad Limitada",
    "C": "Sociedad Colectiva",
    "D": "Sociedad Comanditaria",
    "E": "Comunidad de Bienes",
    "F": "Sociedad Cooperativa",
    "G": "Asociación o Fundación",
    "H": "Comunidad de Propietarios en Régimen de Propiedad Horizontal",
    "J": "Sociedad Civil",
    "N": "Entidad Extranjera",
    "P": "Corporación Local",
    "Q": "Organismo Público",
    "R": "Congregación e Institución Religiosa",
    "S": "Órgano de la Administración del Estado y CC.AA.",
    "T": "Establecimiento Permanente de Entidad no Residente",
    "U": "Unión Temporal de Empresas",
    "V": "Otros tipos no definidos en el resto de claves",
    "W": "Establecimiento permanente de entidad no residente en España",
}

CIF_LETTER_CONTROL = set("PQRSW")
CIF_DIGIT_CONTROL = set("ABEH")


def validate_cif(value: str) -> dict:
    value = value.strip().upper()

    if len(value) != 9:
        return {"input": value, "valid": False, "error": "Must be exactly 9 characters"}

    entity_letter = value[0]
    if entity_letter not in CIF_ENTITY_TYPES:
        return {
            "input": value,
            "valid": False,
            "error": f"Unrecognized entity type letter: {entity_letter}",
        }

    try:
        digits = [int(d) for d in value[1:8]]
    except ValueError:
        return {"input": value, "valid": False, "error": "Positions 2-8 must be digits"}

    odd_sum = 0
    for i in (0, 2, 4, 6):
        doubled = digits[i] * 2
        odd_sum += doubled if doubled < 10 else doubled - 9

    even_sum = digits[1] + digits[3] + digits[5]

    total = odd_sum + even_sum
    control_digit = (10 - (total % 10)) % 10
    control_letter = CIF_CONTROL_LETTERS[control_digit]

    last_char = value[8]

    if entity_letter in CIF_LETTER_CONTROL:
        valid = last_char == control_letter
    elif entity_letter in CIF_DIGIT_CONTROL:
        valid = last_char == str(control_digit)
    else:
        valid = last_char == str(control_digit) or last_char == control_letter

    return {
        "input": value,
        "valid": valid,
        "type": "CIF",
        "entity_type": CIF_ENTITY_TYPES[entity_letter],
        "expected_control": control_letter if entity_letter in CIF_LETTER_CONTROL else (
            str(control_digit) if entity_letter in CIF_DIGIT_CONTROL else
            f"{control_digit} or {control_letter}"
        ),
    }
