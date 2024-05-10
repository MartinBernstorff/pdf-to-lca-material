import datetime as dt

from pdf_to_lca_materials.rlca_client.material import DeclaredUnit, EpdInfo, Material

test_material = Material(
    tenantId="30f95646-f60f-4773-ab08-b64d5a60ba5e",
    isPublic=False,
    isCustom=True,
    expectedLifespan=10,
    name="MBAutoTest",
    description="MBAutoTest",
    lciaResults=[],
    declaredUnit=DeclaredUnit(declaredUnit=0, declaredValue=0, mass=0, massUnit=0),
    epdInfo=EpdInfo(
        epdSpecificationForm=0,
        epdProductIndustryType=0,
        publicationDate=dt.datetime.now(),
        validTo=dt.datetime.now() + dt.timedelta(days=1),
        declarationOwnerId="cbc10878-85b1-4190-a523-e47b25a6a86d",
        sourceEpdUrl="www.realtimelca.com",
        dataSourceId="cf1bca75-0e00-40f1-8666-a72e6b501e09",
        fileEntityId="",
        epdVersion=0,
        declarationNumber="1212-232132",
    ),
    tags=[],
)
