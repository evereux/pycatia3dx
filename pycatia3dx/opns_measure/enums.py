from enum import Enum


class CATMeasurableContextType(Enum):
    PartContext = 0
    ProductContext = 1


class CATMeasurableModeOfCalc(Enum):
    MeasExactElseApproxCalculation = 0
    MeasUnknownCalculation = 1
    MeasExactCalculation = 2
    MeasApproximateCalculation = 3


class CATMeasurableType(Enum):
    CAAMeasurableCone = 0
    CAAMeasurableCurve = 1
    CAAMeasurableBetween = 2
    CAAMeasurableCylinder = 3
    CAAMeasurableSurface = 4
    CAAMeasurableVolume = 5
    CAAMeasurablePoint = 6
    CAAMeasurableSphere = 7
    CAAMeasurablePlane = 8
    CAAMeasurableCircle = 9
    CAAMeasurableAxisSystem = 10
    CAAMeasurableLine = 11


class CATOpnsMeasureDistanceType(Enum):
    catOpnsMaximumDistance12 = 0
    catOpnsMinimumDistanceAlongDir = 1
    catOpnsBandAnalysis = 2
    catOpnsMaximumDistance = 3
    catOpnsMinimumDistance = 4
    catOpnsUnknownDistance = 5


class CATOpnsMeasureEdgeType(Enum):
    catOpnsAxisEdge = 0
    catOpnsArcEdge = 1
    catOpnsUnknownEdge = 2
    catOpnsHyperbolaEdge = 3
    catOpnsCurveEdge = 4
    catOpnsEllipseEdge = 5
    catOpnsLineEdge = 6
    catOpnsParabolaEdge = 7


class CATOpnsMeasureExtensionMode(Enum):
    catOpnsInfiniteExtend = 0
    catOpnsFiniteExtend = 1


class CATOpnsMeasureItemType(Enum):
    catOpnsSurface2DItem = 0
    catOpnsPointItem = 1
    catOpnsVolumeItem = 2
    catOpnsUnknownItem = 3
    catOpnsThicknessItem = 4
    catOpnsAngle3PtsItem = 5
    catOpnsEdgeItem = 6
    catOpnsComplexItem = 7
    catOpnsSurfaceItem = 8
    catOpnsNotValid = 9


class CATOpnsMeasureSurfaceType(Enum):
    catOpnsUnknownSurface = 0
    catOpnsPlaneSurface = 1
    catOpnsCylinderSurface = 2
    catOpnsSphereSurface = 3
    catOpnsConeSurface = 4
    catOpnsTorusSurface = 5


class CATResultCalcType(Enum):
    ResMixedCalculation = 0
    ResExactCalculation = 1
    ResUnknownCalculation = 2
    ResApproximateCalculation = 3


