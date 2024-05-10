from dataclasses import dataclass
from enum import Enum


@dataclass
class Indicator:
    value: int
    type: int
    unit: str


@dataclass
class GWP(Indicator):
    value: float
    type: int = 0
    unit: str = "kg CO₂ eq."


@dataclass
class ODP(Indicator):
    value: float
    type: int = 1
    unit: str = "kg CFC11 eq."


@dataclass
class AP(Indicator):
    value: float
    type: int = 2
    unit: str = "mol H+ eq."


@dataclass
class EP(Indicator):
    value: float
    type: int = 3
    unit: str = "kg PO₄ eq."


@dataclass
class POCP(Indicator):
    value: float
    type: int = 4
    unit: str = "kg NMVOC eq."


@dataclass
class ADPE(Indicator):
    value: float
    type: int = 5
    unit: str = "kg Sb eq."


@dataclass
class ADPF(Indicator):
    value: float
    type: int = 6
    unit: str = "MJ"


@dataclass
class HTP(Indicator):
    value: float
    type: int = 7
    unit: str = "CTUh"


@dataclass
class FAETP(Indicator):
    value: float
    type: int = 8
    unit: str = "kg 1.4-DB-eq"


@dataclass
class TETP(Indicator):
    value: float
    type: int = 9
    unit: str = "kg 1.4-DB-eq"


@dataclass
class ECI(Indicator):
    value: float
    type: int = 10
    unit: str = "Euro"


@dataclass
class MAETP(Indicator):
    value: float
    type: int = 11
    unit: str = "kg 1.4-DB-eq"


@dataclass
class GWP_TOTAL(Indicator):
    value: float
    type: int = 12
    unit: str = "kg CO₂ eq."


@dataclass
class GWP_BIOGENIC(Indicator):
    value: float
    type: int = 13
    unit: str = "kg CO₂ eq."


@dataclass
class GWP_FOSSIL(Indicator):
    value: float
    type: int = 14
    unit: str = "kg CO₂ eq."


@dataclass
class PERE(Indicator):
    value: float
    type: int = 15
    unit: str = "MJ"


@dataclass
class PERM(Indicator):
    value: float
    type: int = 16
    unit: str = "MJ"


@dataclass
class PERT(Indicator):
    value: float
    type: int = 17
    unit: str = "MJ"


@dataclass
class PENRE(Indicator):
    value: float
    type: int = 18
    unit: str = "MJ"


@dataclass
class PENRM(Indicator):
    value: float
    type: int = 19
    unit: str = "MJ"


@dataclass
class PENRT(Indicator):
    value: float
    type: int = 20
    unit: str = "MJ"


@dataclass
class SM(Indicator):
    value: float
    type: int = 21
    unit: str = "kg"


@dataclass
class RSF(Indicator):
    value: float
    type: int = 22
    unit: str = "MJ"


@dataclass
class NRSF(Indicator):
    value: float
    type: int = 23
    unit: str = "MJ"


@dataclass
class FW(Indicator):
    value: float
    type: int = 24
    unit: str = "m³"


@dataclass
class HWD(Indicator):
    value: float
    type: int = 25
    unit: str = "kg"


@dataclass
class MHWD(Indicator):
    value: float
    type: int = 26
    unit: str = "-"


@dataclass
class RWD(Indicator):
    value: float
    type: int = 27
    unit: str = "kg"


@dataclass
class CRU(Indicator):
    value: float
    type: int = 28
    unit: str = "kg"


@dataclass
class MFR(Indicator):
    value: float
    type: int = 29
    unit: str = "kg"


@dataclass
class MER(Indicator):
    value: float
    type: int = 30
    unit: str = "kg"


@dataclass
class EEE(Indicator):
    value: float
    type: int = 31
    unit: str = "MJ"


@dataclass
class EET(Indicator):
    value: float
    type: int = 32
    unit: str = "MJ"


@dataclass
class NHWD(Indicator):
    value: float
    type: int = 33
    unit: str = "kg"


@dataclass
class EP_FRESHWATER(Indicator):
    value: float
    type: int = 34
    unit: str = "kg P eq."


@dataclass
class EP_TERRESTRIAL(Indicator):
    value: float
    type: int = 35
    unit: str = "mol N eq."


@dataclass
class EP_MARINE(Indicator):
    value: float
    type: int = 36
    unit: str = "kg N eq."


@dataclass
class ETP_FW(Indicator):
    value: float
    type: int = 37
    unit: str = "CTUe"


@dataclass
class HTP_C(Indicator):
    value: float
    type: int = 38
    unit: str = "CTUh"


@dataclass
class HTP_NC(Indicator):
    value: float
    type: int = 39
    unit: str = "CTUh"


@dataclass
class AD_MM(Indicator):
    value: float
    type: int = 40
    unit: str = "-"


@dataclass
class ADP_FOS(Indicator):
    value: float
    type: int = 41
    unit: str = "MJ"


@dataclass
class GWP_LULUC(Indicator):
    value: float
    type: int = 42
    unit: str = "kg CO₂ eq."


@dataclass
class ADPM(Indicator):
    value: float
    type: int = 43
    unit: str = "-"


@dataclass
class WDP(Indicator):
    value: float
    type: int = 44
    unit: str = "m³ world eq. Deprived"


@dataclass
class PM(Indicator):
    value: float
    type: int = 45
    unit: str = "Disease incidence"


@dataclass
class IRP(Indicator):
    value: float
    type: int = 46
    unit: str = "kBq U235 eq."


class IndicatorType(Enum):
    GWP = GWP
    ODP = ODP
    AP = AP
    EP = EP
    POCP = POCP
    ADPE = ADPE
    ADPF = ADPF
    HTP = HTP
    FAETP = FAETP
    TETP = TETP
    ECI = ECI
    MAETP = MAETP
    GWP_TOTAL = GWP_TOTAL
    GWP_BIOGENIC = GWP_BIOGENIC
    GWP_FOSSIL = GWP_FOSSIL
    PERE = PERE
    PERM = PERM
    PERT = PERT
    PENRE = PENRE
    PENRM = PENRM
    PENRT = PENRT
    SM = SM
    RSF = RSF
    NRSF = NRSF
    FW = FW
    HWD = HWD
    MHWD = MHWD
    RWD = RWD
    CRU = CRU
    MFR = MFR
    MER = MER
    EEE = EEE
    EET = EET
    NHWD = NHWD
    EP_FRESHWATER = EP_FRESHWATER
    EP_TERRESTRIAL = EP_TERRESTRIAL
    EP_MARINE = EP_MARINE
    ETP_FW = ETP_FW
    HTP_C = HTP_C
    HTP_NC = HTP_NC
    AD_MM = AD_MM
    ADP_FOS = ADP_FOS
    GWP_LULUC = GWP_LULUC
    ADPM = ADPM
    WDP = WDP
    PM = PM
    IRP = IRP


if __name__ == "__main__":
    test = IndicatorType.GWP.value(value=100)
    pass

# TODO: Map the indicators
