from datetime import datetime
from typing import Sequence

import pydantic
from pdf_to_lca_materials.rlca_client.lcia_result import LciaResult


class DeclaredUnit(pydantic.BaseModel):
    declaredUnit: int
    declaredValue: int
    mass: int
    massUnit: int


class EpdInfo(pydantic.BaseModel):
    epdSpecificationForm: int
    epdProductIndustryType: int
    publicationDate: datetime
    validTo: datetime
    declarationOwnerId: str
    sourceEpdUrl: str
    dataSourceId: str
    fileEntityId: str
    epdVersion: int
    declarationNumber: str


class Material(pydantic.BaseModel):
    tenantId: str
    isPublic: bool
    isCustom: bool
    expectedLifespan: int  # In years
    name: str
    description: str
    lciaResults: Sequence[LciaResult]
    declaredUnit: DeclaredUnit
    epdInfo: EpdInfo
    tags: Sequence[str]
