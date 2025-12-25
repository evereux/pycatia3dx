from enum import Enum


class CatAssemblyConstraintMode(Enum):
    catControlledMode = 0
    catMeasuredMode = 1
    catDrivingMode = 2


class CatAssemblyConstraintOption(Enum):
    catOptionFullAxisxneg = 0
    catOptionSector4 = 1
    catOptionAxisSystemX = 2
    catOptionSameOrientation = 3
    catOptionFullAxisy = 4
    catOptionFullAxisx = 5
    catOptionFullAxisyneg = 6
    catOptionAxisSystemZ = 7
    catOptionLineUndefinedOrientation = 8
    catOptionOppositeOrientation = 9
    catOptionSymmetryZX = 10
    catOptionLineOppositeOrientation = 11
    catOptionAxisSystemY = 12
    catOptionSymmetryXY = 13
    catOptionSector1 = 14
    catOptionLineSameOrientation = 15
    catOptionFullAxiszneg = 16
    catOptionSector3 = 17
    catOptionSymmetryYZ = 18
    catOptionFullAxisz = 19
    catOptionUndefinedOrientation = 20
    catOptionSector2 = 21


class CatAssemblyConstraintType(Enum):
    catContactCircleCone = 0
    catParallelismLinePlane = 1
    catSymmetryPlanePlanePlane = 2
    catPerpendicularityLinePlane = 3
    catUniversalAxisSystemAxisSystem = 4
    catCouplingLengthLength = 5
    catAngleLinePlane = 6
    catContactConeCone = 7
    catDistanceLineLine = 8
    catContactSphereCone = 9
    catAnglePlanePlaneLine = 10
    catContactCylinderCylinder = 11
    catSymmetryInstanceInstancePlane = 12
    catContactPlanePlane = 13
    catParallelismPlanePlane = 14
    catCable = 15
    catSphericalAxisSystemAxisSystem = 16
    catFixTransfoAxisSystem = 17
    catCoincidenceAxisSystemAxisSystem = 18
    catFixInstance = 19
    catGear = 20
    catCoincidencePointPlane = 21
    catAnglePlanePlane = 22
    catCoincidenceLineLine = 23
    catParallelismLineLine = 24
    catCoincidencePointSurface = 25
    catCoincidencePointPoint = 26
    catRevoluteAxisSystemAxisSystem = 27
    catSymmetryLineLinePlane = 28
    catFixTransfoInstanceAxisSystem = 29
    catSymmetryAxisSystemAxisSystemPlane = 30
    catContactPlaneCylinder = 31
    catUserDefinedConstraint = 32
    catFixTransfoInstanceInstance = 33
    catCoincidencePlanePlane = 34
    catFixTransfoAxisSystemAxisSystem = 35
    catSymmetryPointPointPlane = 36
    catFixTransfoInstance = 37
    catDistancePlanePlane = 38
    catContactSphereSphere = 39
    catRack = 40
    catDistancePointLine = 41
    catCoincidenceLinePlane = 42
    catCylindricalAxisSystemAxisSystem = 43
    catFixInstanceInstance = 44
    catPerpendicularityLineLine = 45
    catPerpendicularityPlanePlane = 46
    catPlanarAxisSystemAxisSystem = 47
    catDistanceLinePlane = 48
    catAngleLineLine = 49
    catCoincidencePointCurve = 50
    catPrismaticAxisSystemAxisSystem = 51
    catContactCircleSphere = 52
    catFixAxisSystem = 53
    catCouplingLengthAngle = 54
    catDistancePointPlane = 55
    catFixInstanceAxisSystem = 56
    catCoincidencePointLine = 57
    catCouplingAngleAngle = 58
    catDistancePointPoint = 59
    catFixAxisSystemAxisSystem = 60
    catContactPlaneSphere = 61
    catLengthPointCurve = 62


class CatEngConnectionDirection(Enum):
    catDirectionIn = 0
    catDirectionOut = 1


class CatEngConnectionType(Enum):
    catEngRack = 0
    catCylindrical = 1
    catRigid = 2
    catProjection = 3
    catFree = 4
    catPointCurve = 5
    catSlideCurve = 6
    catUniversal = 7
    catSymmetry = 8
    catPlanar = 9
    catRollCurve = 10
    catSpherical = 11
    catUserDefined = 12
    catEngScrew = 13
    catRevolute = 14
    catPrismatic = 15
    catFix = 16
    catEngCable = 17
    catEngGear = 18
    catPointSurface = 19


