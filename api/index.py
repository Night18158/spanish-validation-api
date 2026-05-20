import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from validators.nif import validate_nif, validate_nie
from validators.cif import validate_cif
from validators.iban import validate_iban

app = FastAPI(
    title="Spanish Data Validation API",
    description=(
        "Complete validation suite for Spanish fiscal and identification documents. "
        "Supports NIF, NIE, CIF and IBAN validation with detailed responses."
    ),
    version="1.0.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Status"])
def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get(
    "/validate/nif",
    tags=["Validation"],
    summary="Validate a Spanish NIF",
    response_description="Validation result with document type",
)
def nif_endpoint(
    value: str = Query(..., description="NIF to validate. Example: 12345678Z"),
):
    """
    Validates a Spanish NIF (Número de Identificación Fiscal).

    Also accepts the special prefixed formats K, L and M.

    Returns whether the NIF is valid and its subtype.
    """
    return validate_nif(value)


@app.get(
    "/validate/nie",
    tags=["Validation"],
    summary="Validate a Spanish NIE",
    response_description="Validation result",
)
def nie_endpoint(
    value: str = Query(..., description="NIE to validate. Example: X1234567L"),
):
    """
    Validates a Spanish NIE (Número de Identificación de Extranjero).

    NIE numbers start with X, Y or Z followed by 7 digits and a control letter.
    """
    return validate_nie(value)


@app.get(
    "/validate/cif",
    tags=["Validation"],
    summary="Validate a Spanish CIF",
    response_description="Validation result with entity type",
)
def cif_endpoint(
    value: str = Query(..., description="CIF to validate. Example: B12345678"),
):
    """
    Validates a Spanish CIF (Código de Identificación Fiscal) for legal entities.

    Returns the entity type (S.L., S.A., Cooperative, etc.) when valid.
    """
    return validate_cif(value)


@app.get(
    "/validate/iban",
    tags=["Validation"],
    summary="Validate an IBAN (all countries)",
    response_description="Validation result with bank details for Spanish IBANs",
)
def iban_endpoint(
    value: str = Query(
        ...,
        description="IBAN to validate. Spaces and dashes are ignored. Example: ES91 2100 0418 4502 0005 1332",
    ),
):
    """
    Validates an IBAN number for any supported country.

    For Spanish IBANs (ES), also returns the bank code, branch code and bank name when known.

    Supports 77 countries.
    """
    return validate_iban(value)
