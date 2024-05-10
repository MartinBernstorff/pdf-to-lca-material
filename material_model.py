from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Sequence
from uuid import UUID


class ModuleStage(Enum):
    A1A3 = "0"
    A1 = "1"
    A2 = "2"
    A3 = "3"
    A4 = "4"
    A5 = "5"
    B1 = "6"
    B2 = "7"
    B3 = "8"
    B4 = "9"
    B5 = "10"
    B6 = "11"
    B7 = "12"
    C1 = "13"
    C2 = "14"
    C3 = "15"
    C4 = "16"
    D = "17"


class moduleStatus(Enum):
    NOT_RELEVANT = "0"
    NOT_DECLARED = "1"
    RELEVANT = "2"


@dataclass
class DeclaredUnit:
    declaredUnit: int
    declaredValue: int
    mass: int
    massUnit: int


@dataclass
class EpdInfo:
    epdSpecificationForm: int
    epdProductIndustryType: int
    publicationDate: datetime
    validTo: datetime
    declarationOwnerId: UUID
    sourceEpdUrl: str
    dataSourceId: UUID
    fileEntityId: str
    epdVersion: int
    declarationNumber: str


@dataclass
class Indicator:
    type: int
    unit: str
    value: int


@dataclass
class LciaResult:
    moduleStatusEnum: int
    moduleTypeEnum: ModuleStage
    indicators: Sequence[Indicator]


@dataclass
class Material:
    tenantId: int
    isPublic: bool
    isCustom: bool
    expectedLifespan: int  # In years
    name: str
    description: str
    lciaResults: Sequence[LciaResult]
    declaredUnit: DeclaredUnit
    epdInfo: EpdInfo
    tags: Sequence[str]
