from dataclasses import dataclass
from enum import Enum
from typing import Sequence

from pdf_to_lca_materials.rlca_client.indicator import Indicator


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


class ModuleStatus(Enum):
    NOT_RELEVANT = "0"
    NOT_DECLARED = "1"
    RELEVANT = "2"


@dataclass
class LciaResult:
    moduleStatusEnum: int
    moduleTypeEnum: ModuleStage
    indicators: Sequence[Indicator]
