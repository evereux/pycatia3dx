from enum import Enum


class CATAxisSystemAxisType(Enum):
    catAxisSystemAxisOppositeDirection = 0
    catAxisSystemAxisSameDirection = 1
    catAxisSystemAxisByCoordinates = 2


class CATAxisSystemMainType(Enum):
    catAxisSystemExplicit = 0
    catAxisSystemEulerAngles = 1
    catAxisSystemAxisRotation = 2
    catAxisSystemStandard = 3


class CATAxisSystemOriginType(Enum):
    catAxisSystemOriginByCoordinates = 0
    catAxisSystemOriginByPoint = 1


class CatConstraintAngleSector(Enum):
    catCstAngleSector3 = 0
    catCstAngleSector1 = 1
    catCstAngleSector0 = 2
    catCstAngleSector2 = 3


class CatConstraintDistConfig(Enum):
    catCstDCParallel = 0
    catCstDCParallelSameOrient = 1
    catCstDCParallelOppOrient = 2
    catCstDCUnspec = 3


class CatConstraintDistDirection(Enum):
    catCstDistDirection2 = 0
    catCstDistDirectionNone = 1
    catCstDistDirection3 = 2
    catCstDistDirection1 = 3


class CatConstraintMode(Enum):
    catCstModeDrivingDimension = 0
    catCstModeDrivenDimension = 1


class CatConstraintOrientation(Enum):
    catCstOrientOpposite = 0
    catCstOrientSame = 1
    catCstOrientUndefined = 2


class CatConstraintRefAxis(Enum):
    catCstRefAxisZ = 0
    catCstRefAxisY = 1
    catCstRefAxisX = 2


class CatConstraintRefType(Enum):
    catCstRefTypeRelative = 0
    catCstRefTypeFixInSpace = 1


class CatConstraintSide(Enum):
    catCstSideUndefined = 0
    catCstSideSameAsValue = 1
    catCstSidePositive = 2
    catCstSideNegative = 3
    catCstSideOppositeToValue = 4


class CatConstraintStatus(Enum):
    catCstStatusOK = 0
    catCstStatusKOBroken = 1
    catCstStatusKOStronglyNotSatisfied = 2
    catCstStatusKOWrongValue = 3
    catCstStatusKOWrongOrientOrSide = 4
    catCstStatusKOWrongGeomEltType = 5


class CatConstraintType(Enum):
    catCstTypePoncContact = 0
    catCstTypeHorizontality = 1
    catCstTypeMidPoint = 2
    catCstTypeSdContinuity = 3
    catCstTypeCurvilinearDistance = 4
    catCstTypeParallelism = 5
    catCstTypeEquidistance = 6
    catCstTypeVerticality = 7
    catCstTypeMajorRadius = 8
    catCstTypeCylinderRadius = 9
    catCstTypeTangency = 10
    catCstTypeChamferPerpend = 11
    catCstTypePerpendicularity = 12
    catCstTypeChamfer = 13
    catCstTypeOn = 14
    catCstTypeLength = 15
    catCstTypeAnnulContact = 16
    catCstTypePlanarAngle = 17
    catCstTypeAxisParallelism = 18
    catCstTypeAxisPerpendicularity = 19
    catCstTypeReference = 20
    catCstTypeRadius = 21
    catCstTypeSdShape = 22
    catCstTypeDistance = 23
    catCstTypeMinorRadius = 24
    catCstTypeLinContact = 25
    catCstTypeStContinuity = 26
    catCstTypeSymmetry = 27
    catCstTypeConcentricity = 28
    catCstTypeAngle = 29
    catCstTypeSurfContact = 30
    catCstTypeStDistance = 31


